import pytest
import requests
import random


@pytest.mark.dogs
class TestDogsAPI:

    def test_get_list_all_breed(self, base_url, status_code):
        response = requests.get(base_url + '/api/breeds/list/all')
        assert response.status_code == int(status_code)
        assert response.headers['content-type'] == 'application/json'
        assert response.json()['status'] == 'success'
        assert len(response.json()['message']) == 94

    def test_get_multiple_random_img_from_breed(self, base_url, status_code):
        random_count = random.randint(1, 10)
        response = requests.get(base_url + f'/api/breeds/image/random/{random_count}')
        assert response.status_code == int(status_code)
        assert response.headers['content-type'] == 'application/json'
        assert response.json()['status'] == 'success'
        assert len(response.json()['message']) == random_count

    # This test uses a random breed generation fixture
    def test_get_random_img_from_breed(self, base_url, status_code, get_random_breed):
        response = requests.get(base_url + f'/api/breed/{get_random_breed}/images/random')
        assert response.status_code == int(status_code)
        assert response.headers['content-type'] == 'application/json'
        assert response.json()['status'] == 'success'

    @pytest.mark.parametrize("sub_breed, count_sub_breed", [('hound', 7), ('poodle', 3), ('retriever', 4)])
    def test_get_list_all_sub_breeds(self, base_url, status_code, sub_breed, count_sub_breed):
        response = requests.get(base_url + f'/api/breed/{sub_breed}/list')
        assert response.status_code == int(status_code)
        assert response.headers['content-type'] == 'application/json'
        assert response.json()['status'] == 'success'
        assert len(response.json()['message']) == count_sub_breed

    @pytest.mark.parametrize("breed, sub_breed", [('hound', 'afghan'), ('hound', 'blood'), ('bulldog', 'french')])
    def test_get_random_img_from_sub_breed(self, base_url, status_code, breed, sub_breed):
        response = requests.get(base_url + f'/api/breed/{breed}/{sub_breed}/images/random')
        assert response.status_code == int(status_code)
        assert response.headers['content-type'] == 'application/json'
        assert response.json()['status'] == 'success'
