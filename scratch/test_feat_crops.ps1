Add-Type -AssemblyName System.Drawing

$configs = @(
    @{
        name = "feat1_ap"
        file = "Ap.jpg"
        srcX = 130
        srcY = 0
        size = 338
    },
    @{
        name = "feat2_hc"
        file = "hc.jpg"
        srcX = 90
        srcY = 0
        size = 360
    },
    @{
        name = "feat3_qa"
        file = "QA.jpg"
        srcX = 91
        srcY = 0
        size = 365
    },
    @{
        name = "feat4_dr"
        file = "DR.jpg"
        srcX = 0
        srcY = 0
        size = 447
    }
)

$outW = 4 * 140
$outH = 150
$composite = New-Object System.Drawing.Bitmap($outW, $outH, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
$gc = [System.Drawing.Graphics]::FromImage($composite)
$gc.Clear([System.Drawing.Color]::White)
$gc.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias

$borderPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(255, 51, 195, 165), 4)

for ($i = 0; $i -lt $configs.Count; $i++) {
    $cfg = $configs[$i]
    $src = [System.Drawing.Bitmap]::FromFile($cfg.file)

    $d = 100
    $destSquare = New-Object System.Drawing.Bitmap($d, $d)
    $g = [System.Drawing.Graphics]::FromImage($destSquare)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

    $destRect = New-Object System.Drawing.Rectangle(0, 0, $d, $d)
    $g.DrawImage($src, $destRect, $cfg.srcX, $cfg.srcY, $cfg.size, $cfg.size, [System.Drawing.GraphicsUnit]::Pixel)

    $xOffset = $i * 140 + 20
    $yOffset = 20

    $path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $path.AddEllipse($xOffset, $yOffset, $d, $d)
    $gc.SetClip($path)
    $gc.DrawImage($destSquare, $xOffset, $yOffset, $d, $d)
    $gc.ResetClip()

    $gc.DrawEllipse($borderPen, $xOffset, $yOffset, $d, $d)

    $path.Dispose()
    $g.Dispose()
    $destSquare.Dispose()
    $src.Dispose()
}

$borderPen.Dispose()
$gc.Dispose()

$composite.Save("scratch/feat_circles_test.png", [System.Drawing.Imaging.ImageFormat]::Png)
$composite.Dispose()
Write-Host "Saved scratch/feat_circles_test.png"

