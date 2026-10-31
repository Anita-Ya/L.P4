Add-Type -AssemblyName System.Drawing

$brain = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612"

# Let's inspect where the face is in each original 1024x1024 image
# We will define candidate centers (CX, CY) and crop box size (SIZE)
# Then we will test crop, apply circular mask, and save to scratch/preview_*.png

$configs = @(
    @{
        name = "step1"
        file = "$brain\step1_public_fear_1793437212289.jpg"
        # Boy at metro station
        cx = 570
        cy = 380
        size = 520
        gamma = 0.70
        bright = 0.12
        contrast = 1.20
    },
    @{
        name = "step2"
        file = "$brain\step2_alone_help_1793437238688.jpg"
        # Woman sitting alone
        cx = 640
        cy = 500
        size = 460
        gamma = 0.70
        bright = 0.14
        contrast = 1.20
    },
    @{
        name = "step3"
        file = "$brain\card_career_fear_1793435999167.jpg"
        # Man in suit holding head
        cx = 540
        cy = 340
        size = 520
        gamma = 0.70
        bright = 0.12
        contrast = 1.20
    },
    @{
        name = "step4"
        file = "$brain\step4_social_hesitation_1793437229619.jpg"
        # Woman hesitating socially
        cx = 680
        cy = 360
        size = 520
        gamma = 0.70
        bright = 0.12
        contrast = 1.20
    },
    @{
        name = "step5"
        file = "$brain\step5_family_concern_1793437249813.jpg"
        # Family worried
        cx = 440
        cy = 360
        size = 520
        gamma = 0.70
        bright = 0.12
        contrast = 1.20
    },
    @{
        name = "step6"
        file = "$brain\card_mental_tension_1793435208262.jpg"
        # Person anxious / mental tension
        cx = 500
        cy = 400
        size = 520
        gamma = 0.70
        bright = 0.12
        contrast = 1.20
    }
)

foreach ($cfg in $configs) {
    $src = [System.Drawing.Bitmap]::FromFile($cfg.file)

    $half = [int]($cfg.size / 2)
    $srcX = [Math]::Max(0, [Math]::Min($src.Width - $cfg.size, $cfg.cx - $half))
    $srcY = [Math]::Max(0, [Math]::Min($src.Height - $cfg.size, $cfg.cy - $half))

    # Output square image 400x400
    $outSize = 400
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

    # Save square asset
    $encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.FormatID -eq [System.Drawing.Imaging.ImageFormat]::Jpeg.Guid }
    $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
    $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]95)

    $outAsset = "scratch/test_$($cfg.name).jpg"
    $dest.Save($outAsset, $encoder, $encoderParams)

    # Also render circular masked preview to check circle rim clipping!
    $circPreview = New-Object System.Drawing.Bitmap($outSize, $outSize, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $gc = [System.Drawing.Graphics]::FromImage($circPreview)
    $gc.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $gc.Clear([System.Drawing.Color]::Transparent)

    $path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $path.AddEllipse(4, 4, $outSize - 8, $outSize - 8)
    $gc.SetClip($path)
    $gc.DrawImage($dest, 0, 0)
    $gc.ResetClip()

    # Draw border like on webpage
    $borderPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(255, 51, 195, 165), 10)
    $gc.DrawEllipse($borderPen, 5, 5, $outSize - 10, $outSize - 10)

    $circPath = "scratch/circ_test_$($cfg.name).png"
    $circPreview.Save($circPath, [System.Drawing.Imaging.ImageFormat]::Png)

    $borderPen.Dispose()
    $path.Dispose()
    $gc.Dispose()
    $circPreview.Dispose()

    $g.Dispose()
    $ia.Dispose()
    $src.Dispose()
    $dest.Dispose()

    Write-Host "Processed $($cfg.name): crop=($srcX, $srcY, $($cfg.size), $($cfg.size))"
}

