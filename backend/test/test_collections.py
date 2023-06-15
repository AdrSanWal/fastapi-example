from pytest import mark

from . import asserts


@mark.libraries
class TestLibrary:
    collection = 'bibliotecas'

    def test_get_libraries(self, test_client):
        print(test_client.__dict__)
        asserts.asserts_get_instances(test_client, self.collection)

    def test_post_library(self, test_client, test_collection):
        asserts.asserts_post_instance(test_client,
                                      self.collection,
                                      test_collection)

    def test_post_existing_library(self, test_client, test_collection):
        asserts.asserts_post_existing_instance(test_client,
                                               self.collection,
                                               test_collection)

    def test_get_existing_library(self, test_client, test_collection):
        asserts.asserts_get_existing_instance(test_client,
                                              self.collection,
                                              test_collection)

    def test_fail_get_not_existing_library(self, test_client):
        asserts.asserts_fail_get_not_existing_instance(test_client, self.collection)

    def test_fail_get_not_valid_id(self, test_client):
        asserts.asserts_fail_get_not_valid_id(test_client, self.collection)

    def test_delete_library(self, test_client, test_collection):
        asserts.asserts_delete_instance(test_client,
                                        self.collection,
                                        test_collection)

    def test_update_library(self, test_client, test_collection, test_collection_updated):
        asserts.asserts_update_instance(test_client,
                                        self.collection,
                                        test_collection,
                                        test_collection_updated)


@mark.cemeteries
class TestCemeteries:
    collection = 'cementerios'

    def test_get_cemeteries(self, test_client):
        asserts.asserts_get_instances(test_client, self.collection)

    def test_post_cemetery(self, test_client, test_collection):
        asserts.asserts_post_instance(test_client,
                                      self.collection,
                                      test_collection)

    def test_post_existing_cemetery(self, test_client, test_collection):
        asserts.asserts_post_existing_instance(test_client,
                                               self.collection,
                                               test_collection)

    def test_get_existing_cemetery(self, test_client, test_collection):
        asserts.asserts_get_existing_instance(test_client,
                                              self.collection,
                                              test_collection)

    def test_fail_get_not_existing_cemetery(self, test_client):
        asserts.asserts_fail_get_not_existing_instance(test_client, self.collection)

    def test_fail_get_not_valid_id(self, test_client):
        asserts.asserts_fail_get_not_valid_id(test_client, self.collection)

    def test_delete_cemetery(self, test_client, test_collection):
        asserts.asserts_delete_instance(test_client,
                                        self.collection,
                                        test_collection)

    def test_update_cemetery(self, test_client, test_collection, test_collection_updated):
        asserts.asserts_update_instance(test_client,
                                        self.collection,
                                        test_collection,
                                        test_collection_updated)


@mark.educational_centers
class TestEducationaCenters:
    collection = 'centros-educativos'

    def test_get_educational_centers(self, test_client):
        asserts.asserts_get_instances(test_client, self.collection)

    def test_post_educational_center(self, test_client, test_collection):
        asserts.asserts_post_instance(test_client,
                                      self.collection,
                                      test_collection)

    def test_post_existing_educational_center(self, test_client, test_collection):
        asserts.asserts_post_existing_instance(test_client,
                                               self.collection,
                                               test_collection)

    def test_get_existing_educational_center(self, test_client, test_collection):
        asserts.asserts_get_existing_instance(test_client,
                                              self.collection,
                                              test_collection)

    def test_fail_get_not_existing_educational_center(self, test_client):
        asserts.asserts_fail_get_not_existing_instance(test_client, self.collection)

    def test_fail_get_not_valid_id(self, test_client):
        asserts.asserts_fail_get_not_valid_id(test_client, self.collection)

    def test_delete_educational_center(self, test_client, test_collection):
        asserts.asserts_delete_instance(test_client,
                                        self.collection,
                                        test_collection)

    def test_update_educational_center(self, test_client, test_collection, test_collection_updated):
        asserts.asserts_update_instance(test_client,
                                        self.collection,
                                        test_collection,
                                        test_collection_updated)


