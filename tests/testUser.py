import pytest
from facade import *

user = User()


def test_get_all_users():
    response = user.get_all_users()
    assert response.status_code == 200


def test_get_one_user():
    user_logged = Login("raimundo@dcx.ufpb.br", "87654321")
    response = user.get_one_user(user_logged.token)
    assert response.status_code == 200
    assert response.json()["email"] == "raimundo@dcx.ufpb.br"


def test_create_new_user():
    response = user.create_new_user("Marcos", user.mail_generation(), "123456789")
    assert response.status_code == 201
    assert response.json()["name"] == "Marcos"


def test_update_user():
    user_update = {
        "name": "Updated",
    }
    user_logged = Login("raimundo@dcx.ufpb.br", "87654321")
    response = user.update_user_obj(user_logged.token, user_update)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated"


