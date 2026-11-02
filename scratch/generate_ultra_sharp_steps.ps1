Add-Type -AssemblyName System.Drawing

$brain = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612"

$configs = @(
    @{
        outName = "step1-public-fear.jpg"
        file = "$brain\step1_public_fear_1793437212289.jpg"
        cx = 575
        cy = 430
        cropSize = 650
    },
    @{
        outName = "step2-alone-help.jpg"
        file = "$brain\step2_alone_help_1793437238688.jpg"
        cx = 640
        cy = 560
        cropSize = 650
    },
    @{
        outName = "step3-career-worry.jpg"
        file = "$brain\card_career_fear_1793435999167.jpg"
        cx = 510
        cy = 300
        cropSize = 650
    },
    @{
        outName = "step4-social-hesitation.jpg"
        file = "$brain\step4_social_hesitation_1793437229619.jpg"
        cx = 700
        cy = 380
        cropSize = 650
    },
    @{
        outName = "step5-family-concern.jpg"
        file = "$brain\step5_family_concern_1793437249813.jpg"
        cx = 450
        cy = 380
        cropSize = 650
    },
    @{
        outName = "step6-future-questions.jpg"
        file = "$brain\card_mental_tension_1793435208262.jpg"
        cx = 510
        cy = 410
        cropSize = 650
    }
)

foreach ($cfg in $configs) {
    $src = [System.Drawing.Bitmap]::FromFile($cfg.file)

    $half = [int]($cfg.cropSize / 2)
    $srcX = [Math]::Max(0, [Math]::Min($src.Width - $cfg.cropSize, $cfg.cx - $half))
    $srcY = [Math]::Max(0, [Math]::Min($src.Height - $cfg.cropSize, $cfg.cy - $half))

    # Output high-res 800x800 (Crystal sharp on retina mobile screens)
    $outSize = 800
    $dest = New-Object System.Drawing.Bitmap($outSize, $outSize)
    $g = [System.Drawing.Graphics]::FromImage($dest)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
    $g.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality

    # Render clean image directly with NO washing-out gamma or haze:
    $destRect = New-Object System.Drawing.Rectangle(0, 0, $outSize, $outSize)
    $g.DrawImage($src, $destRect, $srcX, $srcY, $cfg.cropSize, $cfg.cropSize, [System.Drawing.GraphicsUnit]::Pixel)

    # Save with maximum quality (98)
    $encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.FormatID -eq [System.Drawing.Imaging.ImageFormat]::Jpeg.Guid }
    $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
    $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]98)

    $targetFile = "c:\Users\Anita Yadav\Desktop\L.P\LP 4\assets\$($cfg.outName)"
    $dest.Save($targetFile, $encoder, $encoderParams)

    $g.Dispose()
    $src.Dispose()
    $dest.Dispose()

    Write-Host "Generated Ultra-Sharp HD: $targetFile (size=$($cfg.cropSize), outSize=800x800)"
}

