import { ref } from 'vue'

const host = 'http://localhost:8000'

class CollectionService {
  collectionsNames
  collectionData

  constructor() {
    this.collectionsNames = ref([])
    this.collectionData = ref([])
  }

  getCollectionsNames() {
    return this.collectionsNames
  }

  getCollectionData() {
    return this.collectionData
  }

    async fetchCollectionsNames() {
    try {
      const url = `${host}/services`
      const response = await fetch(url)
      const json = await response.json()
      this.collectionsNames.value = await json

    } catch(error) {
      console.log(error)
    }
  }

  async fetchData(collectionName) {
    try {
      const url = `${host}/${collectionName}`
      const response = await fetch(url)
      const json = await response.json()
      this.collectionData.value = await json

    } catch(error) {
      console.log(error)
    }
  }

}

export default CollectionService
