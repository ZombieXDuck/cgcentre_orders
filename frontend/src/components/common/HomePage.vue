<template>
  <div>
    <h4>CGCenter Orders</h4>
    <div class="row justify-content-around">
      <div class="flex-column">
        <div class="col-sm button-container">
          <button type="button" class="btn" @click="routerClick('OrderList')">
            Orders
          </button>
        </div>
      </div>
      <div class="flex-column">
        <div class="col-sm button-container">
          <button type="button" class="btn" @click="routerClick('SupplierList')">
            Suppliers
          </button>
        </div>
        <div class="col-sm button-container">
          <button type="button" class="btn" @click="routerClick('NewSupplier')">
            Create a new supplier
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'HomePage',
    methods: {
      routerClick(routeName) {
        this.$router.push({ name: routeName });
      }
    }
  }
</script>

<style scoped>
  .button-container {
    margin-top: 20px;
  }
</style>
