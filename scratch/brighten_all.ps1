Add-Type -AssemblyName System.Drawing

function Enhance-Photo {
    param (
        [string]$filePath,
        [float]$gamma = 0.55,
        [float]$brightness = 0.16,
        [float]$contrast = 1.15
    )

    if (-not (Test-Path $filePath)) {
        Write-Host "File not found: $filePath"
        return
    }

    $tempPath = $filePath + ".tmp.jpg"
    $src = [System.Drawing.Bitmap]::FromFile($filePath)
    $dest = New-Object System.Drawing.Bitmap($src.Width, $src.Height)
    $g = [System.Drawing.Graphics]::FromImage($dest)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

    $ia = New-Object System.Drawing.Imaging.ImageAttributes
    $ia.SetGamma($gamma, [System.Drawing.Imaging.ColorAdjustType]::Bitmap)

    $matrix = New-Object System.Drawing.Imaging.ColorMatrix
    $matrix.Matrix00 = $contrast
    $matrix.Matrix11 = $contrast
    $matrix.Matrix22 = $contrast
    $matrix.Matrix33 = 1.0
    $matrix.Matrix40 = $brightness
    $matrix.Matrix41 = $brightness
    $matrix.Matrix42 = $brightness
    $matrix.Matrix44 = 1.0

    $ia.SetColorMatrix($matrix, [System.Drawing.Imaging.ColorMatrixFlag]::Default, [System.Drawing.Imaging.ColorAdjustType]::Bitmap)

    $rect = New-Object System.Drawing.Rectangle(0, 0, $src.Width, $src.Height)
    $g.DrawImage($src, $rect, 0, 0, $src.Width, $src.Height, [System.Drawing.GraphicsUnit]::Pixel, $ia)

    $g.Dispose()
    $ia.Dispose()
    $src.Dispose()

    $encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.FormatID -eq [System.Drawing.Imaging.ImageFormat]::Jpeg.Guid }
    $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
    $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]95)

    $dest.Save($tempPath, $encoder, $encoderParams)
    $dest.Dispose()

    Remove-Item $filePath -Force
    Move-Item $tempPath $filePath -Force
    Write-Host "Brightened & Enhanced: $filePath"
}

# Section 2 Problem Circle Images - Give strong daylight boost
Enhance-Photo -filePath "assets/step1-public-fear.jpg" -gamma 0.52 -brightness 0.18 -contrast 1.15
Enhance-Photo -filePath "assets/step2-alone-help.jpg" -gamma 0.45 -brightness 0.24 -contrast 1.18
Enhance-Photo -filePath "assets/step3-career-worry.jpg" -gamma 0.52 -brightness 0.18 -contrast 1.15
Enhance-Photo -filePath "assets/step4-social-hesitation.jpg" -gamma 0.46 -brightness 0.22 -contrast 1.18
Enhance-Photo -filePath "assets/step5-family-concern.jpg" -gamma 0.52 -brightness 0.18 -contrast 1.15
Enhance-Photo -filePath "assets/step6-future-questions.jpg" -gamma 0.50 -brightness 0.20 -contrast 1.15

Write-Host "Section 2 photos enhanced with daylight clarity!"
