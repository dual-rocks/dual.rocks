import Vue from 'vue';
import { mapGetters, mapActions } from 'vuex';
import SelectProfile from './select-profile';

export default Vue.component('chat-critical-error', {
  template:
    `
    <div class="chat__critical-error">
      <div v-if="criticalError == 'PROFILE_NOT_LOADED'">
        <select-profile />
      </div>
      <div v-else-if="criticalError == 'MESSAGES_NOT_LOADED'">
        <div class="chat__critical-error__generic">
          <p v-translate>messages_not_loaded</p>
        </div>
      </div>
      <div v-else-if="isNetworkError">
        <div class="chat__critical-error__generic">
          <p>
            <span class="icon">
              <i class="fas fa-network-wired"></i>
            </span>
            <span v-translate>network_error</span>
          </p>
        </div>
      </div>
      <div v-else-if="criticalError && criticalError.stack" class="chat__critical-error__generic">
        <pre>{{ criticalError.stack }}</pre>
      </div>
      <div v-else class="chat__critical-error__generic">
        <pre>{{ JSON.stringify(criticalError) }}</pre>
      </div>
      <div class="chat__critical-error__reload-btn">
        <button v-on:click="reload" class="button is-rounded">
          <span class="icon">
            <i class="fas fa-redo-alt"></i>
          </span>
          <span v-translate>reload</span>
        </button>
      </div>
    </div>
    `,
  components: {
    SelectProfile
  },
  computed: {
    ...mapGetters([
      'criticalError'
    ]),
    isNetworkError() {
      return this.criticalError.message == 'Network Error';
    }
  },
  methods: {
    ...mapActions([
      'reload'
    ])
  }
});