@mark.fire_stations
class TestFireStations:
    collection = 'parques-de-bomberos'

    def test_get_fire_stations(self, test_client):
        asserts.asserts_get_instances(test_client, self.collection)

    def test_post_fire_station(self, test_client, test_collection):
        asserts.asserts_post_instance(test_client,
                                      self.collection,
                                      test_collection)

    def test_post_existing_fire_station(self, test_client, test_collection):
        asserts.asserts_post_existing_instance(test_client,
                                               self.collection,
                                               test_collection)

    def test_get_existing_fire_station(self, test_client, test_collection):
        asserts.asserts_get_existing_instance(test_client,
                                              self.collection,
                                              test_collection)

    def test_fail_get_not_existing_fire_station(self, test_client):
        asserts.asserts_fail_get_not_existing_instance(test_client, self.collection)

    def test_fail_get_not_valid_id(self, test_client):
        asserts.asserts_fail_get_not_valid_id(test_client, self.collection)

    def test_delete_fire_station(self, test_client, test_collection):
        asserts.asserts_delete_instance(test_client,
                                        self.collection,
                                        test_collection)

    def test_update_fire_station(self, test_client, test_collection, test_collection_updated):
        asserts.asserts_update_instance(test_client,
                                        self.collection,
                                        test_collection,
                                        test_collection_updated)


@mark.monuments
class TestMonuments:
    collection = 'monumentos'

    def test_get_monuments(self, test_client):
        asserts.asserts_get_instances(test_client, self.collection)

    def test_post_monument(self, test_client, test_collection):
        asserts.asserts_post_instance(test_client,
                                      self.collection,
                                      test_collection)

    def test_post_existing_monument(self, test_client, test_collection):
        asserts.asserts_post_existing_instance(test_client,
                                               self.collection,
                                               test_collection)

    def test_get_existing_monument(self, test_client, test_collection):
        asserts.asserts_get_existing_instance(test_client,
                                              self.collection,
                                              test_collection)

    def test_fail_get_not_existing_monument(self, test_client):
        asserts.asserts_fail_get_not_existing_instance(test_client, self.collection)

    def test_fail_get_not_valid_id(self, test_client):
        asserts.asserts_fail_get_not_valid_id(test_client, self.collection)

    def test_delete_monument(self, test_client, test_collection):
        asserts.asserts_delete_instance(test_client,
                                        self.collection,
                                        test_collection)

    def test_update_monument(self, test_client, test_collection, test_collection_updated):
        asserts.asserts_update_instance(test_client,
                                        self.collection,
                                        test_collection,
                                        test_collection_updated)


@mark.municipal_swimming_pools
class TestMunicipalSwimmingPools:
    collection = 'piscinas-municipales'

    def test_get_municipal_swimming_pools(self, test_client):
        asserts.asserts_get_instances(test_client, self.collection)

    def test_post_municipal_swimming_pool(self, test_client, test_collection):
        asserts.asserts_post_instance(test_client,
                                      self.collection,
                                      test_collection)

    def test_post_existing_municipal_swimming_pool(self, test_client, test_collection):
        asserts.asserts_post_existing_instance(test_client,
                                               self.collection,
                                               test_collection)

    def test_get_existing_municipal_swimming_pool(self, test_client, test_collection):
        asserts.asserts_get_existing_instance(test_client,
                                              self.collection,
                                              test_collection)

    def test_fail_get_not_existing_municipal_swimming_pool(self, test_client):
        asserts.asserts_fail_get_not_existing_instance(test_client, self.collection)

    def test_fail_get_not_valid_id(self, test_client):
        asserts.asserts_fail_get_not_valid_id(test_client, self.collection)

    def test_delete_municipal_swimming_pool(self, test_client, test_collection):
        asserts.asserts_delete_instance(test_client,
                                        self.collection,
                                        test_collection)

    def test_update_municipal_swimming_pool(self,
                                            test_client,
                                            test_collection,
                                            test_collection_updated):
        asserts.asserts_update_instance(test_client,
                                        self.collection,
                                        test_collection,
                                        test_collection_updated)


