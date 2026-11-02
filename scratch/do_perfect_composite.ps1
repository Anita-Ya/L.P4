Add-Type -AssemblyName System.Drawing

$pristinePath = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612\doctor_recommendation_portrait_1793596701212.jpg"
$tightBotPath = "$PWD\scratch\tight_bottle.png"

$orig = [System.Drawing.Bitmap]::FromFile($pristinePath)
$tightBot = [System.Drawing.Bitmap]::FromFile($tightBotPath)

$comp = New-Object System.Drawing.Bitmap($orig)
$g = [System.Drawing.Graphics]::FromImage($comp)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

# 1. First, check the right seam (X=575..595, Y=550..690) where doctor's coat is:
# Any stray black bottle edge in original should be clean white coat:
for ($y = 550; $y -le 690; $y++) {
    for ($x = 575; $x -le 590; $x++) {
        $p = $orig.GetPixel($x, $y)
        # If it was part of the black bottle shadow or body (dark) and not skin
        if ($p.R -lt 70 -and $p.G -lt 70 -and $p.B -lt 70) {
            # Pick the coat color from X=588
            $coat = $orig.GetPixel(588, $y)
            $comp.SetPixel($x, $y, $coat)
        }
    }
}

# 2. Draw tight Mirgi Mukti bottle:
# Covers X=478 to 580 (W=102), Y=530 to 712 (H=182)
$x = 478
$y = 530
$w = 102
$h = 182

$destRect = New-Object System.Drawing.Rectangle($x, $y, $w, $h)
$g.DrawImage($tightBot, $destRect)
$g.Dispose()

# 3. Restore doctor's gripping fingers on the left side:
for ($py = 570; $py -le 695; $py++) {
    for ($px = 450; $px -le 488; $px++) {
        $p = $orig.GetPixel($px, $py)
        if ($p.R -gt 130 -and $p.G -gt 85 -and $p.B -gt 65 -and $p.R -gt $p.B + 18) {
            $comp.SetPixel($px, $py, $p)
        }
    }
}

# 4. Restore doctor's supporting fingers on the bottom right:
for ($py = 692; $py -le 730; $py++) {
    for ($px = 490; $px -le 575; $px++) {
        $p = $orig.GetPixel($px, $py)
        if ($p.R -gt 130 -and $p.G -gt 85 -and $p.B -gt 65 -and $p.R -gt $p.B + 18) {
            $comp.SetPixel($px, $py, $p)
        }
    }
}

# 5. Save detailed zoom for verification
$zoomRect = New-Object System.Drawing.Rectangle(430, 500, 190, 240)
$zoom = $comp.Clone($zoomRect, $comp.PixelFormat)
$zoom.Save("$PWD\scratch\perfect_single_tight_zoom.jpg", [System.Drawing.Imaging.ImageFormat]::Jpeg)
$zoom.Dispose()

# 6. Save full composited doctor recommendation image
$comp.Save("$PWD\scratch\doctor_recommendation_perfect.jpg", [System.Drawing.Imaging.ImageFormat]::Jpeg)

$comp.Dispose()
$tightBot.Dispose()
$orig.Dispose()

Write-Host "Compositing complete! Saved scratch\perfect_single_tight_zoom.jpg"

