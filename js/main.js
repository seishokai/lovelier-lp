document.documentElement.classList.add('motion-ready');

const header = document.querySelector('[data-header]');
const menuToggle = document.querySelector('[data-menu-toggle]');
const mobileMenu = document.querySelector('[data-mobile-menu]');
const toast = document.querySelector('[data-toast]');
const moreCasesButton = document.querySelector('[data-more-cases]');
let toastTimer;
const uiText = (source) => window.LovelierI18n?.t(source) || source;

const updateHeader = () => header?.classList.toggle('is-scrolled', window.scrollY > 12);
updateHeader();
window.addEventListener('scroll', updateHeader, { passive: true });

const closeMenu = ({ returnFocus = false } = {}) => {
  if (!menuToggle || !mobileMenu) return;
  const wasOpen = menuToggle.getAttribute('aria-expanded') === 'true';
  menuToggle.setAttribute('aria-expanded', 'false');
  menuToggle.setAttribute('aria-label', uiText('メニューを開く'));
  mobileMenu.hidden = true;
  document.body.classList.remove('menu-open');
  if (returnFocus && wasOpen) menuToggle.focus();
};

menuToggle?.addEventListener('click', () => {
  const opening = menuToggle.getAttribute('aria-expanded') !== 'true';
  menuToggle.setAttribute('aria-expanded', String(opening));
  menuToggle.setAttribute('aria-label', uiText(opening ? 'メニューを閉じる' : 'メニューを開く'));
  mobileMenu.hidden = !opening;
  document.body.classList.toggle('menu-open', opening);
});

mobileMenu?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => closeMenu()));

window.addEventListener('lovelier:languagechange', () => {
  const isOpen = menuToggle?.getAttribute('aria-expanded') === 'true';
  menuToggle?.setAttribute('aria-label', uiText(isOpen ? 'メニューを閉じる' : 'メニューを開く'));
});

const showStatus = (message) => {
  if (!toast) return;
  clearTimeout(toastTimer);
  toast.textContent = message;
  toast.hidden = false;
  toastTimer = setTimeout(() => { toast.hidden = true; }, 4600);
};

document.querySelectorAll('[data-reservation]').forEach((control) => {
  control.addEventListener('click', () => closeMenu());
});

moreCasesButton?.addEventListener('click', () => {
  const hiddenCards = [...document.querySelectorAll('.extra-case[hidden]')];
  hiddenCards.forEach((card) => { card.hidden = false; });
  moreCasesButton.setAttribute('aria-expanded', 'true');
  moreCasesButton.hidden = true;
  const firstCard = hiddenCards[0];
  if (firstCard) {
    firstCard.tabIndex = -1;
    firstCard.focus({ preventScroll: true });
  }
});

document.querySelectorAll('.faq-item').forEach((item, index) => {
  const button = item.querySelector('button');
  const panel = item.querySelector(':scope > div');
  if (!button || !panel) return;
  const panelId = `faq-panel-${index + 1}`;
  panel.id = panelId;
  panel.setAttribute('role', 'region');
  panel.setAttribute('aria-labelledby', `faq-button-${index + 1}`);
  panel.hidden = true;
  button.id = `faq-button-${index + 1}`;
  button.setAttribute('aria-controls', panelId);
  button.addEventListener('click', () => {
    const opening = button.getAttribute('aria-expanded') !== 'true';
    button.setAttribute('aria-expanded', String(opening));
    panel.hidden = !opening;
  });
});

const desktopMenuQuery = window.matchMedia('(min-width: 1121px)');
desktopMenuQuery.addEventListener('change', (event) => {
  if (event.matches) closeMenu();
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    closeMenu({ returnFocus: true });
    if (toast) toast.hidden = true;
  }
});

// Editorial reveal and conversion-aware mobile booking bar.
const revealTargets = document.querySelectorAll(
  '.decision-strip article, .section-head, .about-copy, .thin-copy, .feature-list article > div, .noa-grid > div, .noa-case-head, .case-card, .comparison-grid > div, .flow-list li, .price-editorial-head, .price-matrix-row, .doctor-copy, .clinic-row, .faq-item'
);
const imageRevealTargets = document.querySelectorAll(
  '.case-feature figure, .about figure, .thin-grid figure, .concern-grid figure, .feature-list figure, .noa-grid figure, .noa-case-stage, .doctor-photo, .luxury-final figure'
);

revealTargets.forEach((element, index) => {
  element.classList.add('js-reveal');
  element.style.setProperty('--reveal-delay', `${Math.min(index % 3, 2) * 70}ms`);
});

imageRevealTargets.forEach((element, index) => {
  element.classList.add('js-image-reveal');
  element.style.setProperty('--reveal-delay', `${(index % 2) * 90}ms`);
});

if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-revealed');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

  [...revealTargets, ...imageRevealTargets].forEach((element) => revealObserver.observe(element));
} else {
  [...revealTargets, ...imageRevealTargets].forEach((element) => element.classList.add('is-revealed'));
}

const mobileBookingBar = document.querySelector('[data-mobile-booking]');
const heroSection = document.querySelector('.hero');
const finalCtaSection = document.querySelector('.luxury-final');
let framePending = false;

const updateEditorialUi = () => {
  framePending = false;
  const maxScroll = Math.max(document.documentElement.scrollHeight - window.innerHeight, 1);
  document.documentElement.style.setProperty('--page-progress', Math.min(window.scrollY / maxScroll, 1));

  if (mobileBookingBar && heroSection && finalCtaSection) {
    const beyondHero = window.scrollY > heroSection.offsetTop + heroSection.offsetHeight * 0.72;
    const finalCtaNear = finalCtaSection.getBoundingClientRect().top < window.innerHeight * 0.88;
    mobileBookingBar.classList.toggle('is-visible', beyondHero && !finalCtaNear);
  }
};

const requestEditorialUiUpdate = () => {
  if (framePending) return;
  framePending = true;
  requestAnimationFrame(updateEditorialUi);
};

updateEditorialUi();
window.addEventListener('scroll', requestEditorialUiUpdate, { passive: true });
window.addEventListener('resize', requestEditorialUiUpdate, { passive: true });

// Subtle light follows the pointer across the hero portrait on fine-pointer devices.
const heroPortrait = document.querySelector('.hero-media');
if (heroPortrait && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
  heroPortrait.addEventListener('pointermove', (event) => {
    const rect = heroPortrait.getBoundingClientRect();
    const x = ((event.clientX - rect.left) / rect.width) * 100;
    const y = ((event.clientY - rect.top) / rect.height) * 100;
    heroPortrait.style.setProperty('--hero-light-x', `${x}%`);
    heroPortrait.style.setProperty('--hero-light-y', `${y}%`);
  });
  heroPortrait.addEventListener('pointerleave', () => {
    heroPortrait.style.removeProperty('--hero-light-x');
    heroPortrait.style.removeProperty('--hero-light-y');
  });
}
