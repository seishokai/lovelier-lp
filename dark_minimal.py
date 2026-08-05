#!/usr/bin/env python3
import base64, os
from PIL import Image, ImageOps
from io import BytesIO

OUTPUT_HTML = r"C:\Users\USER\lovelier-lp\index.html"

def img_b64(path, size=1000, q=75):
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)
    img.thumbnail((size, size), Image.Resampling.LANCZOS)
    buf = BytesIO()
    img.save(buf, format='JPEG', quality=q, optimize=True)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"

# ノアさん画像：最初の 8 枚を自動選別（高品質顔のアップ想定）
noa = []
noa_dir = r"C:\Users\USER\Downloads\lovelier_images\ラブリエ\ノアさん"
if os.path.exists(noa_dir):
    for f in sorted(os.listdir(noa_dir))[:8]:
        if f.endswith(('.jpg','.JPG')):
            noa.append(img_b64(os.path.join(noa_dir, f), size=1200, q=80))

# 症例画像：最初の 8 枚を自動選別
cases = []
cases_dir = r"C:\Users\USER\Downloads\lovelier_images\ラブリエ"
if os.path.exists(cases_dir):
    for d in sorted(os.listdir(cases_dir)):
        dp = os.path.join(cases_dir, d)
        if os.path.isdir(dp) and d not in ["ノアさん"]:
            for f in sorted(os.listdir(dp)):
                if f.endswith(('.jpg','.JPG')) and len(cases) < 8:
                    cases.append(img_b64(os.path.join(dp, f), size=900, q=85))

