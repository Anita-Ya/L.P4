$proc = Start-Process -FilePath 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe' -ArgumentList '--headless --screenshot file:///C:/Users/Anita%20Yadav/Desktop/L.P/LP%204/scratch/preview_certs.html' -PassThru -Wait
Write-Host "Exit code: $($proc.ExitCode)"
Get-ChildItem -Path . -Filter "screenshot.png"

