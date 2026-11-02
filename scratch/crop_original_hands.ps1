Add-Type -AssemblyName System.Drawing

$origPath = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612\doctor_recommendation_portrait_1793596701212.jpg"
$orig = [System.Drawing.Bitmap]::FromFile($origPath)

Write-Host "Width: $($orig.Width), Height: $($orig.Height)"

# Crop around doctor's hands: X=400 to 650, Y=450 to 750
$rect = New-Object System.Drawing.Rectangle(400, 450, 250, 300)
$hands = $orig.Clone($rect, $orig.PixelFormat)
$hands.Save("$PWD\scratch\original_doctor_hands.jpg", [System.Drawing.Imaging.ImageFormat]::Jpeg)
$hands.Dispose()
$orig.Dispose()

Write-Host "Saved original_doctor_hands.jpg"

