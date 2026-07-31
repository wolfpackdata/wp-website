<#
  Renders every artboard in templates/export/ to a 300 DPI PNG in preview/.

  Why 3.125: CSS defines 1in as exactly 96px, so a device-scale-factor of
  3.125 makes 1 CSS inch = 300 device pixels. The PNG then drops into Word at
  100% scale with no resampling — 7.5in wide, which is exactly the Letter
  text column at 0.5in side margins.

  Usage:  powershell -ExecutionPolicy Bypass -File .\export-png.ps1
#>

$ErrorActionPreference = 'Stop'
$here    = Split-Path -Parent $MyInvocation.MyCommand.Path
$srcDir  = Join-Path $here 'export'
$outDir  = Join-Path (Split-Path -Parent $here) 'preview'
$scale   = 3.125

if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Force $outDir | Out-Null }

$browser = @(
  "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
  "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
  "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
  "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1

if (-not $browser) { throw "No Edge or Chrome found. Install one, or open the artboards and screenshot by hand." }

# width x height in CSS px, matching body.artboard--* in css/resume-brand.css
$sizes = @{
  'header-dark-music'          = @(720, 128)
  'header-dark-eng'            = @(720, 128)
  'header-light-music'         = @(720, 128)
  'header-light-eng'           = @(720, 128)
  'header-compact-dark-music'  = @(720, 96)
  'header-compact-dark-eng'    = @(720, 96)
  'header-compact-light-music' = @(720, 96)
  'header-compact-light-eng'   = @(720, 96)
  'footer-dark'                = @(720, 26)
  'footer-light'               = @(720, 26)
  # Letter-page proofs — review artefacts, not assets to paste into Word.
  'page-proof-dark-eng'        = @(816, 1056)
  'page-proof-light-music'     = @(816, 1056)
}

foreach ($name in $sizes.Keys | Sort-Object) {
  $src = Join-Path $srcDir "$name.html"
  if (-not (Test-Path $src)) { Write-Warning "missing $src"; continue }
  $out = Join-Path $outDir "$name.png"
  $w, $h = $sizes[$name]
  $tmpProfile = Join-Path $env:TEMP ("resume-artboard-" + [guid]::NewGuid().ToString('N'))
  # Edge writes its "N bytes written" note to stderr; don't redirect it inside
  # PowerShell 5.1 or every run looks like a failure. Start-Process swallows it.
  $argList = @(
    '--headless=new', '--disable-gpu', '--hide-scrollbars',
    "--user-data-dir=$tmpProfile",
    "--force-device-scale-factor=$scale",
    "--window-size=$w,$h",
    "--screenshot=$out",
    "file:///$($src -replace '\\','/')"
  )
  Start-Process -FilePath $browser -ArgumentList $argList -NoNewWindow -Wait
  try { Remove-Item -Recurse -Force $tmpProfile -ErrorAction Stop } catch {}
  if (Test-Path $out) {
    Add-Type -AssemblyName System.Drawing
    $img = [System.Drawing.Image]::FromFile($out)
    Write-Output ("{0,-20} {1} x {2} px  ({3:N2} x {4:N2} in @ 300 DPI)" -f $name, $img.Width, $img.Height, ($img.Width/300), ($img.Height/300))
    $img.Dispose()
  } else {
    Write-Warning "$name did not render"
  }
}
