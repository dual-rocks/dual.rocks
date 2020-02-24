import Vue from 'vue';
import VueTranslate from 'vue-translate-plugin';

Vue.use(VueTranslate);

const pt_BR = {
  select_profile: 'Selecione um perfil',
  loading: 'Carregando...',
  login: 'Entrar na sua conta',
  register: 'Criar conta'
};

Vue.locales({
    pt: pt_BR,
    'pt-BR': pt_BR
});
