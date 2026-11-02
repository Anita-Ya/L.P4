Add-Type -AssemblyName System.Drawing

$origPath = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612\doctor_recommendation_portrait_1793596701212.jpg"
$orig = [System.Drawing.Bitmap]::FromFile($origPath)

# Let's inspect the exact bottle area
# The bottle cap top is around Y=530..570
# Let's find cap top: scan X=480..540, Y=500..600 for dark pixels
$capTopY = 999
for ($y = 500; $y -le 600; $y++) {
    for ($x = 480; $x -le 540; $x++) {
        $p = $orig.GetPixel($x, $y)
        if ($p.R -lt 50 -and $p.G -lt 50 -and $p.B -lt 50) {
            if ($y -lt $capTopY) { $capTopY = $y }
        }
    }
}

Write-Host "Cap top Y: $capTopY"

# Let's find bottle left and right boundaries across Y=580..660
# Where the bottle is held between fingers
# Left hand (doctor's right hand): thumb or fingers holding left side of bottle
# Right hand (doctor's left hand): fingers supporting bottom / right side of bottle

$botLeft = 999; $botRight = 0
for ($y = 570; $y -le 680; $y += 5) {
    for ($x = 450; $x -le 560; $x++) {
        $p = $orig.GetPixel($x, $y)
        if ($p.R -lt 40 -and $p.G -lt 40 -and $p.B -lt 40) {
            if ($x -lt $botLeft) { $botLeft = $x }
            if ($x -gt $botRight) { $botRight = $x }
        }
    }
}

Write-Host "Bottle left: $botLeft, right: $botRight, Width: $($botRight - $botLeft)"

$orig.Dispose()

