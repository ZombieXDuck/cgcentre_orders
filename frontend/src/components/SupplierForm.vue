<template>
  <div>
    <ul class="list-group">
      <li v-for="supplierItem in supplierItems" class="row border-bottom">
        <!-- item code -->
        <div class="col-sm">
          <label>Item Code:</label>
        </div>
        <div class="col-sm">
          <input type="text" class="form-control" name="itemCode" placeholder="Enter Item's Code"
            v-model="supplierItem.itemCode"
            v-validate="'required'"
            :name="'itemCode' + supplierItem.id"
            :class="{'error': errors.has('itemCode' + supplierItem.id)}"
          />
          <p class="form-text text-danger" v-if="errors.has('itemCode' + supplierItem.id)">
            A item code is required
          </p>
        </div>
        <!-- item name -->
        <div class="col-sm">
          <label>Item Name:</label>
        </div>
        <div class="col-sm">
          <input type="text" class="form-control" name="itemName" placeholder="Enter Item's Name"
            v-model="supplierItem.itemName"
            v-validate="'required'"
            :name="'itemName' + supplierItem.id"
            :class="{'error': errors.has('itemName' + supplierItem.id)}"
          />
          <p class="form-text text-danger" v-if="errors.has('itemName' + supplierItem.id)">
            A item name is required
          </p>
        </div>
        <!-- delete button -->
        <div class="col-sm">
          <button type="button" class="btn btn-danger" @click="removeItem(supplierItem.index)">
            <i class="fa fa-trash"></i>
          </button>
        </div>
      </li>
      <li class="list-group-item">
        <button type="button" class="btn" @click="addNewItem">
          Add a new item
        </button>
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
    name: 'SupplierForm',
    data() {
      return {
        supplierName: '',
        supplierItems: [],
        supplierId: ''
      }
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
