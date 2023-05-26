<template>
  <div id="map-container"
       style="height:100vh">

    <ServiceDetail v-if="isDetailVisible"
                   @close="isDetailVisible = false"
                   :info="detailInfo"/>
    <LMap id="map"
          ref="mymap"
          :use-global-leaflet="false"
          :options="lMap.options"
          :center="coords"
          :zoom="lMap.zoom">

      <LControlLayers  position="topleft"/>

      <LTileLayer
        v-for="lTileLayer,i in lTileLayers"
        :key="i"
        :url="lTileLayer.url"
        :visible="lTileLayer.visible"
        :atribution="lTileLayer.atribution"
        :layer-type="lTileLayer.layerType"
        :subdomains="lTileLayer.subdomains"
        :name="lTileLayer.name">
      </LTileLayer>



      <LControl
          @mouseover="mouseover"
          @mouseleave="mouseleave"
          :position="'topright'"
          class="service-selector">
              <div class="icon-service">
                <img :src="lIcon.iconUrl"
                  class="selector-icon">
                <p class="service">{{ collectionStore.actualCollection }}</p>
              </div>
              <div v-if="isVisible">
                <div v-for="collection,i in collections"
                     :key="i"
                     class="icon-service">
                  <img :src="`src/assets/${collection}.svg`"
                  class="selector-icon">
                <p class="service"
                   @click="changeCollection">
                   {{ collection }}</p>
                </div>

              </div>

      </LControl>

      <LMarker v-for="marker in data"
               :key="marker.id"
               :lat-lng="[marker.location.lat, marker.location.lng]"
               :title="marker.title"
               @click="loadDetail(marker)">
        <LTooltip :content="marker.title" />
        <LIcon
          :iconUrl=lIcon.iconUrl
          :iconSize=lIcon.iconSize
          :iconAnchor=lIcon.iconAnchor>
        </LIcon>
      </LMarker>

    </LMap>

  </div>
</template>

<script setup>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LControl, LMarker , LIcon, LTooltip, LControlLayers } from "@vue-leaflet/vue-leaflet";
import { ref, onMounted } from 'vue'
import { useMapStore } from "@/stores/mapStore";
import { useCollectionStore } from "@/stores/collectionStore";
import CollectionService from '@/services/CollectionService'
import ServiceDetail from '@/components/ServiceDetail.vue'


const mapStore = useMapStore()
const collectionStore = useCollectionStore()
const collectionService = new CollectionService()

const collections = collectionService.getCollectionsNames()


const data = collectionService.getCollectionData()

const coords = ref([mapStore.map.coords.lat, mapStore.map.coords.lng])

const isDetailVisible = ref(false)

const detailInfo = ref({})


const lTileLayers = mapStore.tilelayers

const lMap = {
  options:  {
    doubleClickZoom: false,
    zoomControl: false,
    zoomDelta: 0.25,
    zoomSnap: 0,
  },
  zoom: 12
}

const lIcon = {
  iconSize: [25, 25],
  iconAnchor: [0, 0],
  iconUrl: `src/assets/${collectionStore.actualCollection}.svg`
}

onMounted(async () => {
  await collectionService.fetchCollectionsNames()
  await collectionService.fetchData(collectionStore.actualCollection)
})

let isVisible = ref(false)

const mouseover = () => isVisible.value = true
const mouseleave = () => isVisible.value = false

const changeCollection = (e) => {
  const newCollection = e.target.textContent
  collectionStore.changeCollection(newCollection)
  collectionService.fetchData(newCollection)
  lIcon.iconUrl = `src/assets/${collectionStore.actualCollection}.svg`
}

const loadDetail = (marker) => {
  console.log(marker)
  detailInfo.value = marker
  isDetailVisible.value = true
}

</script>

<style scoped>

.selector-icon {
  height: 15px;
}

.service-selector {
  display:flex;
  flex-direction: column;
  background-color: gray;
  color: whitesmoke;
  padding: 5px 15px;
  border-radius: 5px;
  font-size: small;
  border: 1px solid gray;
  opacity: 0.6;

}

.service-selector:hover {
  background-color: rgb(83, 83, 83);
  opacity: 0.9;
}

.icon-service {
  display:flex;
  flex-direction: row;
  align-items: center;
  gap: 10px;
}

.service {
  cursor: pointer
}

</style>
