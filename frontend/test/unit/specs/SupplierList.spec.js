import { shallowMount, createLocalVue } from '@vue/test-utils';
import VueRouter from 'vue-router'
import SupplierList from '@/components/SupplierList'

describe('SupplierList.vue', () => {
  let localVue = createLocalVue()
  localVue.use(VueRouter)
  let router = new VueRouter()
  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(SupplierList, {
      localVue,
      router
    })
  })

  it('should render correct contents', () => {
    expect(wrapper.html()).toContain('Suppliers')
  })

  it('should have correct init data', () => {
    expect(wrapper.vm.suppliers).toEqual([
      {
        name: "Plants Plus",
        supplierId: 22,
        count: 22
      },
      {
        name: "Something Else",
        supplierId: 11,
        count: 33
      }
    ])
  })

  it('should have to order items', () => {
    wrapper.vm.suppliers = [
      {name: "Plants Plus", id: 22, count: 22},
      {name: "Something Else", id: 11, count: 33}
    ]
    expect(wrapper.html()).toContain("Plants Plus")
    expect(wrapper.html()).toContain("Something Else")
  })
})
