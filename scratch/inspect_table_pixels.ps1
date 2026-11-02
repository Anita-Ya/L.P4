Add-Type -AssemblyName System.Drawing

$table = [System.Drawing.Bitmap]::FromFile("$PWD\scratch\orig_table.jpg")
# Check if there are any green or dark bottle pixels in this table crop
$minVal = 255; $maxVal = 0
for ($y = 0; $y -lt $table.Height; $y += 5) {
    for ($x = 0; $x -lt $table.Width; $x += 5) {
        $p = $table.GetPixel($x, $y)
        if ($p.R -lt 50 -and $p.G -lt 50) {
            # dark pixel
        }
    }
}
Write-Host "Table inspected."
$table.Dispose()

