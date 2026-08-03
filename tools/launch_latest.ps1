param(
    [string] $ProjectPath = "C:\Users\Lenovo\Documents\Codex\2026-07-21\fullstack-ren-py-github-cli-gh",
    [string] $RenpyPath = "C:\Users\Lenovo\Documents\Downloads\renpy-8.5.3-sdk\renpy.exe",
    [switch] $NoStop
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $ProjectPath -PathType Container)) {
    throw "Project path does not exist: $ProjectPath"
}

if (-not (Test-Path -LiteralPath $RenpyPath -PathType Leaf)) {
    throw "Ren'Py executable does not exist: $RenpyPath"
}

$branch = (& git -C $ProjectPath branch --show-current).Trim()
if ($branch -ne "main") {
    throw "Latest playtests should launch from the canonical main checkout. '$ProjectPath' is on '$branch'."
}

$dirty = (& git -C $ProjectPath status --porcelain)
if ($dirty) {
    throw "Project checkout has local changes. Commit, stash, or discard them before pulling latest main."
}

& git -C $ProjectPath fetch origin main
& git -C $ProjectPath pull --ff-only origin main

$commit = (& git -C $ProjectPath rev-parse --short HEAD).Trim()
$subject = (& git -C $ProjectPath log -1 --pretty=%s).Trim()

if (-not $NoStop) {
    Get-Process renpy -ErrorAction SilentlyContinue |
        Where-Object { $_.MainWindowTitle -eq "Duck Memes Ren'Py Quiz" } |
        Stop-Process

    Start-Sleep -Seconds 1
}

$process = Start-Process -FilePath $RenpyPath -ArgumentList @($ProjectPath) -PassThru
Start-Sleep -Seconds 2

$shell = New-Object -ComObject WScript.Shell
$null = $shell.AppActivate($process.Id)

Write-Host "Launched Duck Memes Ren'Py Quiz"
Write-Host "Project: $ProjectPath"
Write-Host "Commit: $commit $subject"
Write-Host "ProcessId: $($process.Id)"
