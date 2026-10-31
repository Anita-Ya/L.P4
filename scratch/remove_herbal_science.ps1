Add-Type -AssemblyName System.Drawing

$file = "c:\Users\Anita Yadav\Desktop\L.P\LP 4\assets\split-showcase-perfect.png"

# Read into memory so file is not locked
$bytes = [System.IO.File]::ReadAllBytes($file)
$ms = New-Object System.IO.MemoryStream($bytes, 0, $bytes.Length)
$src = [System.Drawing.Bitmap]::FromStream($ms)

$dest = New-Object System.Drawing.Bitmap($src.Width, $src.Height, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
$g = [System.Drawing.Graphics]::FromImage($dest)
$g.DrawImage($src, 0, 0, $src.Width, $src.Height)
$g.Dispose()

$src.Dispose()
$ms.Dispose()

# Now inpaint X=[25, 175], Y=[25, 62] using vertical column interpolation
for ($x = 25; $x -le 175; $x++) {
    $topPixel = $dest.GetPixel($x, 24)
    $bottomPixel = $dest.GetPixel($x, 63)

    for ($y = 25; $y -le 62; $y++) {
        $t = ($y - 25.0) / (63.0 - 25.0)
        $r = [int]($topPixel.R * (1 - $t) + $bottomPixel.R * $t)
        $g = [int]($topPixel.G * (1 - $t) + $bottomPixel.G * $t)
        $b = [int]($topPixel.B * (1 - $t) + $bottomPixel.B * $t)
        $a = [int]($topPixel.A * (1 - $t) + $bottomPixel.A * $t)

        $dest.SetPixel($x, $y, [System.Drawing.Color]::FromArgb($a, $r, $g, $b))
    }
}

$dest.Save($file, [System.Drawing.Imaging.ImageFormat]::Png)
$dest.Dispose()

Write-Host "HERBAL SCIENCE successfully removed from split-showcase-perfect.png!"
