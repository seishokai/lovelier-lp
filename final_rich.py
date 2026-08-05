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

# ノアさん：4-5枚のみ（最高品質）
noa = []
noa_dir = r"C:\Users\USER\Downloads\lovelier_images\ラブリエ\ノアさん"
if os.path.exists(noa_dir):
    files = sorted(os.listdir(noa_dir))
    # 最高品質のみを選別（均等分散）
    step = len(files) // 4
    indices = [0, step, step*2, step*3]
    for idx in indices:
        if idx < len(files):
            f = files[idx]
            if f.endswith(('.jpg','.JPG')):
                noa.append(img_b64(os.path.join(noa_dir, f), size=1200, q=90))

# 症例画像：20枚以上
cases = []
cases_dir = r"C:\Users\USER\Downloads\lovelier_images\ラブリエ"
if os.path.exists(cases_dir):
    for d in sorted(os.listdir(cases_dir)):
        dp = os.path.join(cases_dir, d)
        if os.path.isdir(dp) and d not in ["ノアさん"]:
            for f in sorted(os.listdir(dp)):
                if f.endswith(('.jpg','.JPG')) and len(cases) < 25:
                    cases.append(img_b64(os.path.join(dp, f), size=900, q=85))

# ヒーロー画像：全部
hero = []
hero_dir = r"C:\Users\USER\Downloads\lovelier_hero_images\ラブリエイメージ"
if os.path.exists(hero_dir):
    for f in sorted(os.listdir(hero_dir))[:10]:
        if f.endswith(('.jpg','.JPG')):
            hero.append(img_b64(os.path.join(hero_dir, f), size=1200, q=85))

print(f"NOA: {len(noa)}, CASES: {len(cases)}, HERO: {len(hero)}")

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

