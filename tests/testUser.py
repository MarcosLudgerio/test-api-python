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


def test_get_one_user():
    user_logged = Login("raimundo@dcx.ufpb.br", "87654321")
    response = user.get_one_user(user_logged.token)
    assert response.status_code == 200
    assert response.json()["email"] == "raimundo@dcx.ufpb.br"


