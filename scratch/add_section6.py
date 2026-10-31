with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '</main>'

section_html = """    <!-- 6. PRODUCT QUALITY & TRUST SECTION (INTERLOCKING HEXAGON CHAIN) -->
    <section class="quality-trust-section" id="qualityTrustSection">
      
      <!-- Section Header -->
      <div class="quality-header">
        <div class="quality-tag">
          <span class="quality-pulse"></span>
          <span>6. PRODUCT QUALITY & TRUST</span>
        </div>
        <h2 class="quality-main-title">विश्वसनीयता और सुरक्षा के कड़े मानक</h2>
        <p class="quality-sub-desc">हर कैप्सूल में शुद्धता, सुरक्षा और उच्चतम गुणवत्ता सुनिश्चित करने के लिए प्रमाणित।</p>
      </div>

      <!-- Interlocking Staggered Hexagon Honeycomb Chain -->
      <div class="trust-hex-chain">

        <!-- Card 1: Top Right (GMP) -->
        <div class="hex-item-wrap pos-right">
          <!-- Backplate (Teal) -->
          <svg class="hex-backplate" viewBox="0 0 200 230">
            <path d="M 100,12 L 182,59 A 16,16 0 0,1 190,73 L 190,157 A 16,16 0 0,1 182,171 L 100,218 A 16,16 0 0,1 90,218 L 18,171 A 16,16 0 0,1 10,157 L 10,73 A 16,16 0 0,1 18,59 L 90,12 A 16,16 0 0,1 100,12 Z" fill="#33C3A5" />
          </svg>
          <!-- Main Card -->
          <svg class="hex-main-bg" viewBox="0 0 200 230">
            <path d="M 100,12 L 182,59 A 16,16 0 0,1 190,73 L 190,157 A 16,16 0 0,1 182,171 L 100,218 A 16,16 0 0,1 90,218 L 18,171 A 16,16 0 0,1 10,157 L 10,73 A 16,16 0 0,1 18,59 L 90,12 A 16,16 0 0,1 100,12 Z" fill="#FFFFFF" stroke="#E2EDF3" stroke-width="1.5" />
          </svg>
          <div class="hex-content">
            <div class="hex-badge-box">
              <img src="assets/cert1.avif" alt="GMP" class="hex-badge-img">
            </div>
            <h3 class="hex-card-title">GMP</h3>
            <p class="hex-card-desc">Good Manufacturing Practice के कड़े अंतरराष्ट्रीय मानकों पर प्रमाणित।</p>
          </div>
        </div>

        <!-- Card 2: Left (FSSAI / AYUSH) -->
        <div class="hex-item-wrap pos-left">
          <!-- Backplate (Navy) -->
          <svg class="hex-backplate" viewBox="0 0 200 230">
            <path d="M 100,12 L 182,59 A 16,16 0 0,1 190,73 L 190,157 A 16,16 0 0,1 182,171 L 100,218 A 16,16 0 0,1 90,218 L 18,171 A 16,16 0 0,1 10,157 L 10,73 A 16,16 0 0,1 18,59 L 90,12 A 16,16 0 0,1 100,12 Z" fill="#0B3C5D" />
          </svg>
          <!-- Main Card -->
          <svg class="hex-main-bg" viewBox="0 0 200 230">
            <path d="M 100,12 L 182,59 A 16,16 0 0,1 190,73 L 190,157 A 16,16 0 0,1 182,171 L 100,218 A 16,16 0 0,1 90,218 L 18,171 A 16,16 0 0,1 10,157 L 10,73 A 16,16 0 0,1 18,59 L 90,12 A 16,16 0 0,1 100,12 Z" fill="#FFFFFF" stroke="#E2EDF3" stroke-width="1.5" />
          </svg>
          <div class="hex-content">
            <div class="hex-badge-box">
              <img src="assets/cert3.avif" alt="FSSAI / AYUSH" class="hex-badge-img">
            </div>
            <h3 class="hex-card-title">FSSAI / AYUSH</h3>
            <p class="hex-card-desc">खाद्य सुरक्षा एवं आयुष मानकों के अनुरूप 100% सुरक्षित और प्रामाणिक।</p>
          </div>
        </div>

        <!-- Card 3: Right (LAB TESTED) -->
        <div class="hex-item-wrap pos-right">
          <!-- Backplate (Teal) -->
          <svg class="hex-backplate" viewBox="0 0 200 230">
            <path d="M 100,12 L 182,59 A 16,16 0 0,1 190,73 L 190,157 A 16,16 0 0,1 182,171 L 100,218 A 16,16 0 0,1 90,218 L 18,171 A 16,16 0 0,1 10,157 L 10,73 A 16,16 0 0,1 18,59 L 90,12 A 16,16 0 0,1 100,12 Z" fill="#33C3A5" />
          </svg>
          <!-- Main Card -->
          <svg class="hex-main-bg" viewBox="0 0 200 230">
            <path d="M 100,12 L 182,59 A 16,16 0 0,1 190,73 L 190,157 A 16,16 0 0,1 182,171 L 100,218 A 16,16 0 0,1 90,218 L 18,171 A 16,16 0 0,1 10,157 L 10,73 A 16,16 0 0,1 18,59 L 90,12 A 16,16 0 0,1 100,12 Z" fill="#FFFFFF" stroke="#E2EDF3" stroke-width="1.5" />
          </svg>
          <div class="hex-content">
            <div class="hex-badge-box">
              <img src="assets/cert4.avif" alt="LAB TESTED" class="hex-badge-img">
            </div>
            <h3 class="hex-card-title">LAB TESTED</h3>
            <p class="hex-card-desc">शुद्धता व गुणवत्ता के लिए प्रमाणित प्रयोगशाला द्वारा पूरी तरह जाँचा गया।</p>
          </div>
        </div>

        <!-- Card 4: Left (ISO) -->
        <div class="hex-item-wrap pos-left">
          <!-- Backplate (Navy) -->
          <svg class="hex-backplate" viewBox="0 0 200 230">
            <path d="M 100,12 L 182,59 A 16,16 0 0,1 190,73 L 190,157 A 16,16 0 0,1 182,171 L 100,218 A 16,16 0 0,1 90,218 L 18,171 A 16,16 0 0,1 10,157 L 10,73 A 16,16 0 0,1 18,59 L 90,12 A 16,16 0 0,1 100,12 Z" fill="#0B3C5D" />
          </svg>
          <!-- Main Card -->
          <svg class="hex-main-bg" viewBox="0 0 200 230">
            <path d="M 100,12 L 182,59 A 16,16 0 0,1 190,73 L 190,157 A 16,16 0 0,1 182,171 L 100,218 A 16,16 0 0,1 90,218 L 18,171 A 16,16 0 0,1 10,157 L 10,73 A 16,16 0 0,1 18,59 L 90,12 A 16,16 0 0,1 100,12 Z" fill="#FFFFFF" stroke="#E2EDF3" stroke-width="1.5" />
          </svg>
          <div class="hex-content">
            <div class="hex-badge-box">
              <img src="assets/iso.avif" alt="ISO" class="hex-badge-img">
            </div>
            <h3 class="hex-card-title">ISO</h3>
            <p class="hex-card-desc">अंतरराष्ट्रीय गुणवत्ता प्रबंधन (ISO 9001) मानकों से मान्यता प्राप्त।</p>
          </div>
        </div>

      </div>

    </section>

  """

if target in content:
    new_content = content.replace(target, section_html + target)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: Section 6 added to index.html!")
else:
    print("ERROR: target not found!")

