(() => {
  document
    .querySelectorAll('[data-confirm]')
    .forEach((elem) => {
      elem.addEventListener('click', (e) => {
        if(!confirm(elem.dataset.confirm)){
          e.preventDefault();
        }
      });
    })
})();
