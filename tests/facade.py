import requests


class Login:
    response = {}
    endpoint = "/auth/login"
    token = ""

    def __init__(self, url, email, password):
        user = {"email": f"{email}", "password": f"{password}"}
        self.response = requests.post(f"{self.url}/auth/login", json=user)
        self.token = self.response.text

    def status_code_connection(self):
        return self.response.status_code

    def get_token(self):
        return self.token


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
