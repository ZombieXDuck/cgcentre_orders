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
  },
  CLEAR_SUPPLIER (state) {
    state.supplier = {supplierName: [], supplierName: ''};
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
      commit('CLEAR_SUPPLIER')
  },
  submitSupplier ({commit, state}, payload) {
    if (payload.type === "new") {
      axios.post('http://localhost:8000/suppliers/',
        {
          supplierName: state.supplier.supplierName,
          supplierItems: state.supplier.supplierItems
        }
      )
        .then(function(response) {
          console.log('submitSupplier response')
          console.log(response)
          payload.router.push(
            {
              name: 'SupplierList',
              params: {
                newSupplierId: response.data.supplierId,
                newSupplierName: state.supplier.supplierName
              }
            });
            commit('CLEAR_SUPPLIER')
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
