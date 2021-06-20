import pytest

from unittest.mock import patch


@pytest.mark.breweries
class TestBreweriesAPI:

    def test_breweries_list(self, breweries, status_code):
        response = breweries.get_breweries_list()
        assert response.status_code == int(status_code)

    def test_random_breweries_by_city(self, breweries, status_code, random_breweries):
        response = breweries.get_breweries_by_city(random_breweries.get("city"))
        assert response.status_code == int(status_code)

    @pytest.mark.parametrize("state", ["New York", "Alabama", "Alaska"])
    def test_breweries_by_state(self, breweries, status_code, state):
        response = breweries.get_breweries_by_state(state)
        assert response.status_code == int(status_code)

    def test_breweries_by_name_and_sort(self, breweries, status_code, sorted_response_by_id):
        response = breweries.get_sorted_breweries_by_name("Alameda", '+id')
        assert response.status_code == int(status_code)
        assert response.json() == sorted_response_by_id

    @pytest.mark.parametrize("count", [0, 1, 15, 21, 50])
    def test_breweries_count_in_page(self, breweries, status_code, count):
        response = breweries.get_breweries_count_in_page(count)
        assert response.status_code == int(status_code)
        assert len(response.json()) == count
