Add-Type -AssemblyName System.Drawing

$comp = [System.Drawing.Bitmap]::FromFile("$PWD\scratch\doctor_recommendation_clean.jpg")

# Check if there are any gold pixels (original AYURVEDIC VITALITY text)
# Earlier we found: Gold text on bottle: X=500..530, Y=618..630
$goldFound = $false
for ($y = 615; $y -le 635; $y++) {
    for ($x = 495; $x -le 535; $x++) {
        $p = $comp.GetPixel($x, $y)
        # Gold text was R > 150, G > 120, B < 80
        # The Mirgi Mukti label here has white/green text (R > 180, G > 180, B > 180 or G > R)
        if ($p.R -gt 150 -and $p.G -gt 120 -and $p.B -lt 80 -and $p.R -gt $p.B + 70) {
            $goldFound = $true
        }
    }
}

Write-Host "Old gold text found: $goldFound"

# Check table area X=180..220, Y=550..650 (where the extra bottle was previously)
$tableP = $comp.GetPixel(197, 566)
Write-Host "Table pixel at 197, 566: R=$($tableP.R), G=$($tableP.G), B=$($tableP.B)"

$comp.Dispose()

