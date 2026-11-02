Add-Type -AssemblyName System.Drawing

$bot = [System.Drawing.Bitmap]::FromFile("$PWD\assets\real-bottle-clean-hd.png")

# Find non-transparent bounding box of real-bottle-clean-hd.png
$minX = $bot.Width; $maxX = 0; $minY = $bot.Height; $maxY = 0

for ($y = 0; $y -lt $bot.Height; $y++) {
    for ($x = 0; $x -lt $bot.Width; $x++) {
        $p = $bot.GetPixel($x, $y)
        if ($p.A -gt 10) {
            if ($x -lt $minX) { $minX = $x }
            if ($x -gt $maxX) { $maxX = $x }
            if ($y -lt $minY) { $minY = $y }
            if ($y -gt $maxY) { $maxY = $y }
        }
    }
}

Write-Host "Non-transparent bounds in 400x700 image:"
Write-Host "X: $minX .. $maxX (Width: $($maxX - $minX))"
Write-Host "Y: $minY .. $maxY (Height: $($maxY - $minY))"
$bot.Dispose()

