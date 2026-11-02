Add-Type -AssemblyName System.Drawing

$brain = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612"

$files = @(
    "step1_public_fear_1793437212289.jpg",
    "step2_alone_help_1793437238688.jpg",
    "card_career_fear_1793435999167.jpg",
    "step4_social_hesitation_1793437229619.jpg",
    "step5_family_concern_1793437249813.jpg",
    "card_mental_tension_1793435208262.jpg"
)

foreach ($f in $files) {
    $p = "$brain\$f"
    $img = [System.Drawing.Bitmap]::FromFile($p)
    Write-Host "$f : Width=$($img.Width), Height=$($img.Height)"
    $img.Dispose()
}