nav{{position:fixed;top:0;width:100%;background:rgba(255,255,255,0.98);backdrop-filter:blur(10px);z-index:1000;padding:18px 40px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(212,175,55,0.1);box-shadow:0 2px 10px rgba(0,0,0,0.05)}}
nav .logo{{font-family:'Playfair Display',serif;font-size:26px;font-weight:700;color:#d4af37}}
nav ul{{display:flex;list-style:none;gap:35px}}
nav a{{color:#1a1a1a;font-size:12px;letter-spacing:0.1em;text-transform:uppercase;font-weight:600}}
nav a:hover{{color:#d4af37}}

.hero{{background:linear-gradient(135deg,rgba(0,0,0,0.25),rgba(0,0,0,0.15)),url('{noa[0] if noa else ''}');background-size:cover;background-position:center;background-attachment:fixed;min-height:100vh;display:flex;align-items:center;justify-content:center;color:#fff;text-align:center;padding:100px 20px;margin-top:60px;position:relative}}
.hero-content{{max-width:1000px;position:relative;z-index:2}}.hero .label{{font-size:13px;letter-spacing:0.3em;color:#d4af37;margin-bottom:30px;text-transform:uppercase;font-weight:700}}.hero h1{{font-size:96px;font-family:'Playfair Display',serif;font-weight:700;line-height:1.05;margin-bottom:35px;text-shadow:0 4px 20px rgba(0,0,0,0.25)}}.hero .sub{{font-size:22px;font-weight:300;line-height:1.9;margin-bottom:60px;opacity:0.98;text-shadow:0 2px 8px rgba(0,0,0,0.2)}}
.btn{{display:inline-block;background:#d4af37;color:#000;padding:16px 48px;font-size:12px;letter-spacing:0.2em;font-weight:700;margin:12px;cursor:pointer;border:2px solid #d4af37;border-radius:2px;text-transform:uppercase;transition:all 0.3s;box-shadow:0 4px 15px rgba(212,175,55,0.3)}}.btn:hover{{background:#fff;color:#d4af37;box-shadow:0 8px 30px rgba(212,175,55,0.4)}}
.btn-outline{{background:transparent;color:#ffffff;border-color:#ffffff}}.btn-outline:hover{{background:#ffffff;color:#d4af37}}

section{{padding:120px 0}}section.light{{background:#fafaf9}}
.container{{max-width:1400px;margin:0 auto;padding:0 40px}}

.sec-title{{text-align:center;padding:80px 20px 50px}}.sec-title .label{{font-size:12px;letter-spacing:0.35em;color:#d4af37;margin-bottom:18px;text-transform:uppercase;font-weight:700}}.sec-title h2{{font-size:56px;font-family:'Playfair Display',serif;font-weight:700;margin-bottom:25px;color:#1a1a1a}}.sec-title p{{font-size:16px;color:#666;max-width:800px;margin:0 auto;line-height:1.8}}
.bar{{width:80px;height:3px;background:linear-gradient(90deg,transparent,#d4af37,transparent);margin:20px auto 0}}

.intro-text{{max-width:1000px;margin:60px auto;text-align:center;font-size:17px;color:#555;line-height:2.1}}
.intro-text strong{{color:#d4af37;font-weight:700}}

.features-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:50px;margin-top:70px}}.feature-card{{padding:50px 40px;background:#ffffff;border:2px solid rgba(212,175,55,0.2);border-radius:4px;box-shadow:0 4px 15px rgba(0,0,0,0.06);transition:all 0.4s}}.feature-card:hover{{border-color:#d4af37;box-shadow:0 8px 30px rgba(212,175,55,0.15);transform:translateY(-5px)}}.feature-card .num{{font-size:72px;color:#d4af37;font-family:'Playfair Display',serif;font-weight:300;margin-bottom:20px}}.feature-card h3{{font-size:24px;font-weight:600;margin-bottom:18px;color:#1a1a1a;line-height:1.3}}.feature-card p{{font-size:15px;color:#666;line-height:1.9}}

.gallery-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:60px}}.gallery-item{{aspect-ratio:1;overflow:hidden;border-radius:4px;background:#e8e8e8;box-shadow:0 4px 15px rgba(0,0,0,0.1);transition:all 0.4s}}.gallery-item img{{width:100%;height:100%;object-fit:cover;transition:transform 0.4s}}.gallery-item:hover{{box-shadow:0 8px 30px rgba(0,0,0,0.15);transform:scale(1.02)}}

.cases-grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:18px;margin-top:60px}}.case-item{{aspect-ratio:1;overflow:hidden;border-radius:4px;background:#f0f0f0;box-shadow:0 4px 15px rgba(0,0,0,0.08);transition:all 0.3s}}.case-item img{{width:100%;height:100%;object-fit:cover;transition:transform 0.3s}}.case-item:hover{{box-shadow:0 8px 25px rgba(0,0,0,0.12);transform:scale(1.03)}}

.flow-grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:25px;margin-top:60px}}.flow-step{{text-align:center;padding:25px}}.flow-step .num{{font-size:52px;color:#d4af37;font-family:'Playfair Display',serif;font-weight:300;line-height:1}}.flow-step h4{{font-size:15px;font-weight:600;margin:15px 0 10px;color:#1a1a1a}}.flow-step p{{font-size:13px;color:#777;line-height:1.7}}

.faq-item{{margin:35px 0;padding:30px;background:#fafaf9;border-left:5px solid #d4af37;border-radius:2px;transition:all 0.3s}}.faq-item:hover{{background:#f5f5f5;box-shadow:0 4px 15px rgba(0,0,0,0.05)}}.faq-item h4{{font-size:16px;font-weight:600;color:#1a1a1a;margin-bottom:12px}}.faq-item p{{font-size:14px;color:#666;line-height:1.8}}

.pricing-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin-top:70px}}.price-card{{padding:50px 40px;background:#ffffff;border:2px solid rgba(212,175,55,0.2);border-radius:4px;text-align:center;box-shadow:0 4px 15px rgba(0,0,0,0.06);transition:all 0.4s}}.price-card:hover{{border-color:#d4af37;box-shadow:0 8px 30px rgba(212,175,55,0.15);transform:translateY(-8px)}}.price-card h3{{font-size:16px;font-weight:600;margin-bottom:15px;color:#1a1a1a}}.price-card .amount{{font-size:56px;color:#d4af37;font-family:'Playfair Display',serif;font-weight:300;margin:25px 0}}.price-card .note{{font-size:12px;color:#999;line-height:1.7}}

.comparison-table{{width:100%;margin-top:60px;border-collapse:collapse}}.comparison-table th,.comparison-table td{{padding:20px;text-align:left;border-bottom:1px solid rgba(0,0,0,0.1)}}.comparison-table th{{background:#fafaf9;font-weight:600;color:#1a1a1a}}.comparison-table td{{font-size:14px;color:#666}}.comparison-table tr:hover{{background:#fafaf9}}

.guarantee-section{{margin-top:60px;padding:50px 40px;background:#fafaf9;border-radius:4px;border-left:5px solid #d4af37}}.guarantee-section h3{{font-size:22px;font-weight:600;margin-bottom:25px;color:#1a1a1a}}.guarantee-items{{display:grid;grid-template-columns:repeat(2,1fr);gap:30px}}.guarantee-item{{padding:20px}}.guarantee-item h4{{font-size:15px;font-weight:600;color:#d4af37;margin-bottom:10px}}.guarantee-item p{{font-size:14px;color:#666;line-height:1.7}}

.cta-section{{background:linear-gradient(135deg,#d4af37,#e8c258);color:#000;padding:120px 40px;text-align:center;border-radius:4px;margin:80px 0}}.cta-section h2{{font-size:52px;font-family:'Playfair Display',serif;font-weight:700;margin-bottom:25px}}.cta-section p{{font-size:18px;margin-bottom:50px;opacity:0.95}}

.footer{{background:#1a1a1a;color:#fff;padding:80px 40px;text-align:center;border-top:1px solid rgba(212,175,55,0.2)}}.footer h2{{font-size:32px;font-family:'Playfair Display',serif;font-weight:700;margin-bottom:15px;color:#d4af37}}.footer p{{font-size:13px;color:#aaa;margin:10px 0}}

@media(max-width:1200px){{.container{{padding:0 30px}}.cases-grid{{grid-template-columns:repeat(4,1fr)}}.gallery-grid{{grid-template-columns:repeat(3,1fr)}}.features-grid{{gap:30px}}.flow-grid{{grid-template-columns:repeat(3,1fr);gap:15px}}.guarantee-items{{grid-template-columns:1fr}}}}
@media(max-width:768px){{nav{{padding:12px 16px}}nav ul{{gap:12px;font-size:10px}}.hero{{padding:60px 16px;margin-top:50px;min-height:60vh}}.hero h1{{font-size:52px}}.container{{padding:0 16px}}section{{padding:80px 0}}.cases-grid{{grid-template-columns:repeat(2,1fr)}}.gallery-grid{{grid-template-columns:repeat(2,1fr)}}.pricing-grid{{grid-template-columns:1fr}}.features-grid{{grid-template-columns:1fr}}.flow-grid{{grid-template-columns:1fr}}.sec-title h2{{font-size:40px}}.hero .sub{{font-size:16px}}}}
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
    <li><a href="#guarantee">保証</a></li>
    <li><a href="#pricing">価格</a></li>
    <li><a href="#booking" class="btn">予約</a></li>
  </ul>
</nav>

<section class="hero">
  <div class="hero-content">
    <div class="label">世界唯一の最先端技術</div>
    <h1>削らない<br>ジルコニアベニア<br><span style="color:#d4af37;">Lovelier</span></h1>
    <p class="sub">0.04mm最薄 × 人工ダイヤモンド級の強度 × 完全無痛<br>YouTuber・ノアさんも体験した次世代審美治療<br>最短3週間で理想の笑顔へ</p>
    <a href="#booking" class="btn">無料カウンセリング予約</a>
    <a href="#features" class="btn btn-outline">詳しく見る</a>
  </div>
</section>

<section id="about">
  <div class="container">
    <div class="sec-title">
      <div class="label">About Lovelier</div>
      <h2>ラブリエについて</h2>
      <p>世界で唯一、0.04mmの超薄加工技術により、歯を削らずに完璧な審美治療を実現します</p>
      <div class="bar"></div>
    </div>
    <div class="intro-text">
      従来のセラミックやラミネートベニアは、歯を削く必要がありました。しかし、<strong>ラブリエは違います。</strong><br><br>
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
        <p>世界でも唯一無二の超薄加工技術により、わずか0.04mmの厚さを実現。従来のセラミック（0.3～0.5mm）と比較して約10分の1の薄さです。削らずに前歯が出ない自然な仕上がりを完全に実現できます。</p>
      </div>
      <div class="feature-card">
        <div class="num">02</div>
        <h3>完全無痛<br>歯を削らない</h3>
        <p>歯を削りません。痛みもありません。健康な歯をそのまま保ちながら、完璧な審美性を手に入れることができます。将来的に外す必要が生じても、元の歯に戻すことが可能です。</p>
      </div>
      <div class="feature-card">
        <div class="num">03</div>
        <h3>人工ダイヤモンド級<br>の強度</h3>
        <p>ジルコニア素材は人工ダイヤモンドに匹敵する強度を持ちます。薄くても割れず、セラミックのように欠けることもありません。食いしばりが強い方でも安心です。</p>
      </div>
      <div class="feature-card">
        <div class="num">04</div>
        <h3>完全自由な<br>色・形選択</h3>
        <p>自身の歯が透けないため、理想の色と形を完全に自由に選択できます。1本単位での治療も可能。全顔改善にも対応。完全オーダーメイドの笑顔をデザインします。</p>
      </div>
    </div>
  </div>
</section>

<section id="noa">
  <div class="container">
    <div class="sec-title">
      <div class="label">NOA Experience</div>
      <h2>ノアさんが体験したラブリエ</h2>
      <p>YouTuber・ノアさんも実際に体験。削らない・痛みほぼゼロの次世代審美治療</p>
      <div class="bar"></div>
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
      <div class="label">Treatment Flow</div>
      <h2>治療の流れ</h2>
      <p>初診から施術完了まで、最短3週間の流れ</p>
      <div class="bar"></div>
    </div>
    <div class="flow-grid">
      <div class="flow-step">
        <div class="num">❶</div>
        <h4>初診・カウンセリング</h4>
        <p>口腔内検査・写真撮影・レントゲン・理想のデザインを相談</p>
      </div>
      <div class="flow-step">
        <div class="num">❷</div>
        <h4>前処置・スキャン</h4>
        <p>虫歯・欠けの治療（保険内）。精密スキャンで3D設計</p>
      </div>
      <div class="flow-step">
        <div class="num">❸</div>
        <h4>デザイン確認</h4>
        <p>2～3週間でデザイン画像をお送り。修正も可能</p>
      </div>
      <div class="flow-step">
        <div class="num">❹</div>
        <h4>ラブリエセット</h4>
        <p>セット当日も色味調整可能。快適な装着感</p>
      </div>
      <div class="flow-step">
        <div class="num">❺</div>
        <h4>定期検診</h4>
        <p>3ヶ月ごとのメンテナンス推奨。美しさを永く保つ</p>
      </div>
    </div>
  </div>
</section>

<section id="cases">
  <div class="container">
    <div class="sec-title">
      <div class="label">Treatment Cases</div>
      <h2>実際の治療例</h2>
      <p>多くの患者様がラブリエで理想の笑顔を実現</p>
      <div class="bar"></div>
    </div>
    <div class="cases-grid">
"""

for b64 in cases[:25]:
    html += f'      <div class="case-item"><img src="{b64}" alt=""></div>\n'

html += f"""    </div>
  </div>
</section>

<section class="light" id="comparison">
  <div class="container">
    <div class="sec-title">
      <div class="label">Comparison</div>
      <h2>セラミック・ラミネートとの比較</h2>
      <div class="bar"></div>
    </div>
    <table class="comparison-table">
      <tr>
        <th>項目</th>
        <th>従来型セラミック</th>
        <th>ラミネート（従来）</th>
        <th>ラブリエ</th>
      </tr>
      <tr>
        <td><strong>厚さ</strong></td>
        <td>0.3～0.5mm</td>
        <td>0.5～1.0mm</td>
        <td>0.04mm～</td>
      </tr>
      <tr>
        <td><strong>削除量</strong></td>
        <td>多い（コア削除）</td>
        <td>少ない</td>
        <td>ほぼ0</td>
      </tr>
      <tr>
        <td><strong>痛み</strong></td>
        <td>あり（麻酔必要）</td>
        <td>ほぼなし</td>
        <td>ほぼなし</td>
      </tr>
      <tr>
        <td><strong>治療期間</strong></td>
        <td>2-3ヶ月</td>
        <td>2-3週間</td>
        <td>3週間</td>
      </tr>
      <tr>
        <td><strong>強度</strong></td>
        <td>中程度</td>
        <td>中程度</td>
        <td>◎◎ダイヤモンド級</td>
      </tr>
      <tr>
        <td><strong>色選択</strong></td>
        <td>透光性重視</td>
        <td>限定的</td>
        <td>完全自由</td>
      </tr>
      <tr>
        <td><strong>可逆性</strong></td>
        <td>困難</td>
        <td>容易</td>
        <td>容易</td>
      </tr>
    </table>
  </div>
</section>

<section id="faq">
  <div class="container">
    <div class="sec-title">
      <div class="label">FAQ</div>
      <h2>よくある質問</h2>
      <div class="bar"></div>
    </div>
    <div style="max-width:1000px;margin:0 auto;">
      <div class="faq-item">
        <h4>Q. 本当に痛くないですか？</h4>
        <p>A. 歯を削りませんので、痛みはほぼありません。施術中も麻酔を使用するため、快適な状態で治療を受けられます。削らないため、知覚過敏の心配もありません。</p>
      </div>
      <div class="faq-item">
        <h4>Q. 治療期間はどのくらい？</h4>
        <p>A. 初回カウンセリングから施術完了まで最短3週間です。スキャン・デザイン確認・セットのプロセスで迅速に実現できます。急ぎの場合はご相談ください。</p>
      </div>
      <div class="faq-item">
        <h4>Q. セラミックとの大きな違いは？</h4>
        <p>A. ラブリエは0.04mmの超薄設計で歯を削りません。セラミックは0.3～0.5mm必要で、歯を大きく削る必要があります。強度もラブリエが優れており、処置後の知覚過敏もほぼありません。</p>
      </div>
      <div class="faq-item">
        <h4>Q. どのくらい持ちますか？</h4>
        <p>A. 人工ダイヤモンド級の強度で、適切なケアにより半永久的に美しさを保ちます。3年間の標準保証付き、さらに10年延長保証も選択可能です。</p>
      </div>
      <div class="faq-item">
        <h4>Q. 1本からできますか？</h4>
        <p>A. はい、1本からの治療が可能です。部分的な改善もできますし、全顔改善（16本以上）を希望される場合もモニター価格でご対応しています。</p>
      </div>
      <div class="faq-item">
        <h4>Q. 外すことはできますか？</h4>
        <p>A. はい。歯を削っていないため、外すことが容易です。将来的に別の治療に変更することも可能です。これが大きなメリットです。</p>
      </div>
      <div class="faq-item">
        <h4>Q. 食事制限はありますか？</h4>
        <p>A. ほぼありません。ジルコニアの高い強度により、通常通りの食事が可能です。ただし極度に硬いものは避けていただくことをお勧めします。</p>
      </div>
      <div class="faq-item">
        <h4>Q. 他院で削られている場合は？</h4>
        <p>A. 既に削られている場合も、ラブリエで対応可能です。詳しくはカウンセリングでご相談ください。</p>
      </div>
    </div>
  </div>
</section>

<section class="light" id="guarantee">
  <div class="container">
    <div class="sec-title">
      <div class="label">Guarantee</div>
      <h2>ラブリエの保証</h2>
      <p>長期的に美しさを保つための充実した保証制度</p>
      <div class="bar"></div>
    </div>
    <div class="guarantee-section">
      <h3>3年間の標準保証</h3>
      <div class="guarantee-items">
        <div class="guarantee-item">
          <h4>✓ 破損・脱落保証</h4>
          <p>正常な使用範囲での破損・脱落は無償で再製作します。</p>
        </div>
        <div class="guarantee-item">
          <h4>✓ 定期検診</h4>
          <p>3ヶ月ごとのメンテナンス・クリーニングで美しさを維持。</p>
        </div>
        <div class="guarantee-item">
          <h4>✓ 調整費無料</h4>
          <p>セット後の色味・形態調整は無料で対応します。</p>
        </div>
        <div class="guarantee-item">
          <h4>✓ 知覚過敏対応</h4>
          <p>万が一知覚過敏が発生した場合も対応いたします。</p>
        </div>
      </div>
      <div style="margin-top:40px;padding-top:30px;border-top:2px solid rgba(212,175,55,0.2);">
        <h3>10年延長保証（+¥22,000/本）</h3>
        <p style="color:#666;margin-top:15px;">3年の標準保証に加えて、さらに10年まで延長保証が可能です。長期的な投資として、安心の保証システムです。</p>
      </div>
    </div>
  </div>
</section>

<section id="pricing">
  <div class="container">
    <div class="sec-title">
      <div class="label">Pricing</div>
      <h2>価格について</h2>
      <p>透明でわかりやすい料金体系</p>
      <div class="bar"></div>
    </div>
    <div class="pricing-grid">
      <div class="price-card">
        <h3>ラブリエ（1本）</h3>
        <div class="amount">¥79,000～<br>¥115,000</div>
        <div class="note">税抜・症例による<br>前歯1本単位</div>
      </div>
      <div class="price-card">
        <h3>全顔モニター</h3>
        <div class="amount">¥1,264,000<br>～</div>
        <div class="note">税抜・16本以上<br>大幅割引あり</div>
      </div>
      <div class="price-card">
        <h3>延長保証</h3>
        <div class="amount">+¥22,000<br>/ 本</div>
        <div class="note">3年→10年間<br>標準保証から追加</div>
      </div>
    </div>
  </div>
</section>

<section class="cta-section" id="booking">
  <h2>理想の笑顔へ</h2>
  <p>削らない、痛みなし。最短3週間で完成。<br>世界で一つだけのあなたの笑顔を。</p>
  <a href="#" class="btn" style="background:#000;color:#d4af37;border-color:#000;padding:18px 52px;font-size:14px">無料カウンセリング予約</a>
</section>

<footer class="footer">
  <h2>Lovelier</h2>
  <p>削らないジルコニアベニア 最先端審美治療</p>
  <p style="margin-top:25px;font-size:12px">名古屋ウィズ歯科・矯正歯科 / BF中日ビル歯科<br>© 2026 清翔会</p>
</footer>

</body>
</html>
"""

with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Final Rich Complete! {os.path.getsize(OUTPUT_HTML)/(1024*1024):.2f}MB")
