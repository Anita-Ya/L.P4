Add-Type -AssemblyName System.Drawing

$pristinePath = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612\doctor_recommendation_portrait_1793596701212.jpg"
$orig = [System.Drawing.Bitmap]::FromFile($pristinePath)

# Let's inspect the width and position of the black bottle at each Y from 530 to 710
for ($y = 535; $y -le 710; $y += 10) {
    $minX = 999; $maxX = 0
    for ($x = 450; $x -le 600; $x++) {
        $p = $orig.GetPixel($x, $y)
        # Is it part of the black bottle?
        # The bottle is dark (R < 60, G < 60, B < 60) OR gold text (R > 140, G > 100, B < 80)
        $isBottle = ($p.R -lt 55 -and $p.G -lt 55 -and $p.B -lt 55) -or ($p.R -gt 130 -and $p.G -gt 90 -and $p.B -lt 80)
        # Exclude doctor's coat / shadow if any: doctor coat is white (R>150, G>150, B>150)
        # Skin tone has R > B + 25 and R > 120
        $isSkin = ($p.R -gt 120 -and $p.G -gt 80 -and $p.B -gt 60 -and $p.R -gt $p.B + 20)
        
        if ($isBottle -and -not $isSkin) {
            if ($x -lt $minX) { $minX = $x }
            if ($x -gt $maxX) { $maxX = $x }
        }
    }
    if ($minX -lt 999) {
        Write-Host "Y=$y : Bottle X=$minX..$maxX (Width = $($maxX - $minX))"
    }
}

$orig.Dispose()

