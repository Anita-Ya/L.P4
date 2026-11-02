Add-Type -AssemblyName System.Drawing

$pristinePath = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612\doctor_recommendation_portrait_1793596701212.jpg"
$orig = [System.Drawing.Bitmap]::FromFile($pristinePath)

for ($x = 575; $x -le 605; $x++) {
    $p = $orig.GetPixel($x, 615)
    Write-Host "X=$x, Y=615: R=$($p.R), G=$($p.G), B=$($p.B)"
}

$orig.Dispose()

