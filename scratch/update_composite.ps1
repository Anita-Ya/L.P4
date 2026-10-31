Add-Type -AssemblyName System.Drawing

$files = @("assets\feat-01-ayurvedic-hd.jpg", "assets\feat-02-herbal-hd.jpg", "assets\feat-03-quality-hd.jpg", "assets\feat-04-routine-hd.jpg")

$outW = 4 * 140
$outH = 150
$composite = New-Object System.Drawing.Bitmap($outW, $outH, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
$gc = [System.Drawing.Graphics]::FromImage($composite)
$gc.Clear([System.Drawing.Color]::White)
$gc.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias

$borderPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(255, 51, 195, 165), 4)

for ($i = 0; $i -lt $files.Count; $i++) {
    $src = [System.Drawing.Bitmap]::FromFile($files[$i])
    $d = 100
    $xOffset = $i * 140 + 20
    $yOffset = 20

    $path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $path.AddEllipse($xOffset, $yOffset, $d, $d)
    $gc.SetClip($path)
    $gc.DrawImage($src, $xOffset, $yOffset, $d, $d)
    $gc.ResetClip()

    $gc.DrawEllipse($borderPen, $xOffset, $yOffset, $d, $d)

    $path.Dispose()
    $src.Dispose()
}

$borderPen.Dispose()
$gc.Dispose()

$composite.Save("scratch/feat_circles_test.png", [System.Drawing.Imaging.ImageFormat]::Png)
$composite.Dispose()
Write-Host "Updated scratch/feat_circles_test.png"

