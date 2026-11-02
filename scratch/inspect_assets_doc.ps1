Add-Type -AssemblyName System.Drawing

$img = [System.Drawing.Bitmap]::FromFile("$PWD\assets\doctor-recommendation.jpg")

# Let's inspect the pixels around X=460..590, Y=530..720 in assets\doctor-recommendation.jpg
# Where is the green bottle, and where is the black bottle?
for ($y = 570; $y -le 700; $y += 20) {
    for ($x = 470; $x -le 580; $x += 10) {
        $p = $img.GetPixel($x, $y)
        Write-Host "X=$x, Y=$y -> R=$($p.R), G=$($p.G), B=$($p.B)"
    }
    Write-Host "---"
}

$img.Dispose()

