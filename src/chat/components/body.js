import Vue from 'vue';
import { mapGetters } from 'vuex';

export default Vue.component('chat-body', {
  template:
    `
    <div class="chat__body">
      <div v-if="profile" class="card">
        <div class="card-content">
          <div class="media">
            <div class="media-left">
              <figure class="image is-48x48">
                <img v-bind:src="profile.picture_url" />
              </figure>
            </div>
            <div class="media-content">
              <p class="title is-4">{{ profile.name }}</p>
              <p class="subtitle is-6">@{{ profile.at }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    `,
  computed: {
    ...mapGetters([
      'profile'
    ])
  }
});
