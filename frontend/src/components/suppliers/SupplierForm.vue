<template>
  <div>
    <form name="newSupplierForm" @submit.prevent="">
      <!-- supplier name -->
      <div class="form-group border-bottom">
        <label>Supplier Name</label>
        <input type="text" name="supplierName" class="form-control" placeholder="Enter Supplier's Name"
          v-model="supplier.supplierName"
          v-validate="'required'"
          :class="{'error': errors.has('supplierName')}"
        />
        <span class="form-text text-danger" v-if="errors.has('supplierName')">
            A supplier name is required
        </span>
      </div>
      <!-- end of supplier name -->
      <!-- supplier items -->
      <p>Supplier Items</p>
      <div class="row border-bottom"
        v-for="(supplierItem, index) in supplier.supplierItems"
        :key="supplierItem.id"
      >
        <!-- @keyup.enter="addItem" -->
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
          <button type="button" class="btn btn-danger" @click="handleRemoveModalClick(index)">
            <i class="fa fa-trash"></i>
          </button>
        </div>
      </div>
      <div class="btn-container">
        <button type="button" class="btn" name="button" @click="addSupplierItem">
          Add New Item
        </button>
      </div>
      <!-- end of supplier items -->
      <!-- submit button -->
      <div class="btn-container--submit">
        <button type="button" class="btn btn-primary" name="button" style="float:right!important"
          @click="showSubmitModal = true"
          :disabled="errors.any()"
        >
          Submit Supplier
        </button>
      </div>
      <!-- end of submit button -->
    </form>

    <VueModal v-if="showRemoveModal" @close="handleRemoveModalClose($event)"></VueModal>
    <VueModal v-if="showSubmitModal" @close="handleSubmitModalClose($event)"></VueModal>
  </div>
</template>

<script>
  import VueModal from '@/components/common/VueModal'
  import $ from 'jquery'
  import Vue from 'vue'
  import VeeValidate from 'vee-validate'
  import axios from 'axios'
  import {mapGetters, mapActions} from 'vuex';

  Vue.use(VeeValidate)
  
  export default {
    name: 'SupplierForm',

    components: {
      'VueModal': VueModal
    },

    props: ['supplierId'],

    data() {
      return {
        id: 0,
        indexToBeRemoved: '',
        showRemoveModal: false,
        showSubmitModal: false
      }
    },

    computed: {
      ...mapGetters(['supplier'])
    },

    methods: {
      ...mapActions(
        [
          'addSupplierItem', 
          'removeSupplierItem', 
          'submitSupplier'
        ]
      ),
      handleRemoveModalClick(itemIndex) {
        this.indexToBeRemoved = itemIndex;
        this.showRemoveModal = true;
      },
      handleRemoveModalClose(remove) {
        this.showRemoveModal = false;
        remove ? this.removeSupplierItem({ this.indexToBeRemoved }) : ''
      },
      handleSubmitModalClose(submit) {
        this.showSubmitModal = false;
        submit ? this.submitForm() : ''
      },
      submitForm() {
        this.validateForm().then(formIsValid => {
          if (formIsValid) {
            this.submitSupplier({supplierId: this.supplierId, router: this.$router})
          }
        })  
      },
      validateForm() {
        return this.$validator.validate().then(valid => valid );
      }
    }
  }
</script>

<style scoped>
  .border-bottom {
    padding-bottom: 15px;
    border-bottom: 3px solid grey;
  }

  .btn-container {
    margin-top: 10px;
  }

  .btn-container--submit {
    margin-top: 33px
  }

  .error {
    border: 1px solid red;
  }
</style>
