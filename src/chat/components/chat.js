import Vue from 'vue';
import { mapGetters } from 'vuex';
import ChatHeader from './header';
import ChatInfo from './info';
import ChatBody from './body';

export default Vue.component('chat', {
  template:
    `
    <div class="chat" v-bind:class="{'chat--full-screen': fullScreen}">
      <chat-header />
      <chat-info v-show="infoOpen" />
      <chat-body v-show="open" />
    </div>
    `,
  components: {
    ChatHeader,
    ChatInfo,
    ChatBody
  },
  computed: {
    ...mapGetters([
      'infoOpen',
      'open',
      'fullScreen'
    ])
  }
});
