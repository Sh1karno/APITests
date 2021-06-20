from wrappers.base_request import BaseRequest


class Breweries(BaseRequest):

    def __init__(self):
        super(Breweries, self).__init__(base_url="https://api.openbrewerydb.org")

    def get_breweries_list(self, params=None):
        return self.get('/breweries', params=params)

    def get_breweries_by_city(self, city):
        return self.get_breweries_list(params={'by_city': city})

    def get_breweries_by_state(self, state):
        return self.get_breweries_list(params={'state': state})

    def get_sorted_breweries_by_name(self, name, sorted_by):
        return self.get_breweries_list(params={'by_name': name, 'sorted_by': sorted_by})

    def get_breweries_count_in_page(self, count):
        return self.get_breweries_list(params={'per_page': count})
