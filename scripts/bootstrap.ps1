# Safe preflight only. Does not install packages.
$script = Join-Path $PSScriptRoot 'harness.ps1'
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  Write-Warning 'Git not found. Install Git before cross-PC task handoff.'
}
if ((Get-Command py -ErrorAction SilentlyContinue) -or (Get-Command python -ErrorAction SilentlyContinue)) {
  & $script doctor
  exit $LASTEXITCODE
}
Write-Error 'Python >=3.10 is required. Install Python, then run scripts\harness.ps1 doctor.'
exit 2
