<template>
  <div>
    <!-- created supplier alert -->
    <div class="alert alert-success alert-dismissible fade show" role="alert" v-if="newSupplierId">
      Supplier
      <router-link :to="{ name: 'Supplier', params: {supplierId: newSupplierId} }">
        {{newSupplierName}}
      </router-link>
      has been created.
      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <!-- end of created supplier alert -->
    <h1 class="header">Suppliers</h1>
    <!-- search suppliers -->
    <div class="input-group p-4">
      <input type="text" class="form-control" placeholder="Search Suppliers" v-model="supplierSearch">
      <div class="input-group-prepend">
        <button class="btn btn-outline-secondary" type="button" @click="clearSupplierSearch">
          Clear
        </button>
      </div>
    </div>
    <!-- end of search suppliers -->
    <div class="item newSupplier" @click="newSupplierClick">
      <p class="item-title">
          Add a new supplier
      </p>
      <div class="item-count">
        <i class="fa fa-plus-square"></i>
      </div>
    </div>
    <div v-for="supplier in filteredSuppliers" class="item" @click="supplierClick(supplier.supplierId)">
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
      suppliers: [],
      supplierSearch: ''
    }
  },
  props: ['newSupplierId', 'newSupplierName'],
  computed: {
      filteredSuppliers: function() {
        const supplierSearch = this.supplierSearch.toLowerCase();
        return this.suppliers.filter(function (el) {
          return (
            supplierSearch === el.supplierName.toLowerCase().substring(0, supplierSearch.length)
          )
        })
      }
  },
  methods: {
    supplierClick(supplierId) {
      this.$router.push({ name: 'Supplier', params: {supplierId: supplierId}});
    },
    newSupplierClick() {
      this.$router.push({ name: 'NewSupplier' });
    },
    clearSupplierSearch() {
      this.supplierSearch = '';
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

  .supplier-search-container {
    padding: 0 40px;
    margin: 25px 0;
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
