import { defineStore } from 'pinia'


export const useMapStore = defineStore('map', {
  state: () => ({
    map: {
      coords: {
        lat: 40.417,
        lng: -3.704,
      }
    },
    tilelayers: [
    {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      visible: true,
      atribution: `&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>`,
      layerType: 'base',
      name: 'OpenStreetMap',
    },
    {
      url: 'https://tiles.stadiamaps.com/tiles/osm_bright/{z}/{x}/{y}{r}.png',
      visible: false,
      atribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
      layerType: 'base',
      name: 'Stadia.OSMBright',
    },
    {
      url: 'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png',
      visible: false,
      atribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      subdomains: 'abcd',
      layerType: 'base',
      name: 'Stamen.Terrain',
    }
    ]
  }),

  actions: {

    async updateCoords(coords) {
      this.coords = coords
    },
  },
  //persist: true,
})
