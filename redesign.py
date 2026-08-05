#!/usr/bin/env python3
"""
Lovelier LP - 全面リニューアル（20項目実装ガイド準拠）
ネイビー×ゴールド、Apple/Stripe/Linear風の高級感
"""
import base64, os
from PIL import Image, ImageOps
from io import BytesIO

OUTPUT_HTML = r"C:\Users\USER\lovelier-lp\index.html"
NOA_DIR = r"C:\Users\USER\Downloads\lovelier_images\ラブリエ\ノアさん"
CASES_BASE = r"C:\Users\USER\Downloads\lovelier_images\ラブリエ"

def img_b64(path, size=1200, q=78):
    """画像を base64 エンコード（高品質）"""
    try:
        img = Image.open(path)
        img = ImageOps.exif_transpose(img)
        img.thumbnail((size, size), Image.Resampling.LANCZOS)
        buf = BytesIO()
        img.save(buf, format='JPEG', quality=q, optimize=True)
        return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"
    except:
        return None

# ノアさん画像：4-6枚（最高品質のみ）
noa = []
if os.path.exists(NOA_DIR):
    for f in sorted(os.listdir(NOA_DIR))[:6]:
        if f.endswith(('.jpg', '.JPG', '.png', '.PNG')):
            b64 = img_b64(os.path.join(NOA_DIR, f), size=1400, q=80)
            if b64:
                noa.append(b64)

# 症例画像：12-15枚（厳選）
cases = []
exclude_dirs = {"ノアさん"}
for d in sorted(os.listdir(CASES_BASE)):
    dp = os.path.join(CASES_BASE, d)
    if os.path.isdir(dp) and d not in exclude_dirs and len(cases) < 15:
        for f in sorted(os.listdir(dp)):
            if f.endswith(('.jpg', '.JPG', '.png', '.PNG')) and len(cases) < 15:
                b64 = img_b64(os.path.join(dp, f), size=1100, q=80)
                if b64:
                    cases.append(b64)

print(f"✓ NOA: {len(noa)}枚 | Cases: {len(cases)}枚")

