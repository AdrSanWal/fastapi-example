import { defineStore } from 'pinia'


export const useCollectionStore = defineStore('collection', {
  state: () => ({
    actualCollection: 'bibliotecas',
  }),

  actions: {

    async changeCollection(collection) {
      this.actualCollection = collection
    },

  },
  //persist: true,
})
