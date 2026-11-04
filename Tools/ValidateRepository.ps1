# Audits the release candidate before publication.
# Prints categories and repository-relative paths only. Never prints secret values.
param(
    [string]$Root = "",
    [switch]$FailOnWarnings
)

$ErrorActionPreference = "Stop"
if ([string]::IsNullOrWhiteSpace($Root)) {
    $Root = Split-Path -Parent $PSScriptRoot
}
$Root = (Resolve-Path -LiteralPath $Root).Path

$archiveName = 'Old' + 'Material'
$forbiddenDirs = @("Library", "Temp", "Obj", "Logs", "UserSettings", "Build", "Builds", ".vs")
$skipDirs = $forbiddenDirs + @(".git", ".vscode", ".idea")
$required = @(
    "Assets",
    "Packages\manifest.json",
    "Packages\packages-lock.json",
    "ProjectSettings\ProjectVersion.txt",
    "ProjectSettings\EditorBuildSettings.asset",
    "README.md",
    "LICENSE",
    ".gitignore",
    "Assets\AI_VR_Workshop_V4\Scenes\Workshop_Desktop.unity",
    "Assets\AI_VR_Workshop_V4\Scenes\Workshop_MetaVR.unity",
    "Assets\AI_VR_Workshop_V4\Runtime\WorkshopDrive.cs",
    "Assets\AI_VR_Workshop_V4\Runtime\WorkshopSpeedControl.cs",
    "SourceArt\Blender\AsterGT.blend",
    "SourceArt\FBX\AsterGT.fbx"
)

$failures = New-Object System.Collections.Generic.List[string]
$warnings = New-Object System.Collections.Generic.List[string]

function Add-Fail([string]$msg) { $script:failures.Add($msg) }
function Add-Warn([string]$msg) { $script:warnings.Add($msg) }

function Test-IgnoredName([string]$rel) {
    $name = Split-Path -Leaf $rel
    if ($name -match '\.(csproj|sln|slnx|user|suo|pidb|tmp|bak|apk|aab)$') { return $true }
    if ($rel -match '(^|[\\/])\.cursor[\\/]mcp\.json$') { return $true }
    if ($rel -match '(^|[\\/])Checkpoints([\\/]|$)') { return $true }
    return $false
}

$gitignore = Join-Path $Root ".gitignore"
if (-not (Test-Path -LiteralPath $gitignore)) {
    Add-Fail "missing-gitignore: .gitignore"
} else {
    $ignoreText = Get-Content -LiteralPath $gitignore -Raw
    $ignoreNormalized = [regex]::Replace($ignoreText, '\[([A-Za-z])[A-Za-z]\]', '$1')
    foreach ($dir in $forbiddenDirs) {
        if ($ignoreNormalized -notmatch ('(?i)' + [regex]::Escape($dir))) {
            Add-Fail "gitignore-missing-rule: $dir"
        }
        $local = Join-Path $Root $dir
        if (Test-Path -LiteralPath $local) {
            Add-Warn "local-generated-dir-present: $dir (must stay untracked)"
        }
    }
    if ($ignoreNormalized -notmatch [regex]::Escape($archiveName)) {
        Add-Warn "gitignore-missing-rule: archived-history-folder"
    }
}

foreach ($rel in $required) {
    if (-not (Test-Path -LiteralPath (Join-Path $Root $rel))) {
        Add-Fail "missing-required: $($rel -replace '\\','/')"
    }
}

$textExt = @{
    ".md"=$true; ".txt"=$true; ".cs"=$true; ".py"=$true; ".ps1"=$true; ".json"=$true
    ".asset"=$true; ".unity"=$true; ".prefab"=$true; ".inputactions"=$true; ".xml"=$true
    ".yml"=$true; ".yaml"=$true; ".shader"=$true; ".hlsl"=$true; ".uss"=$true; ".uxml"=$true
    ".csv"=$true; ".meta"=$true; ".gitignore"=$true; ".gitattributes"=$true; ".editorconfig"=$true
}
$binaryExt = @{ ".blend"=$true; ".fbx"=$true; ".png"=$true; ".jpg"=$true; ".jpeg"=$true; ".psd"=$true; ".mp4"=$true }

