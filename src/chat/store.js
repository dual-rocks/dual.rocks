import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    infoOpen: false,
    open: false,
    fullScreen: false
  },
  getters: {
    open: state => state.open,
    infoOpen: state => state.infoOpen,
    fullScreen: state => state.fullScreen
  },
  mutations: {
    toggleInfoOpen(state) {
      state.infoOpen = !state.infoOpen;
      if (state.infoOpen) {
        state.open = true;
      }
    },
    toggleOpen(state) {
      state.open = !state.open;
    },
    toggleFullScreen(state) {
      state.fullScreen = !state.fullScreen;
      state.open = state.fullScreen;
    }
  },
  actions: {
    toggleInfoOpen(context) {
      context.commit('toggleInfoOpen')
    },
    toggleOpen(context) {
      context.commit('toggleOpen')
    },
    toggleFullScreen(context) {
      context.commit('toggleFullScreen')
    }
  }
});
