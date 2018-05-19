<template>
  <div>
    <h4 class="header">Supplier: {{supplierName}}</h4>
  </div>
</template>

<script>
  import axios from 'axios'
  import SupplierForm from './SupplierForm'

  export default {
    name: 'Supplier',
    components: [SupplierForm],
    data() {
      return {
        supplierName: '',
        supplierItems: [],
        supplierId: ''
      }
    },
    created() {
      var self = this;
      self.supplierId = this.$route.params.supplierId;
      axios.get('http://localhost:8000/suppliers/' + this.$route.params.supplierId)
        .then(function(response) {
          console.log(response)
          self.supplierItems = response.data;
        })
        .catch(function(error) {
          console.log(error)
        })
    },
    methods: {
      addNewItem() {
        this.supplierItems.push({itemName: '', itemCode: ''})
      },
      removeItem(itemIndex) {
        this.supplierItems.splice(itemIndex, 1);
      }
    }
  }
</script>

<style scoped>
  .border-bottom {
    padding-bottom: 15px;
    border-bottom: 3px solid grey;
  }
</style>
