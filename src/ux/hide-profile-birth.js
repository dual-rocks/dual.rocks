import {
  findByName,
  bulmaHideElem,
  bulmaShowElem
} from '../utils';

const bulmaFieldFromInput = inputElem => inputElem.parentElement.parentElement.parentElement;

(() => {
  const VISIBLE_BIRTH_PRONOUMS = ['H', 'S'];
  const BIRTH_FIELDS_NAME = ['year_of_birth', 'month_of_birth']

  const selectFirstOption = (inputElem) => {
    inputElem.options.selectedIndex = 0;
  };

  document
    .querySelectorAll('[data-profile-form]')
    .forEach((form) => {
      const pronounInput = form.querySelector('[name="pronoun"]');
      const birthInputs = BIRTH_FIELDS_NAME.map(name => findByName(form, name));
      const birthFields = birthInputs.map(bulmaFieldFromInput);

      const hideBirthFieldsFn = () => {
        birthInputs.forEach(selectFirstOption);
        birthFields.forEach(bulmaHideElem);
      };
      const showBirthFieldsFn = () => {
        birthFields.forEach(bulmaShowElem);
      };
      const checkPronounFn = () => {
        if (VISIBLE_BIRTH_PRONOUMS.includes(pronounInput.value)) {
          showBirthFieldsFn();
        } else {
          hideBirthFieldsFn();
        }
      };

      pronounInput.addEventListener('change', checkPronounFn);
      checkPronounFn();
    });
})();
