import Vue from 'vue'
import Vuex from 'vuex'
import { SupplierStore } from './SupplierStore.js'

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    SupplierStore: SupplierStore
  }
})
