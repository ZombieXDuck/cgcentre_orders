import axios from 'axios'

export const SupplierStore = {
	state: {
		supplier: {
			supplierItems: [],
			supplierName: ''
		},
		suppliers: [],
	},

	mutations: {
		ADD_SUPPLIER_ITEM(state) {
			state.supplier.supplierItems.push({ itemCode: '', itemName: '' })
		},
		REMOVE_SUPPLIER_ITEM(state, payload) {
			state.supplier.supplierItems.splice(payload.index, 1)
		},
		UPDATE_SUPPLIER(state, payload) {
			state.supplier = payload;
		},
		CLEAR_SUPPLIER(state) {
			state.supplier = { supplierItems: [], supplierName: '' };
		},
		UPDATE_SUPPLIERS(state, payload) {
			state.suppliers = payload;
		}
	},

	actions: {
		addSupplierItem({ commit }) {
			commit('ADD_SUPPLIER_ITEM');
		},
		removeSupplierItem({ commit }, payload) {
			commit('REMOVE_SUPPLIER_ITEM', { index: payload.index });
		},
		getSupplier({ commit }, payload) {
			axios.get('http://localhost:8000/suppliers/' + payload.supplierId)
				.then(function (response) {
					commit('UPDATE_SUPPLIER', response.data);
				})
				.catch(function (error) {
					console.log(error)
				})
		},
		getSuppliers({ commit }, payload) {
			axios.get('http://localhost:8000/suppliers/')
				.then(function (response) {
					commit('UPDATE_SUPPLIERS', response.data)
				})
				.catch(function (error) {
					console.log(error)
				})
		},
		clearSupplier({ commit }) {
			commit('CLEAR_SUPPLIER')
		},
		submitSupplier({ commit, state }, payload) {
			console.log('submitSupplier')
			console.log('payload.supplierId: ' + payload.supplierId)
			console.log('****')
			axios.post('http://localhost:8000/suppliers/' + (payload.supplierId ? payload.supplierId : ''),
				{
					supplierName: state.supplier.supplierName,
					supplierItems: state.supplier.supplierItems
				}
			).then(function (response) {
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
			.catch(function (err) {
				console.log('Submit supplier error')
				console.log(err)
			})
		}
	},

	getters: {
		supplier: state => state.supplier,
		suppliers: state => state.suppliers
	}
}