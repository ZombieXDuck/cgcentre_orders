import Vue from 'vue'
import Router from 'vue-router'
import SupplierList from '@/components/suppliers/SupplierList'
import OrderList from '@/components/orders/OrderList'
import Supplier from '@/components/suppliers/Supplier'
import NewSupplier from '@/components/suppliers/NewSupplier'
import HomePage from '@/components/common/HomePage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/suppliers',
      name: 'SupplierList',
      props: true,
      component: SupplierList
    },
    {
      path: '/suppliers/new',
      name: 'NewSupplier',
      component: NewSupplier
    },
    {
      path: '/suppliers/:supplierId',
      name: 'Supplier',
      props: true,
      component: Supplier
    },
    {
      path: '/orders',
      name: 'OrderList',
      component: OrderList
    },
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
  ]
})
