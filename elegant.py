#!/usr/bin/env python3
import base64, os
from PIL import Image, ImageOps
from io import BytesIO

OUTPUT_HTML = r"C:\Users\USER\lovelier-lp\index.html"

def img_b64(path, size=1000, q=80):
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)
    img.thumbnail((size, size), Image.Resampling.LANCZOS)
    buf = BytesIO()
    img.save(buf, format='JPEG', quality=q, optimize=True)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"

# ノアさん：4枚のみ
noa = []
noa_dir = r"C:\Users\USER\Downloads\lovelier_images\ラブリエ\ノアさん"
if os.path.exists(noa_dir):
    files = sorted(os.listdir(noa_dir))
    step = len(files) // 4
    indices = [0, step, step*2, step*3]
    for idx in indices:
        if idx < len(files):
            f = files[idx]
            if f.endswith(('.jpg','.JPG')):
                noa.append(img_b64(os.path.join(noa_dir, f), size=1200, q=90))

# 症例画像：20枚
cases = []
cases_dir = r"C:\Users\USER\Downloads\lovelier_images\ラブリエ"
if os.path.exists(cases_dir):
    for d in sorted(os.listdir(cases_dir)):
        dp = os.path.join(cases_dir, d)
        if os.path.isdir(dp) and d not in ["ノアさん"]:
            for f in sorted(os.listdir(dp)):
                if f.endswith(('.jpg','.JPG')) and len(cases) < 20:
                    cases.append(img_b64(os.path.join(dp, f), size=900, q=85))

