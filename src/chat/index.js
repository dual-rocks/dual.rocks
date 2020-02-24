import Vue from 'vue';
import store from './store';
import Chat from './components/chat';

(() => {
  new Vue({
    render: h => h(Chat),
    components: {
      Chat
    },
    store,
  }).$mount('#chat');
})();
