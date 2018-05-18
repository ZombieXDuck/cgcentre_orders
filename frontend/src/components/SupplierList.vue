<template>
  <div>
    <h1 class="header">Suppliers</h1>
    <div class="item newSupplier" @click="newSupplierClick">
      <p class="item-title">
          Add a new supplier
      </p>
      <div class="item-count">
        <i class="fa fa-plus-square"></i>
      </div>
    </div>
    <div v-for="supplier in suppliers" class="item" @click="supplierClick(supplier.supplierId)">
      <p class="item-title">
        {{supplier.supplierName}}
      </p>
      <div class="item-count">
        <span>items: {{supplier.count}}</span>
      </div>
    </div>
    <div class="item" v-if="suppliers.length === 0">
      <p>
        No suppliers exist yet.
      </p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SupplierList',
  data () {
    return {
      suppliers: []
    }
  },
  methods: {
    supplierClick(supplierId) {
      this.$router.push({ name: 'Supplier', params: {supplierId: supplierId}});
    },
    newSupplierClick() {
      this.$router.push({ name: 'NewSupplier' });
    }
  },
  created() {
    var self = this
    axios.get('http://localhost:8000/suppliers/')
      .then(function (response) {
        self.suppliers = response.data
      })
      .catch(function (error) {
        console.log(error)
      })
  }
}
</script>

<style scoped>
  .header {
    font-size: 2em;
    font-weight: bold;
    padding-bottom: 30px;
  }

  .item {
    position: relative;
    float: left;
    width: 140px;
    height: 140px;
    box-shadow: 0 1px 4px rgba(1,1,1,.15);
    margin: 0 0 60px 40px;
    cursor: pointer;
  }

  .item-title {
    padding-top: 22px;
    font-weight: bold;
  }

  .item-count {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 6px 14px;
    border-top: 1px solid #e8e8e8;
  }
</style>
