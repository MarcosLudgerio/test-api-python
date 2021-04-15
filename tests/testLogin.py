from facade import *

login = Login("https://api-course-test-automatized.herokuapp.com")


def test_email_first_user():
    response = login.status_code_connection()
    assert response == 200


def test_all_users():
    response = login.get_all_users()
    assert len(response) == 9


def test_get_one_user():
    response = login.login("raimundo@dcx.ufpb.br", "87654321")
    response = login.get_one_user(response.text)
    user = User(response["id"], response["name"], response["email"], response["posts"])
    assert user.get_email() == "raimundo@dcx.ufpb.br"
    assert user.get_name() == "Marcos Ludgério"

