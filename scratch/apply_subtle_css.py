import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

css_subtle = """

/* ==========================================================================
   SUBTLE / LOW-KEY DISCLAIMER STYLES (Requested by User)
   ========================================================================== */
.site-footer.invisible-disclaimer-mode {
  padding: 18px 16px 32px 16px;
  background: #F2F8FB;
}

.disclaimer-subtle-wrap {
  width: 100%;
  max-width: 420px;
  margin: 0 auto;
  opacity: 0.55;
  transition: opacity 0.3s ease;
}

.disclaimer-subtle-wrap:hover {
  opacity: 0.85;
}

.disclaimer-title-subtle {
  font-family: 'Poppins', 'Mukta', sans-serif;
  font-size: 11px;
  font-weight: 700;
  color: #6C8294;
  margin: 0 0 5px 0;
  letter-spacing: 0.3px;
  text-transform: uppercase;
}

.disclaimer-para-subtle {
  font-family: 'Mukta', sans-serif;
  font-size: 10.5px;
  line-height: 1.45;
  color: #7B8F9E;
  margin: 0 0 6px 0;
  text-align: justify;
  font-weight: 400;
}

.disclaimer-para-subtle.legal-subtle {
  font-size: 10px;
  line-height: 1.4;
  color: #8C9EA8;
  margin-bottom: 12px;
}

.footer-subtle-bottom {
  text-align: center;
  padding-top: 10px;
  border-top: 1px solid rgba(11, 60, 93, 0.08);
}

.copyright-subtle {
  font-family: 'Mukta', sans-serif;
  font-size: 11px;
  color: #8A9CA8;
  margin: 0 0 4px 0;
}

.footer-links-subtle {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  font-family: 'Poppins', sans-serif;
  font-size: 10.5px;
  color: #7B8F9E;
}
"""

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_subtle)

# Update index.html cachebuster
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'style\.css\?v=[^\"]+', 'style.css?v=subtle_clean_v2', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Appended subtle styles and updated cachebuster!")

