<template>
    <transition name="modal">
      <div class="modal-mask">
            <div class="modal-wrapper">
                <div class="modal-container">
                    <div id="title-wrap">
                      <h3 class="title">{{ props.info.title }}</h3>
                      <p class="close" @click="$emit('close')">X</p >
                    </div>
                    <hr>
                    <div id="detail-info">
                      <p>{{ props.info.address.street }}, {{ props.info.address.postal_code }} - {{ props.info.address.locality }}</p>
                      <a :href="props.info.relation" target="_blank">+ info  <img class="img" src="src/assets/page-link2.svg"></a>
                    </div>
                    <div v-if="props.info.organization.description">
                      <h4 class="title subtitle">Descripción:</h4>
                      <p>{{ props.info.organization.description }}</p>
                    </div>
                    <div v-if="props.info.organization.services">
                      <h4 class="title subtitle">Servicios:</h4>
                      <p>{{ props.info.organization.services }}</p>
                    </div>
                    <div v-if="props.info.organization.schedule">
                      <h4 class="title subtitle">Detalles:</h4>
                      <p>{{ props.info.organization.schedule }}</p>
                    </div>
                </div>
            </div>
      </div>

    </transition>
</template>

<script setup>
const props = defineProps({
  info: Object
})
</script>

<style scoped>
.modal-mask {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  transition: opacity 0.3s ease;
  z-index: 9999;
  overflow: auto;
}

.modal-wrapper {
  vertical-align: top;
  padding: 100px;
}

.modal-container {
    width: 70%;
    min-width: 500px;
    margin: 0px auto;
    padding: 10px 20px;
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.8);
    transition: all 0.3s ease;
}

.close {
  color: grey;
  font-weight: bolder;
  cursor: pointer;
}

.close:hover {
  color: rgb(87, 85, 85);
}

#title-wrap {
  display: flex;
  justify-content: space-between;
  font-weight: bold;
}

#detail-info {
  margin-top: 15px;
}

p {
  text-align: justify;
}

.title {
  font-weight: bold;
  margin-bottom: 5px;
}

.subtitle {
  margin-top: 5px;
}

.img {
  height: 10px;
}

a {
  text-decoration:none;
}
</style>
