Add-Type -AssemblyName System.Drawing

$brain = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612"

$configs = @(
    @{
        outName = "step1-public-fear.jpg"
        file = "$brain\step1_public_fear_1793437212289.jpg"
        cx = 575
        cy = 420
        size = 500
        gamma = 0.70
        bright = 0.14
        contrast = 1.20
    },
    @{
        outName = "step2-alone-help.jpg"
        file = "$brain\step2_alone_help_1793437238688.jpg"
        cx = 645
        cy = 575
        size = 460
        gamma = 0.70
        bright = 0.15
        contrast = 1.22
    },
    @{
        outName = "step3-career-worry.jpg"
        file = "$brain\card_career_fear_1793435999167.jpg"
        cx = 510
        cy = 285
        size = 500
        gamma = 0.70
        bright = 0.14
        contrast = 1.20
    },
    @{
        outName = "step4-social-hesitation.jpg"
        file = "$brain\step4_social_hesitation_1793437229619.jpg"
        cx = 705
        cy = 360
        size = 500
        gamma = 0.70
        bright = 0.14
        contrast = 1.20
    },
    @{
        outName = "step5-family-concern.jpg"
        file = "$brain\step5_family_concern_1793437249813.jpg"
        cx = 430
        cy = 365
        size = 520
        gamma = 0.70
        bright = 0.14
        contrast = 1.20
    },
    @{
        outName = "step6-future-questions.jpg"
        file = "$brain\card_mental_tension_1793435208262.jpg"
        cx = 505
        cy = 405
        size = 500
        gamma = 0.70
        bright = 0.14
        contrast = 1.20
    }
)

foreach ($cfg in $configs) {
    $src = [System.Drawing.Bitmap]::FromFile($cfg.file)

    $half = [int]($cfg.size / 2)
    $srcX = [Math]::Max(0, [Math]::Min($src.Width - $cfg.size, $cfg.cx - $half))
    $srcY = [Math]::Max(0, [Math]::Min($src.Height - $cfg.size, $cfg.cy - $half))

    # Output square image 480x480 (crisp retina on 112px display)
    $outSize = 480
    $dest = New-Object System.Drawing.Bitmap($outSize, $outSize)
    $g = [System.Drawing.Graphics]::FromImage($dest)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

    $ia = New-Object System.Drawing.Imaging.ImageAttributes
    $ia.SetGamma($cfg.gamma, [System.Drawing.Imaging.ColorAdjustType]::Bitmap)

    $c = $cfg.contrast
    $b = $cfg.bright
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

    $destRect = New-Object System.Drawing.Rectangle(0, 0, $outSize, $outSize)
    $g.DrawImage($src, $destRect, $srcX, $srcY, $cfg.size, $cfg.size, [System.Drawing.GraphicsUnit]::Pixel, $ia)

    # Save asset
    $encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.FormatID -eq [System.Drawing.Imaging.ImageFormat]::Jpeg.Guid }
    $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
    $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]95)

    $targetFile = "c:\Users\Anita Yadav\Desktop\L.P\LP 4\assets\$($cfg.outName)"
    $dest.Save($targetFile, $encoder, $encoderParams)

    $g.Dispose()
    $ia.Dispose()
    $src.Dispose()
    $dest.Dispose()

    Write-Host "Generated: $targetFile (size=$($cfg.size), srcX=$srcX, srcY=$srcY)"
}
