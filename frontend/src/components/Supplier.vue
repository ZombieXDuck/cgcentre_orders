<template>
  <div>
    <h4>Supplier</h4>
    <SupplierForm :supplierId="this.supplierId"></SupplierForm>
  </div>
</template>

<script>
  import axios from 'axios'
  import SupplierForm from './SupplierForm'
  import {mapActions} from 'vuex';

  export default {
    name: 'Supplier',
    components: {
      'SupplierForm': SupplierForm
    },
    props: ['supplierId'],
    methods: {
      ...mapActions(['getSupplier'])
    },
    created() {
      this.getSupplier({supplierId: this.supplierId});
    }
  }
</script>

<style scoped>
</style>
