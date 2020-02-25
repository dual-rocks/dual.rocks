import Vue from 'vue';
import { mapGetters, mapActions } from 'vuex';
import ChatHeader from './header';
import ChatInfo from './info';
import ChatBody from './body';
import ChatCriticalError from './critical-error';

export default Vue.component('chat', {
  template:
    `
    <div class="chat" v-bind:class="{'chat--full-screen': fullScreen}">
      <chat-header />
      <chat-info v-show="infoOpen" />
      <chat-body v-show="!criticalError && open" />
      <chat-critical-error v-if="criticalError && open" />
    </div>
    `,
  components: {
    ChatHeader,
    ChatInfo,
    ChatBody,
    ChatCriticalError
  },
  mounted () {
    const language = (
      window.navigator.userLanguage ||
      window.navigator.language
    );
    this.$translate.setLang(language);
    this.init();
  },
  computed: {
    ...mapGetters([
      'infoOpen',
      'open',
      'fullScreen',
      'criticalError'
    ])
  },
  methods: {
    ...mapActions([
      'init'
    ])
  }
});
