import Vue from 'vue'
import Router from 'vue-router'
import SupplierList from '@/components/SupplierList'
import OrderList from '@/components/OrderList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SupplierList',
      component: SupplierList
    },
    {
      path: '/orders',
      name: 'OrderList',
      component: OrderList
    }
  ]
})
