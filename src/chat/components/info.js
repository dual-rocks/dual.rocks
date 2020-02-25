import Vue from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default Vue.component('chat-info', {
  template:
    `
    <div class="chat__info">
      <div class="notification" v-bind:class="{'is-success': wsConnected, 'is-danger': !wsConnected}">
        <button class="delete" v-on:click="toggleInfoOpen"></button>
        <p v-if="wsConnected"><strong>ONLINE</strong></p>
        <p v-if="!wsConnected"><strong>OFFLINE</strong></p>
        <p v-if="channelName">
          <span class="icon is-small"><i class="fas fa-plug"></i></span>
          <span><small>{{ channelName }}</small></span>
        </p>
      </div>
    </div>
    `,
  computed: {
    ...mapGetters([
      'wsConnected',
      'channelName'
    ])
  },
  methods: {
    ...mapActions([
      'toggleInfoOpen'
    ])
  }
});
