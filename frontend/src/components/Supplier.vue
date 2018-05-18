<template>
  <div>
    <h4 class="header">Supplier: {{supplierName}}</h4>
    <ul class="list-group">
      <li v-for="supplierItem in supplierItems" class="list-group-item">
        <spam><b>itemCode:</b> {{supplierItem.itemCode}}</spam>
        <spam><b>itemName:</b> {{supplierItem.itemName}}</spam>
      </li>
      <li v-if="supplierItems.length === 0" class="list-group-item">
        No items in this supplier exist yet
      </li>
    </ul>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Supplier',
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
    }
  }
</script>

<style scoped>
</style>
