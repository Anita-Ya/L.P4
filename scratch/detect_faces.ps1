Add-Type -AssemblyName System.Drawing

$brain = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612"

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
    $sumX = 0
    $sumY = 0
    $count = 0

    # Sample every 4 pixels between y=100 and y=650
    for ($y = 100; $y -lt 650; $y += 4) {
        for ($x = 100; $x -lt 924; $x += 4) {
            $p = $bmp.GetPixel($x, $y)
            $r = $p.R
            $g = $p.G
            $b = $p.B

            # Standard skin tone heuristic
            if ($r -gt 95 -and $g -gt 40 -and $b -gt 20 -and 
                ($r - $g) -gt 15 -and $r -gt $g -and $g -gt $b -and
                ($r - $b) -gt 15) {
                $sumX += $x
                $sumY += $y
                $count++
            }
        }
    }

    if ($count -gt 0) {
        $avgX = [int]($sumX / $count)
        $avgY = [int]($sumY / $count)
        Write-Host "$($item.name): Skin pixels=$count, Center=($avgX, $avgY)"
    } else {
        Write-Host "$($item.name): No skin detected"
    }
    $bmp.Dispose()
}

