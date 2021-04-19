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
