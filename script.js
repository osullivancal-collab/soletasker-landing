(() => {
  const header = document.querySelector('[data-header]');
  const menuButton = document.querySelector('.menu-button');
  const mobileMenu = document.querySelector('#mobile-menu');

  const setMenu = (open) => {
    if (!menuButton || !mobileMenu) return;
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    menuButton.querySelector('use').setAttribute('href', open ? '#i-x' : '#i-menu');
    mobileMenu.hidden = !open;
    document.body.classList.toggle('menu-open', open);
  };

  menuButton?.addEventListener('click', () => {
    setMenu(menuButton.getAttribute('aria-expanded') !== 'true');
  });

  mobileMenu?.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => setMenu(false));
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 900) setMenu(false);
  });

  const updateHeader = () => header?.classList.toggle('scrolled', window.scrollY > 12);
  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const reveals = document.querySelectorAll('.reveal');
  if (reducedMotion || !('IntersectionObserver' in window)) {
    reveals.forEach((item) => item.classList.add('visible'));
  } else {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    reveals.forEach((item) => observer.observe(item));
  }

  document.querySelectorAll('[data-dialog]').forEach((button) => {
    button.addEventListener('click', () => document.querySelector(`#${button.dataset.dialog}`)?.showModal());
  });

  document.querySelectorAll('dialog').forEach((dialog) => {
    dialog.querySelectorAll('.dialog-close, .dialog-done').forEach((button) => {
      button.addEventListener('click', () => dialog.close());
    });
    dialog.addEventListener('click', (event) => {
      const box = dialog.getBoundingClientRect();
      const outside = event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom;
      if (outside) dialog.close();
    });
  });

  const form = document.querySelector('[data-signup-form]');
  form?.addEventListener('submit', (event) => {
    const email = form.querySelector('input[type="email"]');
    const error = form.querySelector('.field-error');
    const status = form.querySelector('.form-status');
    const isValid = email.value.trim() !== '' && email.validity.valid;

    email.classList.toggle('invalid', !isValid);
    error.textContent = isValid ? '' : 'Enter a valid email address.';
    if (!isValid) {
      event.preventDefault();
      email.focus();
      return;
    }

    status.textContent = 'Opening the secure signup confirmation…';
  });

  document.querySelector('[data-year]').textContent = new Date().getFullYear();
})();
