import requests


class MockDogsResponse(requests.Response):

    def __init__(self, count=0):
        super(MockDogsResponse, self).__init__()
        self.headers = {'content-type': 'application/json'}
        self.status_code = 200
        self.count = count

    def json(self):
        return {"message": range(self.count), 'status': 'success'}
