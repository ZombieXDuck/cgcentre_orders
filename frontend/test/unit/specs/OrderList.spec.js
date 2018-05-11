import { shallowMount, createLocalVue } from '@vue/test-utils';
import VueRouter from 'vue-router'
import OrderList from '@/components/OrderList'

describe('OrderList.vue', () => {
  let localVue = createLocalVue()
  localVue.use(VueRouter)
  let router = new VueRouter()
  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(OrderList, {
      localVue,
      router
    })
  })

  it('should render correct contents', () => {
    expect(wrapper.html()).toContain('Orders')
  })

  it('should have correct init data', () => {
    expect(wrapper.vm.orders).toEqual([
      {
        name: "Plants Plus",
        orderId: 59,
        count: "44"
      },
      {
        name: "Something Else",
        orderId: 60,
        count: "33"
      }
    ])
  })

  it('should have to order items', () => {
    wrapper.vm.orders = [
      {name: "first", id: 1, count: 45},
      {name: "second", id: 2, count: 22}
    ]
    expect(wrapper.html()).toContain("first")
    expect(wrapper.html()).toContain("second")
  })
})
