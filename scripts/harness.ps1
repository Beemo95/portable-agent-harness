# Portable PowerShell wrapper; prefers Windows Python launcher.
$entry = Join-Path $PSScriptRoot 'harness.py'
if (Get-Command py -ErrorAction SilentlyContinue) {
  & py -3 $entry @args
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
  & python $entry @args
} else {
  Write-Error 'Python >=3.10 is required; install Python then retry.'
  exit 127
}
exit $LASTEXITCODE
