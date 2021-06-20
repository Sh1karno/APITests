from wrappers.base_request import BaseRequest


class Placeholder(BaseRequest):
    
    def __init__(self):
        super(Placeholder, self).__init__(base_url="https://jsonplaceholder.typicode.com")

    def get_posts_list(self):
        return self.get('/posts')

    def get_comments_list(self):
        return self.get('/comments')

    def get_post(self, post_id):
        return self.get(f'/posts/{post_id}')

    def post_data(self, test_id, body, some_list):
        return self.post('/posts',
                         data={'testId': test_id,
                               'body': body,
                               'some_list': some_list})

    def put_data(self, post_id, test_id, body, some_list):
        return self.put(f'/posts/{post_id}',
                         data={'testId': test_id,
                               'body': body,
                               'some_list': some_list})
