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

# ノアさん画像：バリエーション豊かに 10 枚選別
noa = []
noa_dir = r"C:\Users\USER\Downloads\lovelier_images\ラブリエ\ノアさん"
if os.path.exists(noa_dir):
    files = sorted(os.listdir(noa_dir))
    # 均等に分散して選ぶ（先頭・中盤・後半から選別）
    indices = [0, 2, 4, 6, 8, 10, 12, 14, 1, 3][:10]
    for idx in indices:
        if idx < len(files):
            f = files[idx]
            if f.endswith(('.jpg','.JPG')):
                noa.append(img_b64(os.path.join(noa_dir, f), size=1200, q=85))

# 症例画像：最初の 12 枚
cases = []
cases_dir = r"C:\Users\USER\Downloads\lovelier_images\ラブリエ"
if os.path.exists(cases_dir):
    for d in sorted(os.listdir(cases_dir)):
        dp = os.path.join(cases_dir, d)
        if os.path.isdir(dp) and d not in ["ノアさん"]:
            for f in sorted(os.listdir(dp)):
                if f.endswith(('.jpg','.JPG')) and len(cases) < 12:
                    cases.append(img_b64(os.path.join(dp, f), size=900, q=85))

# ヒーロー画像：5 枚
hero = []
hero_dir = r"C:\Users\USER\Downloads\lovelier_hero_images\ラブリエイメージ"
if os.path.exists(hero_dir):
    for f in sorted(os.listdir(hero_dir))[:5]:
        if f.endswith(('.jpg','.JPG')):
            hero.append(img_b64(os.path.join(hero_dir, f), size=1200, q=85))

