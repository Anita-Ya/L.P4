Add-Type -AssemblyName System.Drawing

$files = @("Ap.jpg", "hc.jpg", "QA.jpg", "DR.jpg")

foreach ($f in $files) {
    if (Test-Path $f) {
        $bmp = [System.Drawing.Bitmap]::FromFile($f)
        Write-Host "$f : $($bmp.Width) x $($bmp.Height)"
        $bmp.Dispose()
    }
}

