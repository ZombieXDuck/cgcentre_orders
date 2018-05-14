import Vue from 'vue'
import Router from 'vue-router'
import SupplierList from '@/components/SupplierList'
import OrderList from '@/components/OrderList'
import Supplier from '@/components/Supplier'
import NewSupplier from '@/components/NewSupplier'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/suppliers',
      name: 'SupplierList',
      component: SupplierList
    },
    {
      path: '/suppliers/:supplierId',
      name: 'Suppliers',
      component: Supplier
    },
    {
      path: '/suppliers/new',
      name: 'NewSupplier',
      component: NewSupplier
    },
    {
      path: '/orders',
      name: 'OrderList',
      component: OrderList
    }
  ]
})
