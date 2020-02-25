import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    infoOpen: false,
    open: false,
    fullScreen: false,
    criticalError: null,
    profile: null,
    ws: null,
    wsConnected: false,
    roomGroupName: null,
    channelName: null
  },
  getters: {
    open: state => state.open,
    infoOpen: state => state.infoOpen,
    fullScreen: state => state.fullScreen,
    criticalError: state => state.criticalError,
    profile: state => state.profile,
    wsConnected: state => state.wsConnected,
    roomGroupName: state => state.roomGroupName,
    channelName: state => state.channelName
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
    },
    clear(state) {
      state.profile = null;
      state.ws = null;
      state.roomGroupName = null;
      state.channelName = null;
    },
    setCriticalError(state, reason) {
      state.criticalError = reason;
    },
    setProfile(state, profile) {
      state.profile = profile ? profile : null;
    },
    setWs(state, ws) {
      state.ws = ws;
    },
    setWsConnected(state, status) {
      state.wsConnected = status;
    },
    setRoomGroupNameAndChannelName(state, {roomGroupName, channelName}) {
      state.roomGroupName = roomGroupName;
      state.channelName = channelName;
    }
  },
  actions: {
    toggleInfoOpen(context) {
      return context.commit('toggleInfoOpen');
    },
    toggleOpen(context) {
      return context.commit('toggleOpen');
    },
    toggleFullScreen(context) {
      return context.commit('toggleFullScreen');
    },
    clear(context) {
      return context.commit('clear');
    },
    init(context) {
      return context.dispatch('clear')
        .then(() => context.dispatch('loadProfile'))
        .then(() => context.dispatch('connectWs'))
        .catch(reason => context.dispatch('setCriticalError', reason));
    },
    setCriticalError(context, reason) {
      return context.dispatch('clear')
        .then(() => context.commit('setCriticalError', reason));
    },
    loadProfile(context) {
      return axios
        .get('/api/my-profiles/current/')
        .then(response => response.data)
        .then(profile => context.commit('setProfile', profile))
        .catch(() => Promise.reject('PROFILE_NOT_LOADED'));
    },
    connectWs(context) {
      let done = false;

      context.commit(
        'setWs',
        new WebSocket(`ws://${window.location.host}/chat/`)
      );

      return new Promise((resolve, reject) => {
        const onCloseOrError = (event) => {
          if (done) {
            context.dispatch('setCriticalError', event);
          } else {
            done = true;
            reject('CAN_T_CONNECT_TO_WS');
          }
          context.commit('setWsConnected', false);
        };

        context.state.ws.onopen = () => {
          if (!done) {
            done = true;
            resolve();
          }
          context.state.ws.send('PING');
          context.commit('setWsConnected', true);
        };

        context.state.ws.onerror = onCloseOrError;

        context.state.ws.onclose = onCloseOrError;

        context.state.ws.onmessage = (event) => {
          const data = JSON.parse(event.data);

          switch (data.action) {
            case 'PONG':
              let roomGroupName = data.payload.room_group_name;
              let channelName = data.payload.channel_name;
              context.commit(
                'setRoomGroupNameAndChannelName',
                {
                  roomGroupName,
                  channelName
                }
              );
              break;

            default:
              console.warn(`Action not recognized: ${data.action}`);
          }
        };
      });
    }
  }
});
