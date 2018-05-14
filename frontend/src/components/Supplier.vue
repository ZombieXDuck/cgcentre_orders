<template>
  <div>
    <h4 class="header">Supplier: {{name}}</h4>
    <ul class="list-group">
      <li v-for="item in items" class="list-group-item">
        <span>{{item.code}} | </span>
        <span>{{item.desc}} | </span>
        <span>Add Item to Order</span>
      </li>
      <li v-if="items.length === 0" class="list-group-item">
        No items in this supplier exist yet
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'Supplier',
    data() {
      return {
        name: "Plants Plus",
        supplierId: 22,
        count: 22,
        items: [
          {
            code: "1",
            desc: "small plant"
          },
          {
            code: "2",
            desc: "large plant"
          }
        ]
      }
    },
    created() {
      console.log(this.$route.params.supplierId)
      //axios.get('/supplier', { suppliedId })
    }
  }
</script>

<style scoped>
</style>
