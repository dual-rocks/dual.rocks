export const findByName = (elem, name) => {
  return elem.querySelector(`[name="${name}"]`);
};

export const bulmaFieldFromInput = inputElem => inputElem.parentElement.parentElement.parentElement;

export const bulmaHideElem = (elem) => {
  elem.classList.add('is-hidden');
};

export const bulmaShowElem = (elem) => {
  elem.classList.remove('is-hidden');
};
