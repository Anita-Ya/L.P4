Add-Type -AssemblyName System.Drawing

$brain = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612"

$crops = @(
    @{
        out = "step1-public-fear.jpg"
        file = "$brain\step1_public_fear_1793437212289.jpg"
        srcX = 320; srcY = 180; size = 460
        gamma = 0.64; bright = 0.18; contrast = 1.20
    },
    @{
        out = "step2-alone-help.jpg"
        file = "$brain\step2_alone_help_1793437238688.jpg"
        srcX = 420; srcY = 270; size = 400
        gamma = 0.68; bright = 0.16; contrast = 1.20
    },
    @{
        out = "step3-career-worry.jpg"
        file = "$brain\card_career_fear_1793435999167.jpg"
        srcX = 270; srcY = 140; size = 440
        gamma = 0.70; bright = 0.14; contrast = 1.18
    },
    @{
        out = "step4-social-hesitation.jpg"
        file = "$brain\step4_social_hesitation_1793437229619.jpg"
        srcX = 130; srcY = 200; size = 440
        gamma = 0.62; bright = 0.20; contrast = 1.20
    },
    @{
        out = "step5-family-concern.jpg"
        file = "$brain\step5_family_concern_1793437249813.jpg"
        srcX = 110; srcY = 270; size = 400
        gamma = 0.68; bright = 0.15; contrast = 1.20
    },
    @{
        out = "step6-future-questions.jpg"
        file = "$brain\card_mental_tension_1793435208262.jpg"
        srcX = 170; srcY = 130; size = 660
        gamma = 0.65; bright = 0.16; contrast = 1.20
    }
)

$outSize = 480
$encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.FormatID -eq [System.Drawing.Imaging.ImageFormat]::Jpeg.Guid }
$encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]95)

foreach ($c in $crops) {
    $src = [System.Drawing.Bitmap]::FromFile($c.file)
    $dest = New-Object System.Drawing.Bitmap($outSize, $outSize)
    $g = [System.Drawing.Graphics]::FromImage($dest)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

    $ia = New-Object System.Drawing.Imaging.ImageAttributes
    $ia.SetGamma($c.gamma, [System.Drawing.Imaging.ColorAdjustType]::Bitmap)

    $cnt = $c.contrast
    $b = $c.bright
    $matrix = New-Object System.Drawing.Imaging.ColorMatrix
    $matrix.Matrix00 = $cnt
    $matrix.Matrix11 = $cnt
    $matrix.Matrix22 = $cnt
    $matrix.Matrix33 = 1.0
    $matrix.Matrix40 = $b
    $matrix.Matrix41 = $b
    $matrix.Matrix42 = $b
    $matrix.Matrix44 = 1.0

    $ia.SetColorMatrix($matrix, [System.Drawing.Imaging.ColorMatrixFlag]::Default, [System.Drawing.Imaging.ColorAdjustType]::Bitmap)

    $destRect = New-Object System.Drawing.Rectangle(0, 0, $outSize, $outSize)
    $g.DrawImage($src, $destRect, $c.srcX, $c.srcY, $c.size, $c.size, [System.Drawing.GraphicsUnit]::Pixel, $ia)

    $targetFile = "c:\Users\Anita Yadav\Desktop\L.P\LP 4\assets\$($c.out)"
    $dest.Save($targetFile, $encoder, $encoderParams)

    $g.Dispose()
    $ia.Dispose()
    $src.Dispose()
    $dest.Dispose()

    Write-Host "Generated: $($c.out)"
}