@mark.museums
class TestMuseums:
    collection = 'museos'

    def test_get_museums(self, test_client):
        asserts.asserts_get_instances(test_client, self.collection)

    def test_post_museum(self, test_client, test_collection):
        asserts.asserts_post_instance(test_client,
                                      self.collection,
                                      test_collection)

    def test_post_existing_museum(self, test_client, test_collection):
        asserts.asserts_post_existing_instance(test_client,
                                               self.collection,
                                               test_collection)

    def test_get_existing_museum(self, test_client, test_collection):
        asserts.asserts_get_existing_instance(test_client,
                                              self.collection,
                                              test_collection)

    def test_fail_get_not_existing_museum(self, test_client):
        asserts.asserts_fail_get_not_existing_instance(test_client, self.collection)

    def test_fail_get_not_valid_id(self, test_client):
        asserts.asserts_fail_get_not_valid_id(test_client, self.collection)

    def test_delete_museum(self, test_client, test_collection):
        asserts.asserts_delete_instance(test_client,
                                        self.collection,
                                        test_collection)

    def test_update_museum(self, test_client, test_collection, test_collection_updated):
        asserts.asserts_update_instance(test_client,
                                        self.collection,
                                        test_collection,
                                        test_collection_updated)


@mark.parks
class TestParks:
    collection = 'parques-y-jardines'

    def test_get_parks(self, test_client):
        asserts.asserts_get_instances(test_client, self.collection)

    def test_post_park(self, test_client, test_collection):
        asserts.asserts_post_instance(test_client,
                                      self.collection,
                                      test_collection)

    def test_post_existing_park(self, test_client, test_collection):
        asserts.asserts_post_existing_instance(test_client,
                                               self.collection,
                                               test_collection)

    def test_get_existing_park(self, test_client, test_collection):
        asserts.asserts_get_existing_instance(test_client,
                                              self.collection,
                                              test_collection)

    def test_fail_get_not_existing_park(self, test_client):
        asserts.asserts_fail_get_not_existing_instance(test_client, self.collection)

    def test_fail_get_not_valid_id(self, test_client):
        asserts.asserts_fail_get_not_valid_id(test_client, self.collection)

    def test_delete_park(self, test_client, test_collection):
        asserts.asserts_delete_instance(test_client,
                                        self.collection,
                                        test_collection)

    def test_update_park(self, test_client, test_collection, test_collection_updated):
        asserts.asserts_update_instance(test_client,
                                        self.collection,
                                        test_collection,
                                        test_collection_updated)


@mark.police_stations
class TestPoliceStations:
    collection = 'comisarias'

    def test_get_police_stations(self, test_client):
        asserts.asserts_get_instances(test_client, self.collection)

    def test_post_police_station(self, test_client, test_collection):
        asserts.asserts_post_instance(test_client,
                                      self.collection,
                                      test_collection)

    def test_post_existing_police_station(self, test_client, test_collection):
        asserts.asserts_post_existing_instance(test_client,
                                               self.collection,
                                               test_collection)

    def test_get_existing_police_station(self, test_client, test_collection):
        asserts.asserts_get_existing_instance(test_client,
                                              self.collection,
                                              test_collection)

    def test_fail_get_not_existing_police_station(self, test_client):
        asserts.asserts_fail_get_not_existing_instance(test_client, self.collection)

    def test_fail_get_not_valid_id(self, test_client):
        asserts.asserts_fail_get_not_valid_id(test_client, self.collection)

    def test_delete_police_station(self, test_client, test_collection):
        asserts.asserts_delete_instance(test_client,
                                        self.collection,
                                        test_collection)

    def test_update_police_station(self, test_client, test_collection, test_collection_updated):
        asserts.asserts_update_instance(test_client,
                                        self.collection,
                                        test_collection,
                                        test_collection_updated)


