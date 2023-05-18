<template>
  <div id="map-container"
       style="height:100vh">
    <LMap id="map"
          ref="mymap"
          :use-global-leaflet="false"
          :options="lMap.options"
          :center="coords"
          :zoom="lMap.zoom">

      <LTileLayer
        :url="lTileLayer.url"
        :atribution="lTileLayer.atribution"
        :layer-type="lTileLayer.layerType"
        :name="lTileLayer.name">
      </LTileLayer>

      <LControl>

      </LControl>

    </LMap>
  </div>
</template>

<script setup>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LControl } from "@vue-leaflet/vue-leaflet";
import { ref } from 'vue'
import { useMapStore } from "@/stores/mapStore";


const mapStore = useMapStore()

const coords = ref([mapStore.map.coords.lat, mapStore.map.coords.lng])

const lTileLayer = mapStore.tilelayer

const lMap = {
  options:  {
    doubleClickZoom: false,
    zoomControl: false,
    zoomDelta: 0.25, //TODO: try to make this work
    zoomSnap: 0, //TODO: try to make this work
  },
  zoom: 12
}

const lControl = {

}

</script>

<style scoped>

</style>
