Add-Type -AssemblyName System.Drawing

$comp = [System.Drawing.Bitmap]::FromFile("$PWD\scratch\doctor_recommendation_perfect.jpg")

$darkFound = 0
for ($y = 550; $y -le 700; $y += 5) {
    for ($x = 575; $x -le 595; $x += 1) {
        $p = $comp.GetPixel($x, $y)
        if ($p.R -lt 60 -and $p.G -lt 60 -and $p.B -lt 60) {
            Write-Host ("Dark pixel at X={0}, Y={1}: R={2}, G={3}, B={4}" -f $x, $y, $p.R, $p.G, $p.B)
            $darkFound++
        }
    }
}

Write-Host ("Total dark pixels outside right edge of bottle: {0}" -f $darkFound)
$comp.Dispose()
