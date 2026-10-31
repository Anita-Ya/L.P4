Add-Type -AssemblyName System.Drawing

$src = [System.Drawing.Bitmap]::FromFile("c:\Users\Anita Yadav\Desktop\L.P\LP 4\scratch\section2_screenshot.png")
Write-Host "Screenshot size: $($src.Width) x $($src.Height)"

# Crop Section 2 (approx y=700 to 1800)
$cropY = 700
$cropH = [Math]::Min(1100, $src.Height - $cropY)
$dest = New-Object System.Drawing.Bitmap($src.Width, $cropH)
$g = [System.Drawing.Graphics]::FromImage($dest)
$g.DrawImage($src, 0, 0, (New-Object System.Drawing.Rectangle(0, $cropY, $src.Width, $cropH)), [System.Drawing.GraphicsUnit]::Pixel)
$g.Dispose()

$dest.Save("c:\Users\Anita Yadav\Desktop\L.P\LP 4\scratch\section2_crop.png", [System.Drawing.Imaging.ImageFormat]::Png)
$dest.Dispose()
$src.Dispose()
Write-Host "Saved section2_crop.png"

