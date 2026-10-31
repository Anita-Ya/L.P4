Add-Type -AssemblyName System.Drawing

function Enhance-Image {
    param (
        [string]$inputPath,
        [string]$outputPath,
        [float]$brightness = 0.25,   # +25% brightness
        [float]$contrast = 1.25,     # +25% contrast
        [float]$gamma = 0.75         # gamma < 1 brightens shadows
    )

    $src = [System.Drawing.Bitmap]::FromFile($inputPath)
    $dest = New-Object System.Drawing.Bitmap($src.Width, $src.Height)
    $g = [System.Drawing.Graphics]::FromImage($dest)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

    $ia = New-Object System.Drawing.Imaging.ImageAttributes
    $ia.SetGamma($gamma, [System.Drawing.Imaging.ColorAdjustType]::Bitmap)

    # ColorMatrix for brightness and contrast
    # contrast c, brightness b: scale RGB by c, add b
    $c = $contrast
    $b = $brightness
    $matrix = New-Object System.Drawing.Imaging.ColorMatrix
    $matrix.Matrix00 = $c
    $matrix.Matrix11 = $c
    $matrix.Matrix22 = $c
    $matrix.Matrix33 = 1.0
    $matrix.Matrix40 = $b
    $matrix.Matrix41 = $b
    $matrix.Matrix42 = $b
    $matrix.Matrix44 = 1.0

    $ia.SetColorMatrix($matrix, [System.Drawing.Imaging.ColorMatrixFlag]::Default, [System.Drawing.Imaging.ColorAdjustType]::Bitmap)

    $rect = New-Object System.Drawing.Rectangle(0, 0, $src.Width, $src.Height)
    $g.DrawImage($src, $rect, 0, 0, $src.Width, $src.Height, [System.Drawing.GraphicsUnit]::Pixel, $ia)

    $g.Dispose()
    $ia.Dispose()
    $src.Dispose()

    # Save with high quality JPEG
    $encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.FormatID -eq [System.Drawing.Imaging.ImageFormat]::Jpeg.Guid }
    $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
    $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]95)

    $dest.Save($outputPath, $encoder, $encoderParams)
    $dest.Dispose()
    Write-Host "Enhanced: $outputPath"
}

# Test on family-shock-distress
Enhance-Image -inputPath "assets/family-shock-distress.jpg" -outputPath "assets/family-shock-bright.jpg" -brightness 0.18 -contrast 1.15 -gamma 0.70
Write-Host "Done!"

