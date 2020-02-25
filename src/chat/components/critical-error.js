import Vue from 'vue';
import { mapGetters } from 'vuex';
import SelectProfile from './select-profile';

export default Vue.component('chat-critical-error', {
  template:
    `
    <div class="chat__critical-error">
      <div v-if="criticalError == 'PROFILE_NOT_LOADED'">
        <select-profile />
      </div>
      <div v-else-if="criticalError && criticalError.stack" class="chat__critical-error__generic">
        <pre>{{ criticalError.stack }}</pre>
      </div>
      <div v-else class="chat__critical-error__generic">
        <pre>{{ JSON.stringify(criticalError) }}</pre>
      </div>
    </div>
    `,
  components: {
    SelectProfile
  },
  computed: {
    ...mapGetters([
      'criticalError'
    ])
  },
});
