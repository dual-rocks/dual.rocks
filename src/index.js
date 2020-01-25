import './scss/main.scss';

document
  .querySelectorAll('[data-navbar-toggle]')
  .forEach((element) => {
    const targetQuery = element.dataset.navbarToggle;
    const target = document.querySelector(targetQuery);

    element.addEventListener('click', () => {
      target.classList.toggle('is-active');
    });
  });
