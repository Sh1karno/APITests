from wrappers.base_request import BaseRequest


class Dogs(BaseRequest):

    def __init__(self):
        super(Dogs, self).__init__(base_url="https://dog.ceo")

    def get_all_breeds_list(self):
        return self.get('/api/breeds/list/all')

    def get_multiple_img_from_breeds(self, count):
        return self.get(f'/api/breeds/image/random/{count}')

    def get_img_from_breed(self, breed):
        return self.get(f'/api/breed/{breed}/images/random')

    def get_all_sub_breeds_list(self, sub_breed):
        return self.get(f'/api/breed/{sub_breed}/list')

    def get_img_from_sub_breed(self, breed, sub_breed):
        return self.get(f'/api/breed/{breed}/{sub_breed}/images/random')
