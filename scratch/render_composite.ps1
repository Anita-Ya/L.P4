Add-Type -AssemblyName System.Drawing

$assets = @(
    "step1-public-fear.jpg",
    "step2-alone-help.jpg",
    "step3-career-worry.jpg",
    "step4-social-hesitation.jpg",
    "step5-family-concern.jpg",
    "step6-future-questions.jpg"
)

$outW = 6 * 140
$outH = 160
$composite = New-Object System.Drawing.Bitmap($outW, $outH, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
$gc = [System.Drawing.Graphics]::FromImage($composite)
$gc.Clear([System.Drawing.Color]::White)
$gc.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias

$borderPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(255, 51, 195, 165), 4)
$font = New-Object System.Drawing.Font("Arial", 11, [System.Drawing.FontStyle]::Bold)
$brush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(255, 11, 60, 93))

for ($i = 0; $i -lt $assets.Count; $i++) {
    $file = "c:\Users\Anita Yadav\Desktop\L.P\LP 4\assets\$($assets[$i])"
    $bmp = [System.Drawing.Bitmap]::FromFile($file)

    $xOffset = $i * 140 + 15
    $yOffset = 20
    $d = 112

    # Draw circular masked image
    $path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $path.AddEllipse($xOffset, $yOffset, $d, $d)
    $gc.SetClip($path)
    $gc.DrawImage($bmp, $xOffset, $yOffset, $d, $d)
    $gc.ResetClip()

    # Draw mint border
    $gc.DrawEllipse($borderPen, $xOffset, $yOffset, $d, $d)

    # Label
    $gc.DrawString("0$($i+1)", $font, $brush, [float]($xOffset + 45), [float]($yOffset + $d + 6))

    $path.Dispose()
    $bmp.Dispose()
}

$borderPen.Dispose()
$font.Dispose()
$brush.Dispose()
$gc.Dispose()

$destPath = "c:\Users\Anita Yadav\Desktop\L.P\LP 4\scratch\all_circles_composite.png"
$composite.Save($destPath, [System.Drawing.Imaging.ImageFormat]::Png)
$composite.Dispose()
Write-Host "Saved composite to $destPath"

