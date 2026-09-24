$ErrorActionPreference = 'Stop'

$codexHome = $env:CODEX_HOME
if (-not $codexHome) { $codexHome = Join-Path $HOME '.codex' }
if ($codexHome -eq '~') { $codexHome = $HOME }
elseif ($codexHome.StartsWith('~/')) { $codexHome = Join-Path $HOME $codexHome.Substring(2) }
$destination = Join-Path $codexHome 'subagent-router'
[System.IO.Directory]::CreateDirectory($destination) | Out-Null

foreach ($profile in Get-ChildItem -LiteralPath (Join-Path $PSScriptRoot '../routing') -Filter 'astra-*.json' -File) {
    $target = Join-Path $destination $profile.Name
    if (Test-Path -LiteralPath $target) { continue }
    # File.Copy refuses to overwrite a file created by another session meanwhile.
    [System.IO.File]::Copy($profile.FullName, $target, $false)
}
