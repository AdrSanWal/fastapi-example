import json

from api import error_msg


def asserts_get_instances(test_client, collection):
    response = test_client.get(f"/{collection}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def asserts_post_instance(test_client, collection, test_collection):
    response = test_client.post(f"/{collection}", content=json.dumps(test_collection))
    assert response.status_code == 201


def asserts_post_existing_instance(test_client, collection, test_collection):
    test_client.post(f"/{collection}", content=json.dumps(test_collection))
    response = test_client.post(f"/{collection}", content=json.dumps(test_collection))
    assert response.status_code == 409


def asserts_get_existing_instance(test_client, collection, test_collection):
    response = test_client.post(f"/{collection}", content=json.dumps(test_collection))
    id = response.json()['id']
    response = test_client.get(f"/{collection}/{id}")
    assert response.status_code == 200

    response_element = dict(response.json())
    del response_element['id']
    assert response_element == test_collection


def asserts_fail_get_not_existing_instance(test_client, collection):
    id = '645b4d9e5f81141374088b6c'
    response = test_client.get(f"/{collection}/{id}")
    assert response.status_code == 400
    assert response.json()['detail'] == error_msg.instance_not_exists


def asserts_fail_get_not_valid_id(test_client, collection):
    id = 'invalid id'
    response = test_client.get(f"/{collection}/{id}")
    assert response.status_code == 400

    assert response.json()['detail'] == error_msg.invalid_id


def asserts_delete_instance(test_client, collection, test_collection):
    response = test_client.post(f"/{collection}", content=json.dumps(test_collection))
    id = response.json()['id']
    assert len(test_client.get(f"/{collection}").json()) == 1

    response = test_client.delete(f"/{collection}/{id}")
    assert response.status_code == 204

    assert len(test_client.get(f"/{collection}").json()) == 0


def asserts_update_instance(test_client, collection, test_collection, test_collection_updated):
    response = test_client.post(f"/{collection}", content=json.dumps(test_collection))
    id = response.json()['id']
    response = test_client.put(f"/{collection}/{id}",
                               content=json.dumps(test_collection_updated))
    assert response.status_code == 200

    updated_db_user = test_client.get(f"/{collection}/{id}").json()
    test_collection_updated['id'] = id
    assert updated_db_user == test_collection_updated
