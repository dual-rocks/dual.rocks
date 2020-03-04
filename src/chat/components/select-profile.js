import Vue from 'vue';
import { mapActions } from 'vuex';
import axios from 'axios';

export default Vue.component('select-profile', {
  template:
    `
    <div class="chat__select-profile">
      <p class="chat__select-profile__title has-vertical-margin">
        <small><strong v-translate>select_profile</strong></small>
      </p>
      <p v-if="loading" class="has-vertical-margin">
        <span class="icon is-small"><i class="fas fa-spinner fa-pulse"></i></span>
        <small v-translate>loading</small>
      </p>
      <p v-else-if="forbidden" class="has-vertical-margin">
        <a class="button is-small is-primary" href="/login/" v-translate>login</a>
        <a class="button is-small" href="/register/" v-translate>register</a>
      </p>
      <div v-else-if="profiles.length > 0">
        <div v-for="profile in profiles" class="card has-vertical-margin">
          <a v-bind:href="getSetAsCurrentProfileUrl(profile)">
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
          </a>
        </div>
      </div>
      <div v-else class="has-vertical-margin">
        <p v-translate>not_has_profile</p>
        <p>
          <a href="/create-profile/" class="button is-small is-primary" v-translate>create_profile</a>
        </p>
      </div>
    </div>
    `,
  mounted() {
    this.init();
  },
  data() {
    return {
      loading: true,
      forbidden: false,
      profiles: []
    };
  },
  methods: {
    init() {
      axios
        .get('/api/my-profiles/')
        .then((response) => {
          this.profiles = response.data;
        })
        .catch((error) => {
          if (error.response) {
            switch (error.response.status) {
              case 403:
                this.forbidden = true;
                break;

              default:
                console.error(`Unexpected status code: ${error.response.status}`);
            }
          } else {
            this.setCriticalError(error);
          }
        })
        .finally(() => {
          this.loading = false;
        });
    },
    getSetAsCurrentProfileUrl(profile) {
      return `/${profile.at}/set-as-current-profile`;
    },
    ...mapActions([
      'setCriticalError'
    ])
  }
});