print(f"NOA: {len(noa)}, CASES: {len(cases)}")

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lovelier | 削らない最先端ジルコニアベニア × YouTuber ノア</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Noto+Serif+JP:wght@200;300;400;500;600&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}html{{scroll-behavior:smooth}}
body{{font-family:'Noto Serif JP',serif;background:#0f0f0f;color:#ffffff;line-height:1.8;overflow-x:hidden}}
img{{max-width:100%;height:auto;display:block}}a{{text-decoration:none;transition:all 0.3s}}

/* Navigation */
nav{{position:fixed;top:0;width:100%;background:rgba(15,15,15,0.98);backdrop-filter:blur(10px);z-index:1000;padding:20px 40px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(212,175,55,0.2)}}
nav .logo{{font-family:'Playfair Display',serif;font-size:24px;font-weight:700;color:#d4af37}}
nav ul{{display:flex;list-style:none;gap:40px}}
nav a{{color:#ffffff;font-size:13px;letter-spacing:0.1em;text-transform:uppercase;position:relative}}
nav a:hover{{color:#d4af37}}

/* Hero */
.hero{{background:linear-gradient(135deg,rgba(0,0,0,0.6),rgba(0,0,0,0.4)),url('{noa[0] if noa else ''}');background-size:cover;background-position:center;background-attachment:fixed;min-height:100vh;display:flex;align-items:center;justify-content:center;color:#fff;text-align:center;padding:100px 20px;margin-top:60px;position:relative}}
.hero-content{{max-width:800px;position:relative;z-index:2}}.hero .label{{font-size:12px;letter-spacing:0.3em;color:#d4af37;margin-bottom:25px;text-transform:uppercase;font-weight:600}}.hero h1{{font-size:72px;font-family:'Playfair Display',serif;font-weight:700;line-height:1.2;margin-bottom:25px}}.hero .sub{{font-size:18px;font-weight:300;line-height:1.8;margin-bottom:50px;opacity:0.95}}
.btn{{display:inline-block;background:#d4af37;color:#000;padding:16px 48px;font-size:12px;letter-spacing:0.2em;font-weight:600;margin:12px;cursor:pointer;border:2px solid #d4af37;border-radius:0;text-transform:uppercase;transition:all 0.3s}}.btn:hover{{background:transparent;color:#d4af37}}
.btn-outline{{background:transparent;color:#ffffff;border-color:#d4af37}}.btn-outline:hover{{background:#d4af37;color:#000}}

/* Sections */
section{{padding:120px 0}}section.dark{{background:#0a0a0a}}
.container{{max-width:1200px;margin:0 auto;padding:0 40px}}

.sec-title{{text-align:center;padding:40px 20px}}.sec-title .label{{font-size:11px;letter-spacing:0.35em;color:#d4af37;margin-bottom:15px;text-transform:uppercase;font-weight:600}}.sec-title h2{{font-size:48px;font-family:'Playfair Display',serif;font-weight:700;margin-bottom:15px;color:#ffffff}}.sec-title .bar{{width:60px;height:2px;background:linear-gradient(90deg,transparent,#d4af37,transparent);margin:0 auto}}

/* Why Section */
.why-points{{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin-top:60px;text-align:center}}.point{{padding:30px}}.point h3{{font-size:28px;color:#d4af37;font-family:'Playfair Display',serif;margin-bottom:12px}}.point p{{font-size:14px;color:#cccccc;line-height:1.8}}

/* Features Grid */
.features-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:50px;margin-top:60px}}.feature-card{{padding:50px 40px;background:rgba(255,255,255,0.03);border:1px solid rgba(212,175,55,0.2);transition:all 0.4s}}.feature-card:hover{{background:rgba(212,175,55,0.1);border-color:#d4af37}}.feature-card .num{{font-size:56px;color:#d4af37;font-family:'Playfair Display',serif;margin-bottom:15px}}.feature-card h3{{font-size:20px;font-weight:600;margin-bottom:15px;color:#ffffff}}.feature-card p{{font-size:14px;color:#aaaaaa;line-height:1.9}}

/* Cases Grid */
.cases-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;margin-top:60px}}.case-item{{aspect-ratio:1;overflow:hidden;border-radius:2px;background:#1a1a1a;box-shadow:0 8px 30px rgba(0,0,0,0.5)}}.case-item img{{width:100%;height:100%;object-fit:cover;transition:transform 0.4s}}.case-item:hover img{{transform:scale(1.05)}}

/* Pricing */
.pricing-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin-top:60px}}.price-card{{padding:50px 40px;background:rgba(255,255,255,0.02);border:1px solid rgba(212,175,55,0.2);text-align:center;transition:all 0.4s}}.price-card:hover{{background:rgba(212,175,55,0.1);border-color:#d4af37;transform:translateY(-8px)}}.price-card h3{{font-size:16px;font-weight:600;margin-bottom:15px;color:#ffffff}}.price-card .amount{{font-size:44px;color:#d4af37;font-family:'Playfair Display',serif;margin:20px 0}}.price-card .note{{font-size:11px;color:#888;margin-top:15px}}

/* Footer */
.footer{{background:#000000;padding:60px 40px;text-align:center;border-top:1px solid rgba(212,175,55,0.2)}}.footer h2{{font-size:32px;font-family:'Playfair Display',serif;font-weight:700;margin-bottom:10px;color:#d4af37}}.footer p{{font-size:12px;color:#888;margin:8px 0}}

@media(max-width:1024px){{.container{{padding:0 30px}}nav ul{{gap:25px}}.cases-grid{{grid-template-columns:repeat(2,1fr)}}.pricing-grid{{grid-template-columns:repeat(2,1fr)}}.features-grid{{grid-template-columns:1fr}}.why-points{{grid-template-columns:1fr}}}}
@media(max-width:768px){{nav{{padding:15px 16px}}.hero{{margin-top:50px;padding:60px 16px;min-height:70vh}}.hero h1{{font-size:42px}}.container{{padding:0 16px}}section{{padding:80px 0}}.cases-grid{{grid-template-columns:1fr}}.pricing-grid{{grid-template-columns:1fr}}.sec-title h2{{font-size:32px}}nav ul{{gap:15px;font-size:11px}}.features-grid{{gap:30px}}}}
</style>
</head>
<body>

<nav id="navbar">
  <div class="logo">Lovelier</div>
  <ul>
    <li><a href="#why">特徴</a></li>
    <li><a href="#cases">症例</a></li>
    <li><a href="#pricing">価格</a></li>
    <li><a href="#booking" class="btn" style="margin:0">予約</a></li>
  </ul>
</nav>

<section class="hero">
  <div class="hero-content">
    <div class="label">世界唯一の最先端技術</div>
    <h1>削らない<br>ジルコニアベニア<br><span style="color:#d4af37;">Lovelier</span></h1>
    <p class="sub">0.04mm最薄 × 人工ダイヤモンド級の強度 × 完全無痛<br>YouTuber・ノアさんも体験した次世代審美治療</p>
    <a href="#booking" class="btn">無料カウンセリング予約</a>
    <a href="#why" class="btn btn-outline">詳しく見る</a>
  </div>
</section>

<section id="why">
  <div class="container">
    <div class="sec-title">
      <div class="label">Why Lovelier</div>
      <h2>ラブリエが選ばれる理由</h2>
      <div class="bar"></div>
    </div>
    <div class="why-points">
      <div class="point">
        <h3>世界唯一<br>0.04mm</h3>
        <p>超薄加工技術で、削らずに完璧な審美性を実現</p>
      </div>
      <div class="point">
        <h3>完全無痛<br>歯を削らない</h3>
        <p>痛みなし、歯へのダメージゼロで健康を守る</p>
      </div>
      <div class="point">
        <h3>最短3週間<br>で完成</h3>
        <p>ダイヤモンド級の強度で半永久的に美しさ保証</p>
      </div>
    </div>
  </div>
</section>

<section class="dark">
  <div class="container">
    <div class="sec-title">
      <div class="label">Four Features</div>
      <h2>ラブリエの特徴</h2>
      <div class="bar"></div>
    </div>
    <div class="features-grid">
      <div class="feature-card">
        <div class="num">01</div>
        <h3>最薄 0.04mm<br>（世界唯一）</h3>
        <p>世界でも唯一無二の超薄加工技術により、わずか0.04mmの厚さを実現。削らずに前歯が出ない自然な仕上がりを完全に実現できます。</p>
      </div>
      <div class="feature-card">
        <div class="num">02</div>
        <h3>完全無痛<br>歯を削らない</h3>
        <p>歯を削りません。痛みもありません。健康な歯をそのまま保ちながら、完璧な審美性を手に入れることができます。</p>
      </div>
      <div class="feature-card">
        <div class="num">03</div>
        <h3>人工ダイヤモンド級<br>の強度</h3>
        <p>ジルコニア素材は人工ダイヤモンドに匹敵する強度を持ちます。薄くても割れず、セラミックのように欠けることもありません。</p>
      </div>
      <div class="feature-card">
        <div class="num">04</div>
        <h3>完全自由な<br>色・形選択</h3>
        <p>自身の歯が透けないため、理想の色と形を完全に自由に選択できます。1本単位での治療も可能。完全オーダーメイドの笑顔をデザイン。</p>
      </div>
    </div>
  </div>
</section>

<section id="cases">
  <div class="container">
    <div class="sec-title">
      <div class="label">Treatment Cases</div>
      <h2>実際の治療例</h2>
      <div class="bar"></div>
    </div>
    <div class="cases-grid">
"""

for b64 in cases:
    html += f'      <div class="case-item"><img src="{b64}" alt=""></div>\n'

html += f"""    </div>
  </div>
</section>

<section class="dark" id="pricing">
  <div class="container">
    <div class="sec-title">
      <div class="label">Pricing</div>
      <h2>価格について</h2>
      <div class="bar"></div>
    </div>
    <div class="pricing-grid">
      <div class="price-card">
        <h3>ラブリエ（1本）</h3>
        <div class="amount">¥79,000～<br>¥115,000</div>
        <div class="note">税抜 / 症例による</div>
      </div>
      <div class="price-card">
        <h3>全顔モニター</h3>
        <div class="amount">¥1,264,000<br>～</div>
        <div class="note">税抜 / 16本以上</div>
      </div>
      <div class="price-card">
        <h3>保証</h3>
        <div class="amount">3年間<br>+¥22,000</div>
        <div class="note">10年延長保証/本</div>
      </div>
    </div>
  </div>
</section>

<section id="booking" style="background:linear-gradient(135deg,#d4af37,#c4a04d);text-align:center;padding:100px 40px">
  <h2 style="font-size:48px;color:#000;font-family:'Playfair Display',serif;margin-bottom:25px">理想の笑顔へ</h2>
  <p style="font-size:16px;color:#000;margin-bottom:40px;opacity:0.9">削らない、痛みなし。最短3週間で完成。<br>世界で一つだけのあなたの笑顔を。</p>
  <a href="#" class="btn" style="background:#000;color:#d4af37;border-color:#000;padding:18px 52px">無料カウンセリング予約</a>
</section>

<footer class="footer">
  <h2>Lovelier</h2>
  <p>削らないジルコニアベニア 最先端審美治療</p>
  <p style="margin-top:20px;font-size:10px">名古屋ウィズ歯科・矯正歯科 / BF中日ビル歯科<br>© 2026 清翔会</p>
</footer>

</body>
</html>
"""

with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Dark Minimal Complete! {os.path.getsize(OUTPUT_HTML)/(1024*1024):.2f}MB")
