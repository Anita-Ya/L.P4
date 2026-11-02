Add-Type -AssemblyName System.Drawing

$pristinePath = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612\doctor_recommendation_portrait_1793596701212.jpg"
$botPath = "$PWD\assets\real-bottle-clean-hd.png"

$orig = [System.Drawing.Bitmap]::FromFile($pristinePath)
$bot = [System.Drawing.Bitmap]::FromFile($botPath)

$comp = New-Object System.Drawing.Bitmap($orig)
$g = [System.Drawing.Graphics]::FromImage($comp)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

# Exact bottle placement over the black bottle:
# Original bottle was: left=478, right=560 (W=82), capTop=533, bottom=715 (H=182)
# Let's cover X=476, Y=532, W=86, H=184
$x = 476
$y = 532
$w = 86
$h = 184

$destRect = New-Object System.Drawing.Rectangle($x, $y, $w, $h)
$g.DrawImage($bot, $destRect)
$g.Dispose()

# Restore fingers naturally:
# Doctor's right hand fingers holding left side of bottle (X=460..485, Y=570..695)
for ($py = 570; $py -le 695; $py++) {
    for ($px = 460; $px -le 488; $px++) {
        $p = $orig.GetPixel($px, $py)
        # Skin tone condition
        if ($p.R -gt 130 -and $p.G -gt 85 -and $p.B -gt 65 -and $p.R -gt $p.B + 15) {
            $comp.SetPixel($px, $py, $p)
        }
    }
}

# Doctor's left hand fingers supporting bottom of bottle (X=500..570, Y=690..730)
for ($py = 690; $py -le 730; $py++) {
    for ($px = 500; $px -le 570; $px++) {
        $p = $orig.GetPixel($px, $py)
        if ($p.R -gt 130 -and $p.G -gt 85 -and $p.B -gt 65 -and $p.R -gt $p.B + 15) {
            $comp.SetPixel($px, $py, $p)
        }
    }
}

# Save zoom of hands
$zoomRect = New-Object System.Drawing.Rectangle(430, 500, 180, 240)
$zoom = $comp.Clone($zoomRect, $comp.PixelFormat)
$zoom.Save("$PWD\scratch\perfect_single_bottle_zoom.jpg", [System.Drawing.Imaging.ImageFormat]::Jpeg)
$zoom.Dispose()

# Save final composite
$comp.Save("$PWD\scratch\doctor_recommendation_clean.jpg", [System.Drawing.Imaging.ImageFormat]::Jpeg)

$comp.Dispose()
$orig.Dispose()
$bot.Dispose()

Write-Host "Created scratch\perfect_single_bottle_zoom.jpg and doctor_recommendation_clean.jpg"

