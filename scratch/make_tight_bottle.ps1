Add-Type -AssemblyName System.Drawing

$bot = [System.Drawing.Bitmap]::FromFile("$PWD\assets\real-bottle-clean-hd.png")
$tightRect = New-Object System.Drawing.Rectangle(34, 20, 332, 656)
$tightBot = $bot.Clone($tightRect, $bot.PixelFormat)
$tightBot.Save("$PWD\scratch\tight_bottle.png", [System.Drawing.Imaging.ImageFormat]::Png)
$tightBot.Dispose()
$bot.Dispose()

Write-Host "Created scratch\tight_bottle.png with 0px transparent border!"

