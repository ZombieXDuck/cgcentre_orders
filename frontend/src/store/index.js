import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const state = {
  supplier: {
    supplierItems: [],
    supplierName: ''
  }
}

const mutations = {
  ADD_SUPPLIER_ITEM (state) {
    state.supplier.supplierItems.push({itemCode: '', itemName: ''})
  },
  REMOVE_SUPPLIER_ITEM (state, payload) {
    state.supplier.supplierItems.splice(payload.index, 1)
  },
  UPDATE_SUPPLIER (state, payload) {
    state.supplier = payload;
  }
}

const actions = {
  addSupplierItem ({commit}) {
    commit('ADD_SUPPLIER_ITEM');
  },
  removeSupplierItem ({commit}, payload) {
    console.log(payload)
    commit('REMOVE_SUPPLIER_ITEM', {index: payload.index});
  },
  getSupplier ({ commit }, payload) {
    axios.get('http://localhost:8000/suppliers/' + payload.supplierId)
      .then(function(response) {
        commit('UPDATE_SUPPLIER', response.data);
      })
      .catch(function(error) {
        console.log(error)
      })
  },
  clearSupplier ({commit}) {
      commit('UPDATE_SUPPLIER', {supplierItems: [], supplierName: ''})
  },
  submitSupplier ({commit, state}, payload) {
    if (payload.type === "new") {
      axios.post('http://localhost:8000/suppliers/', {supplierName: state.supplierName, supplierItems: state.supplierItems})
        .then(function(response) {
          console.log(response);
          //self.$router.push({ name: 'SupplierList', props: {created: true} });
        })
        .catch(function(err) {
          console.log(err)
        })
    } else {
      console.log('incorrect type: ' + payload)
      //post to suppliers/<supplierId:int>
    }
  }
}

const getters = {
  supplier: state => state.supplier
}

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
})