@mark.public_parkings
class TestPublicParkings:
    collection = 'aparcamientos-publicos-municipales'

    def test_get_public_parkings(self, test_client):
        asserts.asserts_get_instances(test_client, self.collection)

    def test_post_public_parking(self, test_client, test_collection):
        asserts.asserts_post_instance(test_client,
                                      self.collection,
                                      test_collection)

    def test_post_existing_public_parking(self, test_client, test_collection):
        asserts.asserts_post_existing_instance(test_client,
                                               self.collection,
                                               test_collection)

    def test_get_existing_public_parking(self, test_client, test_collection):
        asserts.asserts_get_existing_instance(test_client,
                                              self.collection,
                                              test_collection)

    def test_fail_get_not_existing_public_parking(self, test_client):
        asserts.asserts_fail_get_not_existing_instance(test_client, self.collection)

    def test_fail_get_not_valid_id(self, test_client):
        asserts.asserts_fail_get_not_valid_id(test_client, self.collection)

    def test_delete_public_parking(self, test_client, test_collection):
        asserts.asserts_delete_instance(test_client,
                                        self.collection,
                                        test_collection)

    def test_update_public_parking(self, test_client, test_collection, test_collection_updated):
        asserts.asserts_update_instance(test_client,
                                        self.collection,
                                        test_collection,
                                        test_collection_updated)


@mark.public_schools
class TestPublicSchools:
    collection = 'colegios-publicos'

    def test_get_public_schools(self, test_client):
        asserts.asserts_get_instances(test_client, self.collection)

    def test_post_public_school(self, test_client, test_collection):
        asserts.asserts_post_instance(test_client,
                                      self.collection,
                                      test_collection)

    def test_post_existing_public_school(self, test_client, test_collection):
        asserts.asserts_post_existing_instance(test_client,
                                               self.collection,
                                               test_collection)

    def test_get_existing_public_school(self, test_client, test_collection):
        asserts.asserts_get_existing_instance(test_client,
                                              self.collection,
                                              test_collection)

    def test_fail_get_not_existing_public_school(self, test_client):
        asserts.asserts_fail_get_not_existing_instance(test_client, self.collection)

    def test_fail_get_not_valid_id(self, test_client):
        asserts.asserts_fail_get_not_valid_id(test_client, self.collection)

    def test_delete_public_school(self, test_client, test_collection):
        asserts.asserts_delete_instance(test_client,
                                        self.collection,
                                        test_collection)

    def test_update_public_school(self, test_client, test_collection, test_collection_updated):
        asserts.asserts_update_instance(test_client,
                                        self.collection,
                                        test_collection,
                                        test_collection_updated)


@mark.recycling_points
class TestRecyclingPoints:
    collection = 'puntos-limpios'

    def test_get_recycling_points(self, test_client):
        asserts.asserts_get_instances(test_client, self.collection)

    def test_post_recycling_point(self, test_client, test_collection):
        asserts.asserts_post_instance(test_client,
                                      self.collection,
                                      test_collection)

    def test_post_existing_recycling_point(self, test_client, test_collection):
        asserts.asserts_post_existing_instance(test_client,
                                               self.collection,
                                               test_collection)

    def test_get_existing_recycling_point(self, test_client, test_collection):
        asserts.asserts_get_existing_instance(test_client,
                                              self.collection,
                                              test_collection)

    def test_fail_get_not_existing_recycling_point(self, test_client):
        asserts.asserts_fail_get_not_existing_instance(test_client, self.collection)

    def test_fail_get_not_valid_id(self, test_client):
        asserts.asserts_fail_get_not_valid_id(test_client, self.collection)

    def test_delete_recycling_point(self, test_client, test_collection):
        asserts.asserts_delete_instance(test_client,
                                        self.collection,
                                        test_collection)

    def test_update_recycling_point(self, test_client, test_collection, test_collection_updated):
        asserts.asserts_update_instance(test_client,
                                        self.collection,
                                        test_collection,
                                        test_collection_updated)
