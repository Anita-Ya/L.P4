Add-Type -AssemblyName System.Drawing

$files = @(
    "assets/step1-public-fear.jpg",
    "assets/step2-alone-help.jpg",
    "assets/step3-career-worry.jpg",
    "assets/step4-social-hesitation.jpg",
    "assets/step5-family-concern.jpg",
    "assets/step6-future-questions.jpg"
)

foreach ($f in $files) {
    if (Test-Path $f) {
        $img = [System.Drawing.Bitmap]::FromFile("$PWD\$f")
        Write-Host "$f : Width=$($img.Width), Height=$($img.Height)"
        $img.Dispose()
    } else {
        Write-Host "$f NOT FOUND"
    }
}

