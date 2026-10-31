Add-Type -AssemblyName System.Drawing

$brain = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612"

# Let's inspect step1, step2, step3, step4, step5, step6
# We can create a grid image for each original with grid lines every 100px
$images = @(
    @{ name="step1"; file="$brain\step1_public_fear_1793437212289.jpg" },
    @{ name="step2"; file="$brain\step2_alone_help_1793437238688.jpg" },
    @{ name="step3"; file="$brain\card_career_fear_1793435999167.jpg" },
    @{ name="step4"; file="$brain\step4_social_hesitation_1793437229619.jpg" },
    @{ name="step5"; file="$brain\step5_family_concern_1793437249813.jpg" },
    @{ name="step6"; file="$brain\card_mental_tension_1793435208262.jpg" }
)

foreach ($item in $images) {
    $bmp = [System.Drawing.Bitmap]::FromFile($item.file)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $pen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(180, 255, 255, 0), 2)
    $font = New-Object System.Drawing.Font("Arial", 16, [System.Drawing.FontStyle]::Bold)
    $brush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::Yellow)

    for ($x = 100; $x -lt 1024; $x += 100) {
        $g.DrawLine($pen, $x, 0, $x, 1024)
        $g.DrawString("$x", $font, $brush, [float]($x + 2), 10.0)
    }
    for ($y = 100; $y -lt 1024; $y += 100) {
        $g.DrawLine($pen, 0, $y, 1024, $y)
        $g.DrawString("$y", $font, $brush, 10.0, [float]($y + 2))
    }

    $g.Dispose()
    $pen.Dispose()
    $font.Dispose()
    $brush.Dispose()

    $outPath = "scratch/grid_$($item.name).jpg"
    $bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Jpeg)
    $bmp.Dispose()
    Write-Host "Saved grid for $($item.name) to $outPath"
}

