$html = Get-Content 'index.html' -Raw
$matches = [regex]::Matches($html, 'src="([^"?]+)')

Write-Host "Verifying image sources in index.html:"
$missing = 0
foreach ($m in $matches) {
    $src = $m.Groups[1].Value
    if ($src -notlike 'http*' -and $src -notlike 'data:*') {
        if (Test-Path $src) {
            Write-Host "  [OK] $src"
        } else {
            Write-Host "  [MISSING] $src" -ForegroundColor Red
            $missing++
        }
    }
}

if ($missing -eq 0) {
    Write-Host "`nAll image assets exist successfully!" -ForegroundColor Green
} else {
    Write-Host "`nWarning: $missing images missing!" -ForegroundColor Red
}

