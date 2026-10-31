Add-Type -AssemblyName System.Drawing

$file = "c:\Users\Anita Yadav\Desktop\L.P\LP 4\assets\split-showcase-perfect.png"
$bmp = [System.Drawing.Bitmap]::FromFile($file)
Write-Host "Image size: $($bmp.Width) x $($bmp.Height)"

$minX = 9999; $maxX = 0; $minY = 9999; $maxY = 0; $count = 0

for ($y = 0; $y -lt 150; $y++) {
    for ($x = 0; $x -lt 250; $x++) {
        $p = $bmp.GetPixel($x, $y)
        # Blueish text color
        if ($p.R -lt 50 -and $p.G -lt 100 -and $p.B -gt 70) {
            if ($x -lt $minX) { $minX = $x }
            if ($x -gt $maxX) { $maxX = $x }
            if ($y -lt $minY) { $minY = $y }
            if ($y -gt $maxY) { $maxY = $y }
            $count++
        }
    }
}

Write-Host "Found $count text pixels. Bounds: X=[$minX, $maxX], Y=[$minY, $maxY]"

# Let's also check background color right above and below
$bgAbove = $bmp.GetPixel($minX, [Math]::Max(0, $minY - 5))
$bgBelow = $bmp.GetPixel($minX, [Math]::Min($bmp.Height - 1, $maxY + 5))
Write-Host "BG Above: R=$($bgAbove.R), G=$($bgAbove.G), B=$($bgAbove.B)"
Write-Host "BG Below: R=$($bgBelow.R), G=$($bgBelow.G), B=$($bgBelow.B)"

$bmp.Dispose()

