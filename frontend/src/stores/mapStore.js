import { defineStore } from 'pinia'


export const useMapStore = defineStore('map', {
  state: () => ({
    map: {
      coords: {
        lat: 40.417,
        lng: -3.704,
      }
    },
    tilelayer: {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      atribution: `&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>`,
      layerType: 'base',
      name: 'OpenStreetMap',
    }
  }),

  actions: {

    async updateCoords(coords) {
      this.coords = coords
    },
  },
  //persist: true,
})
