import pytest
import requests


@pytest.mark.breweries
class TestBreweriesAPI:

    def test_list_breweries(self, base_url, status_code):
        response = requests.get(base_url + '/breweries')
        assert response.status_code == int(status_code)

    def test_random_breweries_by_city(self, base_url, status_code, get_random_breweries):
        response = requests.get(base_url + f'/breweries?by_city={get_random_breweries.get("city")}')
        assert response.status_code == int(status_code)

    @pytest.mark.parametrize("state", ["New York", "Alabama", "Alaska"])
    def test_breweries_by_state(self, base_url, status_code, state):
        response = requests.get(base_url + '/breweries',
                                params={'state': state})
        assert response.status_code == int(status_code)

    def test_breweries_by_name_and_sort(self, base_url, status_code, get_sorted_response_by_id):
        response = requests.get(base_url + '/breweries?by_city=Alameda&sort=+id')
        assert response.status_code == int(status_code)
        assert response.json() == get_sorted_response_by_id

    @pytest.mark.parametrize("count", [0, 1, 15, 21, 50])
    def test_breweries_count_in_page(self, base_url, status_code, count):
        response = requests.get(base_url + f'/breweries?per_page={count}')
        assert response.status_code == int(status_code)
        assert len(response.json()) == count
