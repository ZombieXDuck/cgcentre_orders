<template>
  <div>
    <h1 class="header">Suppliers</h1>
    <div v-for="supplier in suppliers" class="item">
      <!-- router-link to="order.id" -->
      <p class="item-title">
        {{supplier.name}}
      </p>
      <div class="item-count">
        <span>items: {{supplier.count}}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SupplierList',
  data () {
    return {
      suppliers: [
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
      ]
    }
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
