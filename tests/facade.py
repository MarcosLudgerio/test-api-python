from random import randint

import requests

base_url = "https://api-course-test-automatized.herokuapp.com"


class Login:
    response = {}
    endpoint = "/auth/login"
    token = ""

    def __init__(self, email, password):
        user = {"email": f"{email}", "password": f"{password}"}
        self.response = requests.post(f"{base_url}{self.endpoint}", json=user)
        self.token = self.response.text

    def status_code_connection(self):
        return self.response.status_code

    def get_token(self):
        return self.token

    def get_response(self):
        return self.response


class User:
    response = {}
    endpoint = "/users"
    cont_user = 0

    def __init__(self):
        self.response = requests.get(f"{base_url}{self.endpoint}")
        self.cont_user = len(self.response.json())

    def get_all_users(self):
        return self.response

    def get_one_user(self, token):
        headers = {"Authorization": token}
        self.response = requests.get(f"{base_url}{self.endpoint}/details", headers=headers)
        return self.response

    def get_status_code(self):
        return self.response.status_code

    def create_new_user_obj(self, user):
        self.response = requests.post(f"{base_url}{self.endpoint}", json=user)
        return self.response

    def create_new_user(self, name, email, password):
        user = {
            "name": name,
            "email": email,
            "password": password
        }
        return self.create_new_user_obj(user)

    def mail_generation(self):
        pt1 = "pt1" + str(randint(0, 999))
        pt2 = "m2" + str(randint(0, 999))
        pt3 = "a3d" + str(randint(0, 999))
        mail = pt1 + pt2 + pt3 + "@mail.com"
        return mail

    def update_user_obj(self, token, user):
        headers = {"Authorization": token}
        self.response = requests.put(f"{base_url}{self.endpoint}", headers=headers, json=user)
        return self.response