print(f"NOA: {len(noa)}, CASES: {len(cases)}, HERO: {len(hero)}")

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lovelier | 削らないジルコニアベニア × YouTuber ノア</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Noto+Serif+JP:wght@200;300;400;500;600&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}html{{scroll-behavior:smooth}}
body{{font-family:'Noto Serif JP',serif;background:#ffffff;color:#1a1a1a;line-height:1.8;overflow-x:hidden}}
img{{max-width:100%;height:auto;display:block}}a{{text-decoration:none;transition:all 0.3s}}

/* Navigation */
nav{{position:fixed;top:0;width:100%;background:rgba(255,255,255,0.98);backdrop-filter:blur(10px);z-index:1000;padding:20px 40px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(212,175,55,0.1);box-shadow:0 2px 10px rgba(0,0,0,0.05)}}
nav .logo{{font-family:'Playfair Display',serif;font-size:26px;font-weight:700;color:#d4af37}}
nav ul{{display:flex;list-style:none;gap:40px}}
nav a{{color:#1a1a1a;font-size:13px;letter-spacing:0.1em;text-transform:uppercase;position:relative;font-weight:500}}
nav a:hover{{color:#d4af37}}

/* Hero */
.hero{{background:linear-gradient(135deg,rgba(0,0,0,0.3),rgba(0,0,0,0.2)),url('{noa[0] if noa else ''}');background-size:cover;background-position:center;background-attachment:fixed;min-height:100vh;display:flex;align-items:center;justify-content:center;color:#fff;text-align:center;padding:100px 20px;margin-top:60px;position:relative}}
.hero-content{{max-width:900px;position:relative;z-index:2}}.hero .label{{font-size:12px;letter-spacing:0.3em;color:#d4af37;margin-bottom:25px;text-transform:uppercase;font-weight:600}}.hero h1{{font-size:84px;font-family:'Playfair Display',serif;font-weight:700;line-height:1.1;margin-bottom:30px;text-shadow:0 4px 20px rgba(0,0,0,0.3)}}.hero .sub{{font-size:20px;font-weight:300;line-height:1.8;margin-bottom:50px;opacity:0.98;text-shadow:0 2px 8px rgba(0,0,0,0.2)}}
.btn{{display:inline-block;background:#d4af37;color:#000;padding:16px 48px;font-size:12px;letter-spacing:0.2em;font-weight:700;margin:12px;cursor:pointer;border:2px solid #d4af37;border-radius:2px;text-transform:uppercase;transition:all 0.3s;box-shadow:0 4px 15px rgba(212,175,55,0.3)}}.btn:hover{{background:#fff;color:#d4af37;box-shadow:0 8px 25px rgba(212,175,55,0.4)}}
.btn-outline{{background:transparent;color:#ffffff;border-color:#ffffff;box-shadow:0 4px 15px rgba(255,255,255,0.2)}}.btn-outline:hover{{background:#ffffff;color:#d4af37}}

/* Sections */
section{{padding:120px 0}}section.light{{background:#fafaf9}}
.container{{max-width:1300px;margin:0 auto;padding:0 40px}}

.sec-title{{text-align:center;padding:60px 20px 40px}}.sec-title .label{{font-size:11px;letter-spacing:0.35em;color:#d4af37;margin-bottom:15px;text-transform:uppercase;font-weight:700}}.sec-title h2{{font-size:52px;font-family:'Playfair Display',serif;font-weight:700;margin-bottom:20px;color:#1a1a1a}}.sec-title .bar{{width:80px;height:3px;background:linear-gradient(90deg,transparent,#d4af37,transparent);margin:0 auto}}

/* Intro Text */
.intro-text{{max-width:900px;margin:60px auto;text-align:center;font-size:17px;color:#555;line-height:2.1}}
.intro-text strong{{color:#d4af37;font-weight:700}}

/* Features Grid */
.features-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:50px;margin-top:60px}}.feature-card{{padding:50px 40px;background:#ffffff;border:2px solid rgba(212,175,55,0.2);border-radius:4px;box-shadow:0 4px 15px rgba(0,0,0,0.06);transition:all 0.4s}}.feature-card:hover{{border-color:#d4af37;box-shadow:0 8px 30px rgba(212,175,55,0.15);transform:translateY(-5px)}}.feature-card .num{{font-size:64px;color:#d4af37;font-family:'Playfair Display',serif;font-weight:300;margin-bottom:15px}}.feature-card h3{{font-size:22px;font-weight:600;margin-bottom:18px;color:#1a1a1a;line-height:1.4}}.feature-card p{{font-size:15px;color:#666;line-height:1.9}}

/* Gallery */
.gallery-grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:20px;margin-top:60px}}.gallery-item{{aspect-ratio:1;overflow:hidden;border-radius:4px;background:#e8e8e8;box-shadow:0 4px 15px rgba(0,0,0,0.1);transition:all 0.4s}}.gallery-item img{{width:100%;height:100%;object-fit:cover;transition:transform 0.4s}}.gallery-item:hover{{box-shadow:0 8px 30px rgba(0,0,0,0.15);transform:scale(1.02)}}

/* Cases Grid */
.cases-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:25px;margin-top:60px}}.case-item{{aspect-ratio:1;overflow:hidden;border-radius:4px;background:#f0f0f0;box-shadow:0 4px 15px rgba(0,0,0,0.08);transition:all 0.3s}}.case-item img{{width:100%;height:100%;object-fit:cover;transition:transform 0.3s}}.case-item:hover{{box-shadow:0 8px 25px rgba(0,0,0,0.12);transform:scale(1.03)}}

/* Treatment Flow */
.flow-grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:30px;margin-top:60px}}.flow-step{{text-align:center}}.flow-step .num{{font-size:48px;color:#d4af37;font-family:'Playfair Display',serif;font-weight:300;line-height:1}}.flow-step h4{{font-size:16px;font-weight:600;margin:15px 0 10px;color:#1a1a1a}}.flow-step p{{font-size:13px;color:#777;line-height:1.7}}

/* FAQ */
.faq-item{{margin:30px 0;padding:25px;background:#fafaf9;border-left:4px solid #d4af37;border-radius:2px;transition:all 0.3s}}.faq-item:hover{{background:#f5f5f5;box-shadow:0 4px 15px rgba(0,0,0,0.05)}}.faq-item h4{{font-size:16px;font-weight:600;color:#1a1a1a;margin-bottom:12px}}.faq-item p{{font-size:14px;color:#666;line-height:1.8}}

/* Pricing */
.pricing-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin-top:60px}}.price-card{{padding:50px 40px;background:#ffffff;border:2px solid rgba(212,175,55,0.2);border-radius:4px;text-align:center;box-shadow:0 4px 15px rgba(0,0,0,0.06);transition:all 0.4s}}.price-card:hover{{border-color:#d4af37;box-shadow:0 8px 30px rgba(212,175,55,0.15);transform:translateY(-8px)}}.price-card h3{{font-size:16px;font-weight:600;margin-bottom:15px;color:#1a1a1a}}.price-card .amount{{font-size:52px;color:#d4af37;font-family:'Playfair Display',serif;font-weight:300;margin:20px 0}}.price-card .note{{font-size:12px;color:#999;line-height:1.6}}

/* CTA Section */
.cta-section{{background:linear-gradient(135deg,#d4af37,#e8c258);color:#000;padding:100px 40px;text-align:center;border-radius:4px;margin:60px 0}}.cta-section h2{{font-size:48px;font-family:'Playfair Display',serif;font-weight:700;margin-bottom:20px}}.cta-section p{{font-size:16px;margin-bottom:40px;opacity:0.95}}

/* Footer */
.footer{{background:#1a1a1a;color:#fff;padding:60px 40px;text-align:center;border-top:1px solid rgba(212,175,55,0.2)}}.footer h2{{font-size:32px;font-family:'Playfair Display',serif;font-weight:700;margin-bottom:10px;color:#d4af37}}.footer p{{font-size:12px;color:#aaa;margin:8px 0}}

@media(max-width:1200px){{.container{{padding:0 30px}}.gallery-grid{{grid-template-columns:repeat(4,1fr)}}.cases-grid{{grid-template-columns:repeat(3,1fr)}}.features-grid{{gap:30px}}.flow-grid{{grid-template-columns:repeat(3,1fr);gap:20px}}}}
@media(max-width:768px){{nav{{padding:15px 16px}}nav ul{{gap:15px;font-size:11px}}.hero{{margin-top:50px;padding:60px 16px;min-height:60vh}}.hero h1{{font-size:48px}}.container{{padding:0 16px}}section{{padding:80px 0}}.gallery-grid{{grid-template-columns:repeat(2,1fr)}}.cases-grid{{grid-template-columns:repeat(2,1fr)}}.pricing-grid{{grid-template-columns:1fr}}.features-grid{{grid-template-columns:1fr}}.flow-grid{{grid-template-columns:1fr}}.sec-title h2{{font-size:36px}}.feature-card,.price-card{{padding:30px 20px}}}}
</style>
</head>
<body>

<nav>
  <div class="logo">Lovelier</div>
  <ul>
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
    <h1>削らない<br>ジルコニアベニア<br><span style="color:#d4af37;">Lovelier</span></h1>
    <p class="sub">0.04mm最薄 × 人工ダイヤモンド級の強度 × 完全無痛<br>YouTuber・ノアさんも体験した<br>次世代審美治療</p>
    <a href="#booking" class="btn">無料カウンセリング予約</a>
    <a href="#features" class="btn btn-outline">詳しく見る</a>
  </div>
</section>

<section>
  <div class="container">
    <div class="sec-title">
      <div class="label">About Lovelier</div>
      <h2>ラブリエについて</h2>
      <div class="bar"></div>
    </div>
    <div class="intro-text">
      従来の審美治療は、歯を大きく削く必要がありました。しかし、<strong>ラブリエは違います。</strong><br><br>
      <strong>世界でも唯一無二の超薄加工技術</strong>で、最高強度のジルコニアを<strong>0.04mmまで薄く仕上げることで、歯を削らずに完全な審美治療を実現します。</strong><br><br>
      痛みなし、歯へのダメージなし、最短3週間で施術完了。人工ダイヤモンド級の強度で、<strong>半永久的に美しさを保つことができます。</strong>
    </div>
  </div>
</section>

<section class="light" id="features">
  <div class="container">
    <div class="sec-title">
      <div class="label">Four Features</div>
      <h2>ラブリエの特徴</h2>
      <div class="bar"></div>
    </div>
    <div class="features-grid">
      <div class="feature-card">
        <div class="num">01</div>
        <h3>最薄0.04mm<br>（世界唯一）</h3>
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
        <p>自身の歯が透けないため、理想の色と形を完全に自由に選択できます。1本単位での治療も可能。完全オーダーメイド。</p>
      </div>
    </div>
  </div>
</section>

<section id="noa">
  <div class="container">
    <div class="sec-title">
      <div class="label">NOA Experience</div>
      <h2>ノアさんが体験したラブリエ</h2>
      <div class="bar"></div>
    </div>
    <p class="intro-text">
      YouTuber・ノアさんも実際に体験。<strong>「削らない・痛みほぼゼロ」</strong>の次世代審美治療が実現できます。
    </p>
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
      <div class="label">Treatment Flow</div>
      <h2>治療の流れ</h2>
      <div class="bar"></div>
    </div>
    <div class="flow-grid">
      <div class="flow-step">
        <div class="num">❶</div>
        <h4>無料カウンセリング</h4>
        <p>口腔内・顔貌・レントゲン写真でカウンセリング</p>
      </div>
      <div class="flow-step">
        <div class="num">❷</div>
        <h4>精密スキャン<br>色調選択</h4>
        <p>虫歯や欠けがあれば事前治療（保険内）</p>
      </div>
      <div class="flow-step">
        <div class="num">❸</div>
        <h4>デザイン確認</h4>
        <p>2～3週間でデザイン画像をお送り</p>
      </div>
      <div class="flow-step">
        <div class="num">❹</div>
        <h4>ラブリエセット</h4>
        <p>セット当日も色味調整可能</p>
      </div>
      <div class="flow-step">
        <div class="num">❺</div>
        <h4>定期検診</h4>
        <p>3ヶ月ごとのメンテナンス推奨</p>
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

for i, b64 in enumerate(cases[:12], 1):
    html += f'      <div class="case-item"><img src="{b64}" alt=""></div>\n'

html += f"""    </div>
  </div>
</section>

<section class="light" id="faq">
  <div class="container">
    <div class="sec-title">
      <div class="label">FAQ</div>
      <h2>よくある質問</h2>
      <div class="bar"></div>
    </div>
    <div style="max-width:900px;margin:0 auto;">
      <div class="faq-item">
        <h4>Q. 本当に痛くないですか？</h4>
        <p>A. 歯を削りませんので、痛みはほぼありません。施術中も麻酔を使用するため、快適な状態で治療を受けられます。</p>
      </div>
      <div class="faq-item">
        <h4>Q. 治療期間はどのくらい？</h4>
        <p>A. 初回カウンセリングから施術完了まで最短3週間です。スキャン・デザイン確認・セットのプロセスで実現できます。</p>
      </div>
      <div class="faq-item">
        <h4>Q. セラミックとの違いは？</h4>
        <p>A. ラブリエは0.04mmの超薄設計で歯を削りません。セラミックは0.3～0.5mmの厚さが必要で、歯を削る必要があります。強度もラブリエの方が優れています。</p>
      </div>
      <div class="faq-item">
        <h4>Q. どのくらい持ちますか？</h4>
        <p>A. 人工ダイヤモンド級の強度で、適切なケアにより半永久的に美しさを保ちます。3年間の保証付き、さらに10年延長保証も選択可能です。</p>
      </div>
      <div class="faq-item">
        <h4>Q. 1本からできますか？</h4>
        <p>A. はい、1本からの治療が可能です。部分的な改善もできますし、全顔改善を希望される場合も対応しています。</p>
      </div>
    </div>
  </div>
</section>

<section id="pricing">
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
        <div class="note">税抜<br>症例による</div>
      </div>
      <div class="price-card">
        <h3>全顔モニター</h3>
        <div class="amount">¥1,264,000<br>～</div>
        <div class="note">税抜<br>16本以上</div>
      </div>
      <div class="price-card">
        <h3>保証</h3>
        <div class="amount">3年間<br>+¥22,000</div>
        <div class="note">10年延長保証<br>1本単位</div>
      </div>
    </div>
  </div>
</section>

<section class="cta-section" id="booking">
  <h2>理想の笑顔へ</h2>
  <p>削らない、痛みなし。最短3週間で完成。<br>世界で一つだけのあなたの笑顔を。</p>
  <a href="#" class="btn" style="background:#000;color:#d4af37;border-color:#000;box-shadow:0 4px 15px rgba(0,0,0,0.3)">無料カウンセリング予約</a>
</section>

<footer class="footer">
  <h2>Lovelier</h2>
  <p>削らないジルコニアベニア 最先端審美治療</p>
  <p style="margin-top:20px;font-size:11px">名古屋ウィズ歯科・矯正歯科 / BF中日ビル歯科<br>© 2026 清翔会</p>
</footer>

</body>
</html>
"""

with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"White Premium Complete! {os.path.getsize(OUTPUT_HTML)/(1024*1024):.2f}MB")
