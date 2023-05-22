import { defineStore } from 'pinia'

const icon = {
  'libraries': 'book-solid',
  'police-stations': 'handcuffs-solid'

}

export const useCollectionStore = defineStore('collection', {
  state: () => ({
    actualCollection: 'libraries',
  }),

  getters: {
    markerIcon: (state) => icon[state.actualCollection]
  },

  actions: {

    async changeCollection(collection) {
      this.actualCollection = collection
      this.markerIcon = icon.collection
    },

  },
  //persist: true,
})
