param([Parameter(Mandatory=$true)][string]$UnityProject)
$ErrorActionPreference = 'Stop'
$kitRoot = Split-Path $PSScriptRoot -Parent
$projectPath = (Resolve-Path -LiteralPath $UnityProject).Path
if (!(Test-Path -LiteralPath (Join-Path $projectPath 'Assets')) -or !(Test-Path -LiteralPath (Join-Path $projectPath 'ProjectSettings'))) {
    throw 'Select the Unity project root containing Assets and ProjectSettings.'
}
$sourcePath = Join-Path $kitRoot 'Assets/AI_VR_Workshop_V4'
$targetPath = Join-Path $projectPath 'Assets/AI_VR_Workshop_V4'
if (Test-Path -LiteralPath $targetPath) {
    throw 'AI_VR_Workshop_V4 already exists. No files copied. Use a new project copy for a clean reinstall.'
}
Copy-Item -LiteralPath $sourcePath -Destination $targetPath -Recurse
Write-Host 'Copied Assets/AI_VR_Workshop_V4 only. Packages and ProjectSettings were not changed.'
Write-Host 'Open Workshop_Desktop.unity and run Workshop V4 > Validate active workshop scene.'