print(f"NOA: {len(noa)}, CASES: {len(cases)}")

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lovelier | 削らない最先端ジルコニアベニア</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Noto+Serif+JP:wght@200;300;400;500;600&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}html{{scroll-behavior:smooth}}
body{{font-family:'Noto Serif JP',serif;background:#ffffff;color:#1a1a1a;line-height:1.8;overflow-x:hidden}}
img{{max-width:100%;height:auto;display:block}}a{{text-decoration:none;transition:all 0.3s}}

nav{{position:fixed;top:0;width:100%;background:#ffffff;backdrop-filter:blur(10px);z-index:1000;padding:20px 40px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #f0f0f0;box-shadow:0 1px 3px rgba(0,0,0,0.05)}}
nav .logo{{font-family:'Playfair Display',serif;font-size:24px;font-weight:700;color:#d4af37}}
nav ul{{display:flex;list-style:none;gap:40px}}
nav a{{color:#1a1a1a;font-size:12px;letter-spacing:0.1em;text-transform:uppercase;font-weight:600}}
nav a:hover{{color:#d4af37}}

.hero{{background:linear-gradient(135deg,#f9f9f9 0%,#ffffff 100%);min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:100px 40px;margin-top:60px;position:relative}}
.hero-content{{max-width:900px}}.hero .label{{font-size:12px;letter-spacing:0.35em;color:#d4af37;margin-bottom:25px;text-transform:uppercase;font-weight:700}}.hero h1{{font-size:92px;font-family:'Playfair Display',serif;font-weight:700;line-height:1.1;margin-bottom:30px;color:#1a1a1a}}.hero .sub{{font-size:20px;font-weight:300;line-height:1.8;margin-bottom:55px;color:#666}}
.btn{{display:inline-block;background:#d4af37;color:#1a1a1a;padding:15px 45px;font-size:12px;letter-spacing:0.2em;font-weight:700;margin:12px;cursor:pointer;border:2px solid #d4af37;border-radius:0;text-transform:uppercase;transition:all 0.3s}}.btn:hover{{background:#ffffff;color:#d4af37;box-shadow:0 4px 15px rgba(212,175,55,0.2)}}

section{{padding:100px 40px}}section.light{{background:#fafaf9}}
.container{{max-width:1300px;margin:0 auto}}

.sec-title{{text-align:center;padding:40px 0 60px;margin-bottom:40px}}.sec-title .label{{font-size:11px;letter-spacing:0.35em;color:#d4af37;margin-bottom:15px;text-transform:uppercase;font-weight:700}}.sec-title h2{{font-size:48px;font-family:'Playfair Display',serif;font-weight:700;margin-bottom:15px;color:#1a1a1a}}.sec-title p{{font-size:15px;color:#888;margin-top:10px}}

.intro-text{{max-width:900px;margin:50px auto;text-align:center;font-size:16px;color:#666;line-height:1.9}}
.intro-text strong{{color:#1a1a1a;font-weight:600}}

.features-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:40px;margin-top:50px}}.feature-card{{padding:40px;background:#ffffff;border-bottom:3px solid #d4af37;box-shadow:0 2px 8px rgba(0,0,0,0.04);transition:all 0.3s}}.feature-card:hover{{box-shadow:0 4px 15px rgba(0,0,0,0.08);transform:translateY(-3px)}}.feature-card .num{{font-size:56px;color:#d4af37;font-family:'Playfair Display',serif;font-weight:300;margin-bottom:15px}}.feature-card h3{{font-size:20px;font-weight:600;margin-bottom:15px;color:#1a1a1a}}.feature-card p{{font-size:14px;color:#777;line-height:1.8}}

.gallery-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:15px;margin-top:50px}}.gallery-item{{aspect-ratio:1;overflow:hidden;border-radius:2px;background:#e8e8e8;box-shadow:0 2px 8px rgba(0,0,0,0.08);transition:all 0.3s}}.gallery-item img{{width:100%;height:100%;object-fit:cover;transition:transform 0.3s}}.gallery-item:hover{{transform:scale(1.02);box-shadow:0 4px 15px rgba(0,0,0,0.12)}}

.cases-grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:15px;margin-top:50px}}.case-item{{aspect-ratio:1;overflow:hidden;border-radius:2px;background:#f0f0f0;box-shadow:0 2px 8px rgba(0,0,0,0.06);transition:all 0.3s}}.case-item img{{width:100%;height:100%;object-fit:cover;transition:transform 0.3s}}.case-item:hover{{transform:scale(1.03)}}

.flow-grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:20px;margin-top:50px}}.flow-step{{text-align:center;padding:20px}}.flow-step .num{{font-size:44px;color:#d4af37;font-family:'Playfair Display',serif;font-weight:300}}.flow-step h4{{font-size:14px;font-weight:600;margin:12px 0 8px;color:#1a1a1a}}.flow-step p{{font-size:12px;color:#888;line-height:1.6}}

.faq-section{{max-width:950px;margin:0 auto}}.faq-item{{margin:25px 0;padding:25px;background:#fafaf9;border-left:3px solid #d4af37;transition:all 0.3s}}.faq-item:hover{{background:#f5f5f5}}.faq-item h4{{font-size:15px;font-weight:600;color:#1a1a1a;margin-bottom:10px}}.faq-item p{{font-size:13px;color:#777;line-height:1.7}}

.pricing-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;margin-top:50px}}.price-card{{padding:45px 35px;background:#ffffff;border-bottom:3px solid #d4af37;box-shadow:0 2px 8px rgba(0,0,0,0.04);text-align:center;transition:all 0.3s}}.price-card:hover{{box-shadow:0 4px 15px rgba(0,0,0,0.08);transform:translateY(-3px)}}.price-card h3{{font-size:15px;font-weight:600;margin-bottom:12px;color:#1a1a1a}}.price-card .amount{{font-size:48px;color:#d4af37;font-family:'Playfair Display',serif;font-weight:300;margin:20px 0}}.price-card .note{{font-size:12px;color:#999}}

.cta{{background:#d4af37;color:#1a1a1a;padding:100px 40px;text-align:center;margin:80px 0;border-radius:0}}.cta h2{{font-size:48px;font-family:'Playfair Display',serif;font-weight:700;margin-bottom:20px}}.cta p{{font-size:16px;margin-bottom:40px;opacity:0.9}}

.footer{{background:#1a1a1a;color:#fff;padding:60px 40px;text-align:center}}.footer h2{{font-size:28px;font-family:'Playfair Display',serif;font-weight:700;margin-bottom:10px;color:#d4af37}}.footer p{{font-size:12px;color:#aaa;margin:8px 0}}

@media(max-width:1024px){{section{{padding:80px 30px}}.cases-grid{{grid-template-columns:repeat(3,1fr)}}.features-grid{{gap:25px}}.flow-grid{{grid-template-columns:repeat(3,1fr);gap:15px}}.pricing-grid{{grid-template-columns:repeat(2,1fr)}}.gallery-grid{{grid-template-columns:repeat(3,1fr)}}}}
@media(max-width:768px){{nav{{padding:15px 16px}}nav ul{{gap:15px}}.hero{{padding:60px 16px;min-height:60vh}}.hero h1{{font-size:48px}}.section{{padding:60px 16px}}.container{{padding:0}}.cases-grid{{grid-template-columns:repeat(2,1fr)}}.gallery-grid{{grid-template-columns:repeat(2,1fr)}}.pricing-grid{{grid-template-columns:1fr}}.features-grid{{grid-template-columns:1fr}}.flow-grid{{grid-template-columns:1fr}}}}
</style>
</head>
<body>

<nav>
  <div class="logo">Lovelier</div>
  <ul>
    <li><a href="#about">About</a></li>
    <li><a href="#features">特徴</a></li>
    <li><a href="#flow">治療の流れ</a></li>
    <li><a href="#cases">症例</a></li>
    <li><a href="#faq">Q&A</a></li>
    <li><a href="#pricing">価格</a></li>
    <li><a href="#booking" class="btn">予約</a></li>
  </ul>
</nav>

<section class="hero">
  <div class="hero-content">
    <div class="label">世界唯一の最先端技術</div>
    <h1>削らない<br>ジルコニアベニア<br>Lovelier</h1>
    <p class="sub">0.04mm最薄 × 完全無痛 × 最短3週間<br>YouTuber・ノアさんも体験した次世代審美治療</p>
    <a href="#booking" class="btn">無料カウンセリング予約</a>
  </div>
</section>

<section id="about">
  <div class="container">
    <div class="sec-title">
      <div class="label">About Lovelier</div>
      <h2>削らない理由</h2>
      <p>従来の審美治療は歯を削く必要でした。ラブリエは違います。</p>
    </div>
    <div class="intro-text">
      <strong>世界唯一の超薄加工技術</strong>で、ジルコニアを0.04mmまで仕上げることで、<strong>歯を削らずに完全な審美治療を実現します。</strong><br>痛みなし、ダメージなし、最短3週間で施術完了。人工ダイヤモンド級の強度で、半永久的に美しさを保ちます。
    </div>
  </div>
</section>

<section class="light" id="features">
  <div class="container">
    <div class="sec-title">
      <div class="label">Features</div>
      <h2>4つの特徴</h2>
    </div>
    <div class="features-grid">
      <div class="feature-card">
        <div class="num">01</div>
        <h3>最薄0.04mm<br>世界唯一</h3>
        <p>超薄加工技術により実現。削らずに前歯が出ない自然な仕上がりが完全に可能。従来のセラミック（0.3～0.5mm）の約10分の1。</p>
      </div>
      <div class="feature-card">
        <div class="num">02</div>
        <h3>完全無痛<br>削らない</h3>
        <p>歯を削りません。痛みもありません。健康な歯をそのまま保ちながら、完璧な審美性が得られます。将来的に外すことも容易です。</p>
      </div>
      <div class="feature-card">
        <div class="num">03</div>
        <h3>ダイヤモンド級<br>の強度</h3>
        <p>ジルコニアは人工ダイヤモンドに匹敵する強度。薄くても割れず、セラミックのように欠けることもありません。</p>
      </div>
      <div class="feature-card">
        <div class="num">04</div>
        <h3>完全自由な<br>色・形選択</h3>
        <p>自身の歯が透けないため、理想の色と形を完全に自由に選択できます。1本単位での治療も可能。完全オーダーメイド。</p>
      </div>
    </div>
  </div>
</section>

<section id="noa">
  <div class="container">
    <div class="sec-title">
      <div class="label">Experience</div>
      <h2>ノアさんが体験</h2>
      <p>YouTuber・ノアさんも実際に体験した次世代審美治療</p>
    </div>
    <div class="gallery-grid">
"""

for b64 in noa:
    html += f'      <div class="gallery-item"><img src="{b64}" alt=""></div>\n'

html += f"""    </div>
  </div>
</section>

<section class="light" id="flow">
  <div class="container">
    <div class="sec-title">
      <div class="label">Flow</div>
      <h2>治療の流れ</h2>
      <p>最短3週間で完成</p>
    </div>
    <div class="flow-grid">
      <div class="flow-step">
        <div class="num">❶</div>
        <h4>初診</h4>
        <p>カウンセリング・検査・撮影</p>
      </div>
      <div class="flow-step">
        <div class="num">❷</div>
        <h4>スキャン</h4>
        <p>精密スキャン・色選択・前処置</p>
      </div>
      <div class="flow-step">
        <div class="num">❸</div>
        <h4>デザイン</h4>
        <p>2～3週間でデザイン画像を確認</p>
      </div>
      <div class="flow-step">
        <div class="num">❹</div>
        <h4>セット</h4>
        <p>ラブリエをセット・色味調整</p>
      </div>
      <div class="flow-step">
        <div class="num">❺</div>
        <h4>検診</h4>
        <p>3ヶ月ごとのメンテナンス</p>
      </div>
    </div>
  </div>
</section>

<section id="cases">
  <div class="container">
    <div class="sec-title">
      <div class="label">Cases</div>
      <h2>実際の治療例</h2>
    </div>
    <div class="cases-grid">
"""

for b64 in cases[:20]:
    html += f'      <div class="case-item"><img src="{b64}" alt=""></div>\n'

html += f"""    </div>
  </div>
</section>

<section class="light" id="faq">
  <div class="container">
    <div class="sec-title">
      <div class="label">FAQ</div>
      <h2>よくある質問</h2>
    </div>
    <div class="faq-section">
      <div class="faq-item">
        <h4>本当に痛くないですか？</h4>
        <p>歯を削らないため、痛みはほぼありません。施術中も麻酔を使用するため、快適です。</p>
      </div>
      <div class="faq-item">
        <h4>セラミックとの違いは？</h4>
        <p>ラブリエは0.04mmで削らない。セラミックは0.3～0.5mmで削る必要があります。強度もラブリエが優れています。</p>
      </div>
      <div class="faq-item">
        <h4>どのくらい持ちますか？</h4>
        <p>人工ダイヤモンド級の強度で、適切なケアにより半永久的に。3年保証、10年延長保証も選択可能。</p>
      </div>
      <div class="faq-item">
        <h4>1本からできますか？</h4>
        <p>はい、1本からの治療が可能です。全顔改善にも対応しています。</p>
      </div>
      <div class="faq-item">
        <h4>外すことはできますか？</h4>
        <p>はい。歯を削っていないため、外すことが容易です。別の治療への変更も可能。</p>
      </div>
    </div>
  </div>
</section>

<section id="pricing">
  <div class="container">
    <div class="sec-title">
      <div class="label">Pricing</div>
      <h2>価格</h2>
    </div>
    <div class="pricing-grid">
      <div class="price-card">
        <h3>1本</h3>
        <div class="amount">¥79,000～<br>¥115,000</div>
        <div class="note">税抜・症例による</div>
      </div>
      <div class="price-card">
        <h3>全顔</h3>
        <div class="amount">¥1,264,000<br>～</div>
        <div class="note">税抜・16本以上</div>
      </div>
      <div class="price-card">
        <h3>保証</h3>
        <div class="amount">3年間<br>+¥22,000</div>
        <div class="note">10年延長保証</div>
      </div>
    </div>
  </div>
</section>

<section class="cta" id="booking">
  <h2>理想の笑顔へ</h2>
  <p>削らない、痛みなし。最短3週間で完成。</p>
  <a href="#" class="btn">無料カウンセリング予約</a>
</section>

<section class="footer">
  <h2>Lovelier</h2>
  <p>削らないジルコニアベニア 最先端審美治療</p>
  <p style="margin-top:20px;font-size:11px">名古屋ウィズ歯科・矯正歯科 / BF中日ビル歯科<br>© 2026 清翔会</p>
</section>

</body>
</html>
"""

with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Elegant Complete! {os.path.getsize(OUTPUT_HTML)/(1024*1024):.2f}MB")
