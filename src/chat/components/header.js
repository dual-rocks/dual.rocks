import Vue from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default Vue.component('chat-header', {
  template:
    `
    <div class="chat__header">
      <div class="chat__header__title" v-on:click="toggleOpen">
        <span class="icon">
          <i class="fas" v-bind:class="{'fa-caret-right': !open, 'fa-caret-down': open}"></i>
        </span>
        <span>Chat</span>
      </div>
      <div class="chat__header__actions">
        <span class="chat__header__actions__action icon" v-on:click="toggleFullScreen">
          <i class="fas fa-expand-alt"></i>
        </span>
        <span class="chat__header__actions__action icon" v-on:click="toggleInfoOpen">
          <i class="fas fa-info-circle"></i>
        </span>
      </div>
    </div>
    `,
  computed: {
    ...mapGetters([
      'open'
    ])
  },
  methods: {
    ...mapActions([
      'toggleInfoOpen',
      'toggleOpen',
      'toggleFullScreen'
    ])
  }
});
