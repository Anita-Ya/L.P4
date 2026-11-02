Add-Type -AssemblyName System.Drawing

$bot = [System.Drawing.Bitmap]::FromFile("$PWD\assets\real-bottle-clean-hd.png")
Write-Host "Real bottle png width: $($bot.Width), height: $($bot.Height), Aspect Ratio: $($bot.Width / $bot.Height)"
$bot.Dispose()

