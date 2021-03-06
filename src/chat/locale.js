import Vue from 'vue';
import VueTranslate from 'vue-translate-plugin';

Vue.use(VueTranslate);

const pt_BR = {
  select_profile: 'Selecione um perfil',
  loading: 'Carregando...',
  login: 'Entrar na sua conta',
  register: 'Criar conta',
  not_has_profile: 'Você não tem nenhum perfil!',
  create_profile: 'Criar perfil',
  messages_not_loaded: 'Mensagens não carregadas.',
  reload: 'Recarregar',
  network_error: 'Erro na conexão!'
};

Vue.locales({
    pt: pt_BR,
    'pt-BR': pt_BR
});
