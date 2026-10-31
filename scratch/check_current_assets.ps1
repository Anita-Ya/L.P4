Add-Type -AssemblyName System.Drawing

$files = @("step1-public-fear.jpg", "step2-alone-help.jpg", "step3-career-worry.jpg", "step4-social-hesitation.jpg", "step5-family-concern.jpg", "step6-future-questions.jpg")

foreach ($f in $files) {
    $path = "c:\Users\Anita Yadav\Desktop\L.P\LP 4\assets\$f"
    if (Test-Path $path) {
        $bmp = [System.Drawing.Bitmap]::FromFile($path)
        $sumX = 0
        $sumY = 0
        $count = 0
        for ($y = 0; $y -lt $bmp.Height; $y += 2) {
            for ($x = 0; $x -lt $bmp.Width; $x += 2) {
                $p = $bmp.GetPixel($x, $y)
                if ($p.R -gt 90 -and $p.G -gt 40 -and $p.B -gt 20 -and ($p.R - $p.G) -gt 10 -and $p.R -gt $p.B) {
                    $sumX += $x
                    $sumY += $y
                    $count++
                }
            }
        }
        if ($count -gt 0) {
            $cx = [int]($sumX / $count)
            $cy = [int]($sumY / $count)
            Write-Host "$f ($($bmp.Width)x$($bmp.Height)): Center=($cx, $cy), offset from mid=($($cx - $bmp.Width/2), $($cy - $bmp.Height/2))"
        } else {
            Write-Host "$f ($($bmp.Width)x$($bmp.Height)): No skin detected"
        }
        $bmp.Dispose()
    }
}

