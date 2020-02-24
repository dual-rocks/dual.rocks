import Vue from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default Vue.component('chat-info', {
  template:
    `
    <div class="chat__info">
      <div class="notification is-success">
        <button class="delete" v-on:click="toggleInfoOpen"></button>
        <strong>ONLINE</strong>
      </div>
    </div>
    `,
  methods: {
    ...mapActions([
      'toggleInfoOpen'
    ])
  }
});
