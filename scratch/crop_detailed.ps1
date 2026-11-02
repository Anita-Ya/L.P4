Add-Type -AssemblyName System.Drawing

$pristinePath = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612\doctor_recommendation_portrait_1793596701212.jpg"
$orig = [System.Drawing.Bitmap]::FromFile($pristinePath)

$rect = New-Object System.Drawing.Rectangle(440, 510, 180, 240)
$crop = $orig.Clone($rect, $orig.PixelFormat)
$crop.Save("$PWD\scratch\orig_bottle_zoom_detailed.jpg", [System.Drawing.Imaging.ImageFormat]::Jpeg)
$crop.Dispose()
$orig.Dispose()

Write-Host "Saved orig_bottle_zoom_detailed.jpg"

