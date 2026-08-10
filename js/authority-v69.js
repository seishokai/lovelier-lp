(() => {
  'use strict';

  const heroCopy = document.querySelector('.hero-copy');
  if (heroCopy && !heroCopy.querySelector('[data-hero-authority]')) {
    heroCopy.insertAdjacentHTML('afterbegin', `
      <a class="hero-authority-seal" href="#authority-proof" data-hero-authority aria-label="日本一の症例数を誇る医療法人清翔会について見る">
        <span>LOVELIER CASE VOLUME</span>
        <strong><b>症例数</b><em>日本一</em><sup>※</sup></strong>
        <small>医療法人清翔会</small>
      </a>`);
  }

  const stripAuthority = document.querySelector('.decision-strip article:nth-child(2)');
  stripAuthority?.classList.add('decision-authority');

  const decisionStrip = document.querySelector('.decision-strip');
  if (decisionStrip && !document.querySelector('[data-authority-proof]')) {
    const section = document.createElement('section');
    section.className = 'authority-proof';
    section.id = 'authority-proof';
    section.dataset.authorityProof = '';
    section.setAttribute('aria-labelledby', 'authority-proof-title');
    section.innerHTML = `
      <div class="authority-proof-inner wrap-wide">
        <div class="authority-proof-rank">
          <p>LOVELIER CASE LEADERSHIP / JAPAN</p>
          <div><span>症例数</span><strong>日本一</strong><sup>※</sup></div>
          <h2 id="authority-proof-title">日本一の症例数が、<br>治療の選択肢と<br>デザイン精度を支える。</h2>
          <p class="authority-proof-lead">削らない選択肢を、積み重ねた経験から提案します。</p>
        </div>
        <figure class="authority-proof-award">
          <img src="assets/images/award-certified-dentist.jpg" width="720" height="1080" loading="lazy" alt="原俊太朗先生のLa Briller Certified Dentist 2026認定盾">
          <figcaption><span>OFFICIAL CERTIFICATION</span><strong>La Briller<br>Certified Dentist 2026</strong><small>ラブリエ認定医</small></figcaption>
        </figure>
        <div class="authority-proof-doctor">
          <p>MEDICAL CORPORATION</p>
          <strong>医療法人清翔会</strong>
          <h3>原 俊太朗</h3>
          <ul>
            <li>副理事長</li>
            <li>名古屋ウィズ歯科・矯正歯科 院長</li>
            <li>BF中日ビル歯科・矯正歯科 院長</li>
          </ul>
          <a href="#doctor">原先生の治療哲学を見る <span aria-hidden="true">→</span></a>
        </div>
      </div>
      <p class="authority-proof-note wrap-wide">※医療法人清翔会グループ提供情報に基づく表現です。集計期間・対象施設・算定基準はお問い合わせください。</p>`;
    decisionStrip.insertAdjacentElement('afterend', section);
  }

  const proof = document.querySelector('[data-authority-proof]');
  if (proof) {
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.16 });
      observer.observe(proof);
    } else {
      proof.classList.add('is-visible');
    }
  }
})();
