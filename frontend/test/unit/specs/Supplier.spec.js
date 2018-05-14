import { shallowMount, createLocalVue } from '@vue/test-utils';
import VueRouter from 'vue-router'
import Supplier from '@/components/Supplier'

describe('Supplier.vue', () => {
  let localVue = createLocalVue()
  localVue.use(VueRouter)
  let router = new VueRouter()
  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(Supplier, {
      localVue,
      router
    })
  })

  it('should render correct contents', () => {
    expect(wrapper.html()).toContain('Supplier')
  })


  it('should have the supplier items listed', () => {
    expect(wrapper.html()).toContain("small plant");
    expect(wrapper.html()).toContain("large plant");
  })
});