$pathRx = [regex]'[A-Za-z]:\\[A-Za-z0-9._ -]+\\|/[Uu]sers/[A-Za-z0-9._-]+|\\[Uu]sers\\'
$cjkRx = [regex]'[\u4E00-\u9FFF]'
$archiveName = 'Old' + 'Material'
$secretRules = @(
    @{ Name = "private-key"; Pattern = 'BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY' },
    @{ Name = "github-token"; Pattern = 'gh' + 'p_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}' },
    @{ Name = "aws-access-key"; Pattern = 'AKIA[0-9A-Z]{16}' },
    @{ Name = "slack-token"; Pattern = 'xox[baprs]-[A-Za-z0-9-]{10,}' },
    @{ Name = "assigned-secret"; Pattern = '(?i)(api[_-]?key|client[_-]?secret|password)[^\S\r\n]*[:=][^\S\r\n]*\S{8,}' }
)

function Get-AsciiRuns([byte[]]$bytes, [int]$minLen) {
    $sb = New-Object System.Text.StringBuilder
    $found = New-Object System.Collections.Generic.List[string]
    foreach ($b in $bytes) {
        if ($b -ge 32 -and $b -le 126) {
            [void]$sb.Append([char]$b)
        } else {
            if ($sb.Length -ge $minLen) { $found.Add($sb.ToString()) }
            [void]$sb.Clear()
        }
    }
    if ($sb.Length -ge $minLen) { $found.Add($sb.ToString()) }
    return $found
}

$scanned = 0
$bytes = [int64]0
Get-ChildItem -LiteralPath $Root -Recurse -File -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $full = $_.FullName
    $rel = $full.Substring($Root.Length).TrimStart('\','/')
    $top = ($rel -split '[\\/]')[0]
    if ($skipDirs -contains $top) { return }
    $bytes += $_.Length
    $posix = $rel -replace '\\','/'
    if ($_.Name -match '[^\x00-\x7F]') {
        Add-Fail "non-english-filename: $posix"
    }
    if ($posix -match ('(^|/)' + [regex]::Escape($archiveName) + '(/|$)')) {
        Add-Fail "archive-folder-inside-release: $posix"
    }
    if ($_.Length -ge 100MB) {
        Add-Fail ("oversized-100mb: {0} ({1:N1} MB)" -f $posix, ($_.Length / 1MB))
    } elseif ($_.Length -ge 50MB) {
        Add-Warn ("large-50mb: {0} ({1:N1} MB)" -f $posix, ($_.Length / 1MB))
    }
    if (Test-IgnoredName $rel) {
        Add-Warn "gitignored-local-file: $posix"
        return
    }
    $scanned++
    $ext = $_.Extension.ToLowerInvariant()
    $scanText = $null
    if ($textExt.ContainsKey($ext) -or $_.Name -in @("README.md","LICENSE","CHANGELOG.md","AGENTS.md",".gitignore",".gitattributes")) {
        $scanText = [System.IO.File]::ReadAllText($full)
    } elseif ($binaryExt.ContainsKey($ext) -and $_.Length -le 40MB) {
        $raw = [System.IO.File]::ReadAllBytes($full)
        $runs = Get-AsciiRuns $raw 12
        $scanText = ($runs -join "`n")
    }
    if ($null -eq $scanText) { return }
    if ($cjkRx.IsMatch($scanText)) {
        Add-Fail "chinese-text: $posix"
    }
    if ($pathRx.IsMatch($scanText)) {
        Add-Fail "absolute-path-pattern: $posix"
    }
    if ($scanText.Contains($archiveName) -and $_.Name -ne ".gitignore") {
        Add-Fail "archive-name-reference: $posix"
    }
    foreach ($rule in $secretRules) {
        if ($scanText -match $rule.Pattern) {
            Add-Fail ("credential-category: {0} in {1}" -f $rule.Name, $posix)
        }
    }
}

Write-Output ("root-kind: release-candidate")
Write-Output ("scanned-files: {0}" -f $scanned)
Write-Output ("scanned-bytes-excluding-forbidden-dirs: {0}" -f $bytes)
Write-Output ("failures: {0}" -f $failures.Count)
foreach ($item in $failures) { Write-Output ("FAIL {0}" -f $item) }
Write-Output ("warnings: {0}" -f $warnings.Count)
foreach ($item in $warnings) { Write-Output ("WARN {0}" -f $item) }
if ($failures.Count -gt 0 -or ($FailOnWarnings -and $warnings.Count -gt 0)) {
    Write-Output "STATUS: FAIL"
    exit 1
}
Write-Output "STATUS: PASS"
exit 0
