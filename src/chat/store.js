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
    channelName: null,
    messages: []
  },
  getters: {
    open: state => state.open,
    infoOpen: state => state.infoOpen,
    fullScreen: state => state.fullScreen,
    criticalError: state => state.criticalError,
    profile: state => state.profile,
    wsConnected: state => state.wsConnected,
    roomGroupName: state => state.roomGroupName,
    channelName: state => state.channelName,
    messages: state => state.messages
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
      state.criticalError = null;
      state.profile = null;
      state.ws = null;
      state.roomGroupName = null;
      state.channelName = null;
      state.messages = [];
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
    },
    setMessages(state, messages) {
      state.messages = messages;
    },
    addNewMessage(state, message) {
      state.messages.unshift(message);
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
        .then(() => context.dispatch('loadMessages'))
        .catch(reason => context.dispatch('setCriticalError', reason));
    },
    reload(context) {
      return context.dispatch('init');
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

            case 'message':
              const message = data.payload.message
              context.commit('addNewMessage', message);
              break;

            default:
              console.warn(`Action not recognized: ${data.action}`);
          }
        };
      });
    },
    loadMessages(context) {
      return axios
        .get('/api/my-messages/?limit_messages_per_profile=3')
        .then(response => response.data)
        .then(messages => context.commit('setMessages', messages))
        .catch(() => Promise.reject('MESSAGES_NOT_LOADED'));
    }
  }
});
