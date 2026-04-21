import requests


class Post:
    def __init__(self, id):
        self.post_num = id-1
        self.url = f"https://api.npoint.io/1ad80cb61d6c22baaaaf/{self.post_num}/"
        self.response = requests.get(self.url)
        self.content = self.response.json()
        self.title = self.content['title']
        self.body = self.content['body']
