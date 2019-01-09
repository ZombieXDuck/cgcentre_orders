<template>
    <div class="modal fade" :id="modalId" tabindex="-1" role="dialog" aria-labelledby="submitModal" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="removeItemModalLabel">Remove Supplier Item</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            Are you sure you want to submit this {{formName}}?
          </div>
          <div class="modal-footer">
            <button type="button" @click="closeModal(false)" class="btn btn-default">Cancel</button>
            <button type="button" @click="closeModal(true)" class="btn btn-primary">Submit</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import EventBus from '@/EventBus'

  export default {
    name: 'SubmitModal',
    props: ['formName', 'modalId'],
    methods: {
      closeModal(remove) {
        EventBus.$emit('closeSubmitModal', remove);
      }
    }
  }
</script>

<style scoped>
</style>
