Add-Type -AssemblyName System.Drawing

$pristinePath = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612\doctor_recommendation_portrait_1793596701212.jpg"
$orig = [System.Drawing.Bitmap]::FromFile($pristinePath)

# Check all pixels in the hand region Y=525..720, X=440..610
# Identify what is at each coordinate
for ($y = 525; $y -le 720; $y += 5) {
    for ($x = 440; $x -le 610; $x += 5) {
        $p = $orig.GetPixel($x, $y)
        # Check if outside X=478..582 but dark (R < 55, G < 55, B < 55)
        if (($x -lt 478 -or $x -gt 582) -and ($p.R -lt 55 -and $p.G -lt 55 -and $p.B -lt 55)) {
            Write-Host "Dark pixel outside bottle rect: X=$x, Y=$y (R=$($p.R), G=$($p.G), B=$($p.B))"
        }
    }
}

$orig.Dispose()

