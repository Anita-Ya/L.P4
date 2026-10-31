Add-Type -AssemblyName System.Drawing

$configs = @(
    @{
        outName = "feat-01-ayurvedic-hd.jpg"
        file = "Ap.jpg"
        srcX = 50
        srcY = 0
        size = 338
    },
    @{
        outName = "feat-02-herbal-hd.jpg"
        file = "hc.jpg"
        srcX = 90
        srcY = 0
        size = 360
    },
    @{
        outName = "feat-03-quality-hd.jpg"
        file = "QA.jpg"
        srcX = 91
        srcY = 0
        size = 365
    },
    @{
        outName = "feat-04-routine-hd.jpg"
        file = "DR.jpg"
        srcX = 0
        srcY = 0
        size = 447
    }
)

$outSize = 400
$encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.FormatID -eq [System.Drawing.Imaging.ImageFormat]::Jpeg.Guid }
$encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]95)

foreach ($cfg in $configs) {
    $src = [System.Drawing.Bitmap]::FromFile($cfg.file)
    $dest = New-Object System.Drawing.Bitmap($outSize, $outSize)
    $g = [System.Drawing.Graphics]::FromImage($dest)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

    $destRect = New-Object System.Drawing.Rectangle(0, 0, $outSize, $outSize)
    $g.DrawImage($src, $destRect, $cfg.srcX, $cfg.srcY, $cfg.size, $cfg.size, [System.Drawing.GraphicsUnit]::Pixel)

    $targetPath = "assets\$($cfg.outName)"
    $dest.Save($targetPath, $encoder, $encoderParams)

    $g.Dispose()
    $dest.Dispose()
    $src.Dispose()

    Write-Host "Generated: $targetPath"
}

