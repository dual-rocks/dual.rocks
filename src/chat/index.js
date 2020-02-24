import Vue from 'vue';
import store from './store';
import Chat from './components/chat';
import './locale';

(() => {
  new Vue({
    render: h => h(Chat),
    components: {
      Chat
    },
    store,
  }).$mount('#chat');
})();
