Add-Type -AssemblyName System.Drawing

$brain = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612"

$images = @{
    "step1" = "$brain\step1_public_fear_1793437212289.jpg"
    "step2" = "$brain\step2_alone_help_1793437238688.jpg"
    "step3" = "$brain\card_career_fear_1793435999167.jpg"
    "step4" = "$brain\step4_social_hesitation_1793437229619.jpg"
    "step5" = "$brain\step5_family_concern_1793437249813.jpg"
    "step6" = "$brain\card_mental_tension_1793435208262.jpg"
}

foreach ($k in $images.Keys) {
    $path = $images[$k]
    $img = [System.Drawing.Bitmap]::FromFile($path)
    Write-Host "$k -> Width=$($img.Width), Height=$($img.Height)"
    $img.Dispose()
}

