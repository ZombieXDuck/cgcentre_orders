<template>
  <div>
    <h4>New Supplier</h4>
    <SupplierForm></SupplierForm>
  </div>
</template>

<script>
  import SupplierForm from './SupplierForm'
  import axios from 'axios'
  import {mapActions} from 'vuex';

  export default {
    name: 'NewSupplier',
    components: {
      'SupplierForm': SupplierForm
    }
  }
</script>

<style scoped>
</style>
