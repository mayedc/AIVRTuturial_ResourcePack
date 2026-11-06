# Source-first static repository validation (source-first workflow).
# The old full Unity project is intentionally absent.
$ErrorActionPreference = 'Stop'
$repo = Split-Path -Parent $PSScriptRoot
$validator = Join-Path $PSScriptRoot 'Validation/validate_source_first.py'
if (!(Test-Path -LiteralPath $validator)) {
    throw "Missing source-first validator: $validator"
}
if (Get-Command python -ErrorAction SilentlyContinue) {
    & python $validator
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 $validator
} else {
    throw 'Python 3 is required to run the source-first static checker.'
}
if ($LASTEXITCODE -ne 0) {
    throw "Source-first repository validation failed (exit $LASTEXITCODE)."
}
Write-Host 'Source-only static validation complete. Real Unity Play and Quest HMD remain separate checks.'
