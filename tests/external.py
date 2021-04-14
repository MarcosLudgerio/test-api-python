import requests


class InitialTest:
    response = {}
    url = ""
    endpoint = "/users"

    def __init__(self, url):
        self.response = requests.get(f"{url}{self.endpoint}")
        self.url = url

    def status_code_connection(self):
        return self.response.status_code

    def login(self, email, password):
        user = {"email": f"{email}", "password": f"{password}"}
        headers = {'content-type': 'application/json'}
        token = requests.post(f"{self.url}/auth/login", json=user, headers=headers)
        return token

    def get_all_users(self):
        return self.response.json()

    def get_one_user(self, token):
        headers = {'Authorization': token}
        user = requests.get(f"{self.url}{self.endpoint}/details", headers=headers)
        return user.json()


class User:
    identify = 0
    name = ""
    email = ""
    posts = []

    def __init__(self, identify, name, email, posts):
        self.identify = identify
        self.name = name
        self.email = email
        self.posts = posts

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_posts(self):
        return self.posts
