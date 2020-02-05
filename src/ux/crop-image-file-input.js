import Cropper from 'cropperjs';
import { bulmaHideElem, bulmaShowElem } from '../utils';

(() => {
  document
    .querySelectorAll('[data-crop-image-file-input]')
    .forEach((input) => {
      const attrs = JSON.parse(input.dataset.cropImageFileInput);
      const control = input.parentElement.parentElement;
      const form = control.parentElement.parentElement;
      const targetQuery = attrs.target;
      const target = form.querySelector(targetQuery);

      const image = document.createElement('img');
      const imageContainer = document.createElement('div');
      imageContainer.appendChild(image);
      imageContainer.classList.add('crop-image-file-input-image-container');
      bulmaHideElem(imageContainer);
      control.appendChild(imageContainer);

      bulmaHideElem(target.parentElement.parentElement);

      input.addEventListener('change', () => {
        const file = new FileReader();
        file.readAsDataURL(input.files[0]);
        file.onload = () => {
          image.src = file.result;
          bulmaShowElem(imageContainer);

          const cropper = new Cropper(
            image,
            Object.assign({
              crop: () => {
                target.value = JSON.stringify(cropper.getData());
              },
            }, attrs.options)
          );
        };
      });
    });
})();
