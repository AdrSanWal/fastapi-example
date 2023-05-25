<template>
    <LefletMap id="map-component"/>
</template>

<script setup>
import LefletMap from '@/components/LeafletMap.vue';
import { useMapStore } from '@/stores/mapStore'

const mapStore = useMapStore()

</script>

<style scoped>

</style>
