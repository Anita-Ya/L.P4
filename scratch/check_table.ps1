Add-Type -AssemblyName System.Drawing

$origPath = "C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612\doctor_recommendation_portrait_1793596701212.jpg"
$orig = [System.Drawing.Bitmap]::FromFile($origPath)

# Check table area around X=150..250, Y=500..650
$rect = New-Object System.Drawing.Rectangle(150, 480, 160, 200)
$table = $orig.Clone($rect, $orig.PixelFormat)
$table.Save("$PWD\scratch\orig_table.jpg", [System.Drawing.Imaging.ImageFormat]::Jpeg)
$table.Dispose()
$orig.Dispose()

Write-Host "Saved scratch\orig_table.jpg"