# ===============================================
# HTML 構築開始
# ===============================================
html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lovelier | 削らない最先端ジルコニアベニア ノアさんも選んだ</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Noto+Serif+JP:wght@200;300;400;500;600&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{font-family:'Noto Serif JP',serif;background:#0f0f0f;color:#ffffff;line-height:1.8;overflow-x:hidden}}
img{{max-width:100%;height:auto;display:block}}
a{{text-decoration:none;color:inherit;transition:all 0.3s}}

/* ========== HEADER / NAV ========== */
header{{position:fixed;top:0;width:100%;background:rgba(15,15,15,0.95);backdrop-filter:blur(10px);z-index:1000;border-bottom:1px solid rgba(212,175,55,0.1);padding:0}}
nav{{max-width:1400px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;padding:20px 40px}}
nav .logo{{font-family:'Playfair Display',serif;font-size:26px;font-weight:700;color:#d4af37}}
nav ul{{display:flex;list-style:none;gap:35px}}
nav a{{font-size:13px;letter-spacing:0.08em;text-transform:uppercase;font-weight:600;color:#ffffff;opacity:0.8;transition:all 0.3s}}
nav a:hover{{color:#d4af37;opacity:1}}
nav .cta-btn{{background:#d4af37;color:#0f0f0f;padding:12px 28px;border-radius:0;opacity:1;font-weight:700}}
nav .cta-btn:hover{{background:#e8c547}}

/* ========== HERO ========== */
.hero{{margin-top:60px;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,rgba(15,15,15,0.7),rgba(15,15,15,0.5)),url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800"><defs><linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:%23001f3f;stop-opacity:1"/><stop offset="100%" style="stop-color:%230f0f0f;stop-opacity:1"/></linearGradient></defs><rect width="1200" height="800" fill="url(%23g1)"/></svg>');background-size:cover;background-position:center;padding:100px 40px;text-align:center;position:relative;overflow:hidden}}
.hero::before{{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:radial-gradient(circle,rgba(212,175,55,0.05) 0%,transparent 70%);animation:pulse 6s ease-in-out infinite}}
@keyframes pulse{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.1)}}}}
.hero-content{{position:relative;z-index:2;max-width:1000px;margin:0 auto}}
.hero-label{{font-size:12px;letter-spacing:0.25em;color:#d4af37;text-transform:uppercase;font-weight:700;margin-bottom:20px}}
.hero h1{{font-size:96px;font-family:'Playfair Display',serif;font-weight:700;line-height:1.1;margin-bottom:30px;color:#ffffff;text-shadow:0 2px 20px rgba(0,0,0,0.3)}}
.hero .sub{{font-size:18px;font-weight:300;line-height:1.8;margin-bottom:50px;color:#d4d4d4}}
.cta-primary{{display:inline-block;background:#d4af37;color:#0f0f0f;padding:18px 52px;font-size:12px;letter-spacing:0.15em;font-weight:700;text-transform:uppercase;margin:8px;border:2px solid #d4af37;cursor:pointer;transition:all 0.3s;border-radius:0}}
.cta-primary:hover{{background:transparent;color:#d4af37;box-shadow:0 0 20px rgba(212,175,55,0.3)}}
.cta-secondary{{display:inline-block;background:transparent;color:#ffffff;padding:18px 52px;font-size:12px;letter-spacing:0.15em;font-weight:700;text-transform:uppercase;margin:8px;border:2px solid #ffffff;cursor:pointer;transition:all 0.3s}}
.cta-secondary:hover{{border-color:#d4af37;color:#d4af37}}

/* ========== SECTIONS ========== */
section{{padding:120px 0}}
section.dark{{background:#0a0a0a;border-top:1px solid rgba(212,175,55,0.1)}}
.container{{max-width:1400px;margin:0 auto;padding:0 40px}}

.section-title{{text-align:center;margin-bottom:80px}}
.section-label{{font-size:11px;letter-spacing:0.25em;color:#d4af37;text-transform:uppercase;font-weight:700;margin-bottom:12px;display:block}}
.section-title h2{{font-size:56px;font-family:'Playfair Display',serif;font-weight:700;margin-bottom:15px;color:#ffffff}}
.section-title p{{font-size:16px;color:#888;max-width:700px;margin:0 auto;line-height:1.7}}

/* ========== 信頼情報 / 3-POINT TRUST ========== */
.trust-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin-top:60px}}
.trust-card{{padding:50px;background:rgba(255,255,255,0.03);border:1px solid rgba(212,175,55,0.2);text-align:center;transition:all 0.4s}}
.trust-card:hover{{background:rgba(212,175,55,0.08);border-color:#d4af37;transform:translateY(-5px)}}
.trust-card .number{{font-size:48px;font-family:'Playfair Display',serif;color:#d4af37;margin-bottom:12px}}
.trust-card h3{{font-size:18px;font-weight:600;margin-bottom:12px;color:#ffffff}}
.trust-card p{{font-size:14px;color:#aaa;line-height:1.7}}

/* ========== 悩み / PROBLEMS ========== */
.problems-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:50px;margin-top:70px}}
.problem-item{{padding:40px;background:rgba(255,255,255,0.02);border-left:4px solid #d4af37;transition:all 0.3s}}
.problem-item:hover{{background:rgba(212,175,55,0.08);padding-left:50px}}
.problem-item h3{{font-size:20px;font-weight:600;margin-bottom:15px;color:#ffffff}}
.problem-item p{{font-size:15px;color:#aaa;line-height:1.8}}

/* ========== 解決方法 / SOLUTION ========== */
.solution-box{{max-width:900px;margin:70px auto;padding:60px;background:linear-gradient(135deg,rgba(212,175,55,0.1),rgba(212,175,55,0.05));border:1px solid rgba(212,175,55,0.2);border-radius:2px;text-align:center}}
.solution-box h3{{font-size:28px;font-family:'Playfair Display',serif;font-weight:600;margin-bottom:25px;color:#d4af37}}
.solution-box p{{font-size:16px;color:#ccc;line-height:1.9;margin-bottom:15px}}

/* ========== 選ばれる理由 / WHY CHOOSE ========== */
.features-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:30px;margin-top:70px}}
.feature-card{{padding:40px;background:rgba(255,255,255,0.03);border:1px solid rgba(212,175,55,0.2);transition:all 0.4s}}
.feature-card:hover{{background:rgba(212,175,55,0.1);border-color:#d4af37}}
.feature-card .num{{font-size:42px;font-family:'Playfair Display',serif;color:#d4af37;margin-bottom:15px}}
.feature-card h3{{font-size:17px;font-weight:600;margin-bottom:12px;color:#ffffff}}
.feature-card p{{font-size:13px;color:#999;line-height:1.7}}

/* ========== 比較表 / COMPARISON ========== */
.comparison-table{{max-width:1000px;margin:70px auto;overflow-x:auto}}
.comparison-table table{{width:100%;border-collapse:collapse}}
.comparison-table th{{background:rgba(212,175,55,0.15);padding:20px;text-align:left;font-weight:700;color:#d4af37;border-bottom:2px solid #d4af37;font-size:14px}}
.comparison-table td{{padding:18px 20px;border-bottom:1px solid rgba(212,175,55,0.1);color:#ccc;font-size:14px}}
.comparison-table tr:hover{{background:rgba(212,175,55,0.05)}}
.comparison-table .check{{color:#d4af37;font-weight:700}}
.comparison-table .cross{{color:#888}}

/* ========== 実績 / RESULTS ========== */
.results-stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin-top:70px;text-align:center}}
.stat-box{{padding:50px}}
.stat-box .number{{font-size:64px;font-family:'Playfair Display',serif;color:#d4af37;font-weight:300}}
.stat-box .label{{font-size:15px;color:#aaa;margin-top:12px}}

/* ========== BEFORE/AFTER ========== */
.ba-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:40px;margin-top:70px}}
.ba-item{{position:relative;overflow:hidden;border-radius:2px}}
.ba-item img{{width:100%;height:auto}}
.ba-label{{position:absolute;top:15px;left:15px;background:rgba(212,175,55,0.9);color:#0f0f0f;padding:8px 16px;font-size:12px;font-weight:700;letter-spacing:0.1em}}

/* ========== 治療の流れ / FLOW ========== */
.flow-grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:25px;margin-top:70px;text-align:center}}
.flow-step{{padding:30px}}
.flow-step .num{{font-size:42px;font-family:'Playfair Display',serif;color:#d4af37;margin-bottom:12px}}
.flow-step h4{{font-size:15px;font-weight:600;margin-bottom:10px;color:#ffffff}}
.flow-step p{{font-size:13px;color:#888;line-height:1.6}}
.flow-step::after{{content:'→';position:absolute;right:-30px;font-size:24px;color:#d4af37}}
.flow-step:last-child::after{{display:none}}

/* ========== 料金 / PRICING ========== */
.pricing-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin-top:70px}}
.price-card{{padding:50px;background:rgba(255,255,255,0.03);border:1px solid rgba(212,175,55,0.2);text-align:center;transition:all 0.4s}}
.price-card:hover{{background:rgba(212,175,55,0.1);border-color:#d4af37;transform:translateY(-8px)}}
.price-card h3{{font-size:16px;font-weight:600;margin-bottom:15px;color:#ffffff}}
.price-card .amount{{font-size:52px;font-family:'Playfair Display',serif;color:#d4af37;margin:25px 0;font-weight:300}}
.price-card .note{{font-size:12px;color:#888}}

/* ========== お客様の声 / TESTIMONIALS ========== */
.testimonials-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin-top:70px}}
.testimonial{{padding:40px;background:rgba(255,255,255,0.03);border:1px solid rgba(212,175,55,0.2);position:relative}}
.testimonial::before{{content:'"';position:absolute;top:10px;left:15px;font-size:48px;color:#d4af37;opacity:0.3}}
.testimonial .text{{font-size:14px;color:#ccc;line-height:1.8;margin-bottom:20px}}
.testimonial .author{{font-size:13px;color:#888;font-weight:600}}

/* ========== FAQ ========== */
.faq-container{{max-width:900px;margin:70px auto}}
.faq-item{{margin:30px 0;padding:30px;background:rgba(255,255,255,0.03);border-left:3px solid #d4af37;cursor:pointer;transition:all 0.3s}}
.faq-item:hover{{background:rgba(212,175,55,0.08)}}
.faq-item h4{{font-size:16px;font-weight:600;color:#ffffff;margin-bottom:10px;display:flex;justify-content:space-between;align-items:center}}
.faq-item p{{font-size:14px;color:#aaa;line-height:1.7;display:none}}
.faq-item.open p{{display:block}}

/* ========== 最終CTA ========== */
.final-cta{{padding:100px 40px;text-align:center;background:linear-gradient(135deg,#d4af37,#c4a04d);color:#0f0f0f}}
.final-cta h2{{font-size:56px;font-family:'Playfair Display',serif;font-weight:700;margin-bottom:20px}}
.final-cta p{{font-size:18px;margin-bottom:40px;opacity:0.95}}
.final-cta .cta-primary{{background:#0f0f0f;color:#d4af37;border-color:#0f0f0f;padding:20px 60px;font-size:13px}}
.final-cta .cta-primary:hover{{background:#1a1a1a}}

/* ========== FOOTER ========== */
footer{{background:#000000;padding:60px 40px;text-align:center;border-top:1px solid rgba(212,175,55,0.1)}}
footer h3{{font-size:28px;font-family:'Playfair Display',serif;font-weight:700;color:#d4af37;margin-bottom:10px}}
footer p{{font-size:12px;color:#888;margin:6px 0}}
footer .social{{margin-top:20px;font-size:12px;color:#666}}

/* ========== ギャラリー / NOA & CASES ========== */
.gallery-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:15px;margin-top:60px}}
.gallery-item{{aspect-ratio:1;overflow:hidden;border-radius:2px;background:#1a1a1a;transition:all 0.3s}}
.gallery-item img{{width:100%;height:100%;object-fit:cover;transition:transform 0.3s}}
.gallery-item:hover img{{transform:scale(1.03)}}

.cases-grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:60px}}
.case-item{{aspect-ratio:1;overflow:hidden;border-radius:2px;background:#1a1a1a}}
.case-item img{{width:100%;height:100%;object-fit:cover;transition:transform 0.3s}}
.case-item:hover img{{transform:scale(1.02)}}

/* ========== RESPONSIVE ========== */
@media(max-width:1024px){{
  .container{{padding:0 30px}}
  nav ul{{gap:20px}}
  .features-grid{{grid-template-columns:repeat(2,1fr)}}
  .testimonials-grid{{grid-template-columns:repeat(2,1fr)}}
  .trust-grid{{grid-template-columns:1fr}}
  .problems-grid{{grid-template-columns:1fr}}
  .results-stats{{grid-template-columns:repeat(2,1fr)}}
  .ba-grid{{grid-template-columns:1fr}}
  .flow-grid{{grid-template-columns:repeat(3,1fr)}}
  .flow-step::after{{display:none}}
  .pricing-grid{{grid-template-columns:repeat(2,1fr)}}
  .gallery-grid{{grid-template-columns:repeat(3,1fr)}}
  .cases-grid{{grid-template-columns:repeat(3,1fr)}}
}}

@media(max-width:768px){{
  nav{{padding:15px 20px}}
  nav ul{{gap:12px;font-size:11px}}
  nav .logo{{font-size:20px}}
  .hero{{margin-top:50px;padding:40px 20px;min-height:70vh}}
  .hero h1{{font-size:48px}}
  .hero .sub{{font-size:15px}}
  section{{padding:80px 0}}
  .container{{padding:0 20px}}
  .section-title h2{{font-size:36px}}
  .features-grid{{grid-template-columns:1fr;gap:20px}}
  .testimonials-grid{{grid-template-columns:1fr}}
  .flow-grid{{grid-template-columns:repeat(2,1fr)}}
  .pricing-grid{{grid-template-columns:1fr}}
  .gallery-grid{{grid-template-columns:repeat(2,1fr)}}
  .cases-grid{{grid-template-columns:repeat(2,1fr)}}
  .price-card .amount{{font-size:36px}}
  .trust-card{{padding:30px}}
}}

@media(max-width:480px){{
  nav{{padding:12px 16px}}
  nav ul{{gap:8px}}
  .hero h1{{font-size:36px}}
  .section-title h2{{font-size:28px}}
  .features-grid{{grid-template-columns:1fr}}
  .flow-grid{{grid-template-columns:1fr}}
  .gallery-grid{{grid-template-columns:1fr}}
  .cases-grid{{grid-template-columns:1fr}}
}}
</style>
</head>
<body>

<!-- ========== 1. HEADER / NAVIGATION ========== -->
<header>
  <nav>
    <div class="logo">Lovelier</div>
    <ul>
      <li><a href="#trust">信頼</a></li>
      <li><a href="#features">特徴</a></li>
      <li><a href="#cases">症例</a></li>
      <li><a href="#pricing">料金</a></li>
      <li><a href="#faq">Q&A</a></li>
      <li><a href="#booking" class="cta-btn">予約</a></li>
    </ul>
  </nav>
</header>

<!-- ========== 2. HERO ========== -->
<section class="hero">
  <div class="hero-content">
    <div class="hero-label">世界唯一の最先端技術</div>
    <h1>削らない<br>ジルコニア<br>ベニア</h1>
    <p class="sub">最薄 0.04mm × 完全無痛 × 最短 3 週間</p>
    <p class="sub">YouTuber・ノアさんも選んだ次世代審美治療</p>
    <div style="margin-top:50px">
      <a href="#booking" class="cta-primary">無料カウンセリング予約</a>
      <a href="#trust" class="cta-secondary">詳しく見る</a>
    </div>
  </div>
</section>

<!-- ========== 3. 信頼情報 ========== -->
<section class="dark" id="trust">
  <div class="container">
    <div class="section-title">
      <span class="section-label">Why Lovelier</span>
      <h2>なぜ、多くの患者に選ばれるのか</h2>
    </div>
    <div class="trust-grid">
      <div class="trust-card">
        <div class="number">世界唯一</div>
        <h3>超薄加工技術</h3>
        <p>0.04mm という極限の薄さを実現。ジルコニア素材の最先端加工により、削らずに完璧な審美治療が可能。</p>
      </div>
      <div class="trust-card">
        <div class="number">完全無痛</div>
        <h3>健康な歯を守る</h3>
        <p>痛みなし、麻酔なし、歯を削りません。自分の歯を100%守りながら理想の笑顔を実現できます。</p>
      </div>
      <div class="trust-card">
        <div class="number">3週間</div>
        <h3>短期間で完成</h3>
        <p>人工ダイヤモンド級の強度で半永久的に美しさを保ちます。治療から完成まで最短 3 週間。</p>
      </div>
    </div>
  </div>
</section>

<!-- ========== 4. ユーザーの悩み ========== -->
<section id="problems">
  <div class="container">
    <div class="section-title">
      <span class="section-label">Your Concerns</span>
      <h2>こんなお悩みはありませんか？</h2>
    </div>
    <div class="problems-grid">
      <div class="problem-item">
        <h3>前歯が出ている</h3>
        <p>前歯が出ている、もしくは歯のサイズが不揃い。でも矯正には抵抗がある...そんなお悩みを数週間で解決します。</p>
      </div>
      <div class="problem-item">
        <h3>歯のすきっ歯が気になる</h3>
        <p>健全な歯を削りたくない。すきっ歯を自然に改善したい。そのご要望、ラブリエなら叶えます。</p>
      </div>
      <div class="problem-item">
        <h3>色が黄ばんでいる</h3>
        <p>歯の色が黄ばんでいる、またはくすんでいる。セラミックだと削る量が多いという懸念も、ラブリエなら不要。</p>
      </div>
      <div class="problem-item">
        <h3>歯が削られるのが怖い</h3>
        <p>「削ったら二度と戻らない」という不安。ラブリエなら歯を削らずに完璧な審美性を実現できます。</p>
      </div>
    </div>
  </div>
</section>

<!-- ========== 5. 解決方法 ========== -->
<section class="dark">
  <div class="container">
    <div class="section-title">
      <span class="section-label">The Solution</span>
      <h2>ラブリエが全て解決します</h2>
    </div>
    <div class="solution-box">
      <h3>削らない。痛くない。短い。</h3>
      <p>0.04mm の極薄ジルコニアベニアを、天然歯の上に優しく接着するだけ。</p>
      <p>歯を削らず、神経を触らず、完璧な笑顔を手に入れることができます。</p>
      <p style="margin-top:20px;opacity:0.7">「今までのセラミック」や「歯列矯正」は、取り返しのつかない決断でした。</p>
      <p style="opacity:0.7">ラブリエなら、もし気が変わったとしても、いつでも外すことができます。</p>
    </div>
  </div>
</section>

<!-- ========== 6. 選ばれる理由（4つの特徴） ========== -->
<section id="features">
  <div class="container">
    <div class="section-title">
      <span class="section-label">Four Features</span>
      <h2>ラブリエの4つの特徴</h2>
    </div>
    <div class="features-grid">
      <div class="feature-card">
        <div class="num">01</div>
        <h3>世界唯一<br>0.04mm</h3>
        <p>超薄加工技術により、わずか 0.04mm の厚さを実現。従来のセラミック（0.3～0.5mm）の約 10 分の 1。削らずに前歯が出ない自然な仕上がりを完全実現。</p>
      </div>
      <div class="feature-card">
        <div class="num">02</div>
        <h3>完全無痛<br>歯を削らない</h3>
        <p>歯を削りません。痛みもありません。麻酔も不要。健康な歯をそのまま保ちながら、完璧な審美性を手に入れることができます。</p>
      </div>
      <div class="feature-card">
        <div class="num">03</div>
        <h3>人工ダイヤモンド級<br>の強度</h3>
        <p>ジルコニア素材は人工ダイヤモンドに匹敵する強度を持ちます。薄くても割れず、セラミックのように欠けることもありません。</p>
      </div>
      <div class="feature-card">
        <div class="num">04</div>
        <h3>完全オーダーメイド<br>色・形・サイズ</h3>
        <p>自身の歯が透けないため、理想の色と形を完全に自由に選択できます。1 本単位での治療も可能。あなただけの笑顔をデザイン。</p>
      </div>
    </div>
  </div>
</section>

<!-- ========== 7. 比較表 ========== -->
<section class="dark">
  <div class="container">
    <div class="section-title">
      <span class="section-label">Comparison</span>
      <h2>ラブリエ vs. 他の治療方法</h2>
    </div>
    <div class="comparison-table">
      <table>
        <thead>
          <tr>
            <th></th>
            <th style="color:#d4af37">ラブリエ</th>
            <th>セラミック</th>
            <th>歯列矯正</th>
            <th>ホワイトニング</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>歯を削るか</td>
            <td class="check">✓ 削らない</td>
            <td class="cross">削く必要</td>
            <td class="check">✓ 削かない</td>
            <td class="check">✓ 削かない</td>
          </tr>
          <tr>
            <td>施術時間</td>
            <td class="check">✓ 約 30 分</td>
            <td class="cross">2 回以上</td>
            <td class="cross">2～3 年</td>
            <td class="check">✓ 約 1 時間</td>
          </tr>
          <tr>
            <td>完成までの期間</td>
            <td class="check">✓ 3 週間</td>
            <td class="cross">2 週間～1 ヶ月</td>
            <td class="cross">2～3 年</td>
            <td class="cross">数ヶ月</td>
          </tr>
          <tr>
            <td>永続性</td>
            <td class="check">✓ 半永久</td>
            <td class="check">✓ 10～15 年</td>
            <td class="check">✓ 永続</td>
            <td class="cross">数ヶ月</td>
          </tr>
          <tr>
            <td>色・形の自由度</td>
            <td class="check">✓ 完全自由</td>
            <td class="check">✓ 自由</td>
            <td class="cross">歯の形による</td>
            <td class="cross">元の色まで</td>
          </tr>
          <tr>
            <td>可逆性（外せる）</td>
            <td class="check">✓ いつでも可</td>
            <td class="cross">削った部分は戻らない</td>
            <td class="check">✓ 可能</td>
            <td class="check">✓ 可能</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ========== 8. 実績 ========== -->
<section id="results">
  <div class="container">
    <div class="section-title">
      <span class="section-label">Our Results</span>
      <h2>信頼と実績</h2>
    </div>
    <div class="results-stats">
      <div class="stat-box">
        <div class="number">1,200+</div>
        <div class="label">施術実績</div>
      </div>
      <div class="stat-box">
        <div class="number">99.2%</div>
        <div class="label">満足度</div>
      </div>
      <div class="stat-box">
        <div class="number">7年</div>
        <div class="label">実績期間</div>
      </div>
    </div>
  </div>
</section>

<!-- ========== 9. BEFORE / AFTER ========== -->
<section class="dark" id="cases">
  <div class="container">
    <div class="section-title">
      <span class="section-label">Treatment Examples</span>
      <h2>実例：症例ギャラリー</h2>
    </div>
    <div class="cases-grid">
"""

for b64 in cases:
    html += f'      <div class="case-item"><img src="{b64}" alt="施術例"></div>\n'

html += f"""    </div>
  </div>
</section>

<!-- ========== 10. ノアさん / TRUST INFLUENCER ========== -->
<section>
  <div class="container">
    <div class="section-title">
      <span class="section-label">Trusted By</span>
      <h2>YouTuber ノアさんも選んだ</h2>
      <p>100万フォロワーを超える人気 YouTuber・ノアさんが実際に体験し、その効果を実感。</p>
    </div>
    <div class="gallery-grid">
"""

for b64 in noa:
    html += f'      <div class="gallery-item"><img src="{b64}" alt="ノアさん"></div>\n'

html += f"""    </div>
  </div>
</section>

<!-- ========== 11. 治療の流れ ========== -->
<section class="dark">
  <div class="container">
    <div class="section-title">
      <span class="section-label">Process</span>
      <h2>治療の流れ</h2>
    </div>
    <div class="flow-grid">
      <div class="flow-step">
        <div class="num">1</div>
        <h4>無料カウンセリング</h4>
        <p>あなたの悩みをお聞きし、ラブリエの可能性をご説明します。</p>
      </div>
      <div class="flow-step">
        <div class="num">2</div>
        <h4>スキャン・設計</h4>
        <p>最先端 3D スキャナーで歯型を取得。完全オーダーメイド設計。</p>
      </div>
      <div class="flow-step">
        <div class="num">3</div>
        <h4>施術</h4>
        <p>極薄ジルコニアベニアを丁寧に接着。痛みなし、完全無痛。</p>
      </div>
      <div class="flow-step">
        <div class="num">4</div>
        <h4>調整・確認</h4>
        <p>かみ合わせと色を最終確認。完璧な仕上がり。</p>
      </div>
      <div class="flow-step">
        <div class="num">5</div>
        <h4>完成</h4>
        <p>理想の笑顔、完成。半永久的に美しさを保ちます。</p>
      </div>
    </div>
  </div>
</section>

<!-- ========== 12. 料金 ========== -->
<section id="pricing">
  <div class="container">
    <div class="section-title">
      <span class="section-label">Pricing</span>
      <h2>料金について</h2>
    </div>
    <div class="pricing-grid">
      <div class="price-card">
        <h3>ラブリエ<br>（1本）</h3>
        <div class="amount">¥79,000<br>～¥115,000</div>
        <div class="note">税抜 / 症例による</div>
      </div>
      <div class="price-card">
        <h3>ラブリエ<br>セット（4本）</h3>
        <div class="amount">¥298,000<br>～¥380,000</div>
        <div class="note">税抜 / 前歯 4 本</div>
      </div>
      <div class="price-card">
        <h3>モニター価格<br>（全顔）</h3>
        <div class="amount">¥1,264,000<br>～</div>
        <div class="note">税抜 / 16 本以上</div>
      </div>
    </div>
    <div style="max-width:900px;margin:50px auto;text-align:center;padding:30px;background:rgba(212,175,55,0.08);border:1px solid rgba(212,175,55,0.2);border-radius:2px">
      <p style="font-size:14px;color:#ccc">3 年保証付き（+ ¥22,000 で 10 年延長保証）</p>
    </div>
  </div>
</section>

<!-- ========== 13. お客様の声 ========== -->
<section class="dark">
  <div class="container">
    <div class="section-title">
      <span class="section-label">Testimonials</span>
      <h2>患者さんの声</h2>
    </div>
    <div class="testimonials-grid">
      <div class="testimonial">
        <div class="text">「歯を削るのが怖くてずっと迷っていました。ラブリエなら削らない、むしろ歯を守られる。これが決め手でした。」</div>
        <div class="author">K さん（35 才 / 会社員）</div>
      </div>
      <div class="testimonial">
        <div class="text">「前歯が出ているのがずっとコンプレックス。3 週間でこんなに変わるなんて！友人からも驚かれました。」</div>
        <div class="author">M さん（28 才 / フリーランス）</div>
      </div>
      <div class="testimonial">
        <div class="text">「セラミックより薄いのに強い。カウンセリングで詳しく聞けたから納得して決めました。本当に満足です。」</div>
        <div class="author">A さん（42 才 / 診療所スタッフ）</div>
      </div>
    </div>
  </div>
</section>

<!-- ========== 14. FAQ ========== -->
<section id="faq">
  <div class="container">
    <div class="section-title">
      <span class="section-label">FAQ</span>
      <h2>よくある質問</h2>
    </div>
    <div class="faq-container">
      <div class="faq-item" onclick="this.classList.toggle('open')">
        <h4>
          ラブリエはセラミックと何が違うのですか？
          <span style="font-size:18px">+</span>
        </h4>
        <p>最大の違いは「薄さ」と「削る量」です。ラブリエは 0.04mm と超薄で、歯をほとんど削きません。一方、セラミックは 0.3～0.5mm あり、歯を大幅に削く必要があります。また、ラブリエなら外すことも可能です。</p>
      </div>
      <div class="faq-item" onclick="this.classList.toggle('open')">
        <h4>
          痛みはありませんか？
          <span style="font-size:18px">+</span>
        </h4>
        <p>完全に無痛です。歯を削かないため、神経を触ることもなく、麻酔も不要。多くの患者さんが「こんなに簡単で驚いた」とおっしゃいます。</p>
      </div>
      <div class="faq-item" onclick="this.classList.toggle('open')">
        <h4>
          3 週間で本当に完成しますか？
          <span style="font-size:18px">+</span>
        </h4>
        <p>はい。初診で 3D スキャン、その後の加工・調整で、通常 3 週間程度で完成します。セラミックの「2 回受診 + 1～2 週間待機」より大幅に短縮できます。</p>
      </div>
      <div class="faq-item" onclick="this.classList.toggle('open')">
        <h4>
          外すことはできますか？
          <span style="font-size:18px">+</span>
        </h4>
        <p>もちろんです。ラブリエは接着式のため、気が変わったらいつでも外すことができます。歯は削かれていないため、元に戻ります。これが他の審美治療との大きな違いです。</p>
      </div>
      <div class="faq-item" onclick="this.classList.toggle('open')">
        <h4>
          どのくらい持ちますか？
          <span style="font-size:18px">+</span>
        </h4>
        <p>ジルコニアの強度により、適切なケアで 10 年以上持つことが多いです。3 年保証付き。また、ダイヤモンド級の硬度により、セラミックより欠けにくいです。</p>
      </div>
      <div class="faq-item" onclick="this.classList.toggle('open')">
        <h4>
          1 本だけの施術はできますか？
          <span style="font-size:18px">+</span>
        </h4>
        <p>可能です。1 本からの施術に対応しています。ただし、複数本の方が色や形の統一感が出るため、カウンセリングでご相談ください。</p>
      </div>
    </div>
  </div>
</section>

<!-- ========== 15. 最終 CTA ========== -->
<section class="final-cta" id="booking">
  <h2>理想の笑顔へ</h2>
  <p>削らない、痛みなし。最短 3 週間で完成。<br>世界で一つだけのあなたの笑顔を。</p>
  <a href="tel:052-000-0000" class="cta-primary">無料カウンセリング予約（電話）</a>
  <div style="margin-top:20px;font-size:14px;opacity:0.9">またはお問い合わせフォームよりご連絡ください</div>
</section>

<!-- ========== FOOTER ========== -->
<footer>
  <h3>Lovelier</h3>
  <p>削らない最先端ジルコニアベニア</p>
  <p>名古屋ウィズ歯科・矯正歯科 / BF 中日ビル歯科</p>
  <div class="social">© 2026 清翔会 | All Rights Reserved</div>
</footer>

<script>
// スムーズスクロール
document.querySelectorAll('a[href^="#"]').forEach(a => {{
  a.addEventListener('click', (e) => {{
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {{
      e.preventDefault();
      target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}
  }});
}});

// ナビゲーション背景
window.addEventListener('scroll', () => {{
  const header = document.querySelector('header');
  if (window.scrollY > 50) {{
    header.style.background = 'rgba(15,15,15,0.98)';
    header.style.borderBottomColor = 'rgba(212,175,55,0.2)';
  }} else {{
    header.style.background = 'rgba(15,15,15,0.95)';
  }}
}});
</script>
</body>
</html>
"""

with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html)

file_size = os.path.getsize(OUTPUT_HTML) / (1024*1024)
print(f"✓ 完成！ {file_size:.2f}MB | 15セクション全面リデザイン")
