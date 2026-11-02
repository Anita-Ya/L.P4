Add-Type -AssemblyName System.Drawing

$origPath = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612\doctor_recommendation_portrait_1793596701212.jpg"
$orig = [System.Drawing.Bitmap]::FromFile($origPath)

# Let's sample a grid in X=420..580, Y=480..720
# Find dark pixels (bottle cap and body) vs skin pixels vs white coat
$minX = 1200; $maxX = 0; $minY = 896; $maxY = 0

for ($y = 480; $y -le 720; $y += 2) {
    for ($x = 420; $x -le 580; $x += 2) {
        $p = $orig.GetPixel($x, $y)
        # Check if very dark (black bottle body or cap): R, G, B all < 55
        if ($p.R -lt 55 -and $p.G -lt 55 -and $p.B -lt 55) {
            if ($x -lt $minX) { $minX = $x }
            if ($x -gt $maxX) { $maxX = $x }
            if ($y -lt $minY) { $minY = $y }
            if ($y -gt $maxY) { $maxY = $y }
        }
    }
}

Write-Host "Dark bottle bounding box roughly: X=$minX..$maxX (W=$($maxX-$minX)), Y=$minY..$maxY (H=$($maxY-$minY))"

# Let's also check where the gold text "AYURVEDIC VITALITY" was:
# Yellow/gold pixels: R > 150, G > 120, B < 80
$goldMinX = 1200; $goldMaxX = 0; $goldMinY = 896; $goldMaxY = 0
for ($y = 520; $y -le 700; $y += 2) {
    for ($x = 420; $x -le 580; $x += 2) {
        $p = $orig.GetPixel($x, $y)
        if ($p.R -gt 150 -and $p.G -gt 120 -and $p.B -lt 80) {
            if ($x -lt $goldMinX) { $goldMinX = $x }
            if ($x -gt $goldMaxX) { $goldMaxX = $x }
            if ($y -lt $goldMinY) { $goldMinY = $y }
            if ($y -gt $goldMaxY) { $goldMaxY = $y }
        }
    }
}

Write-Host "Gold text on bottle: X=$goldMinX..$goldMaxX, Y=$goldMinY..$goldMaxY"

$orig.Dispose()

