from facade import *


def test_login_success():
    login = Login("raimundo@dcx.ufpb.br", "87654321")
    response = login.status_code_connection()
    assert response == 200


def test_try_login_with_error_in_password():
    login = Login("raimundo@dcx.ufpb.br", "12345")
    response = login.get_response().json()
    assert login.get_response().status_code == 401
    assert response["erros"][0] == "Falha ao tentar efetuar o login, verifique os dados e tente novamente"


def test_try_login_with_account_not_exist():
    login = Login("nao@existe.com", "12345")
    response = login.get_response().json()
    assert login.get_response().status_code == 400
    assert response["erros"][0] == "Usuário não encontrado, verifique os dados e tente novamente"


def test_try_login_with_invalid_email():
    login = Login("raimundo", "12345")
    response = login.get_response().json()
    assert login.get_response().status_code == 400
    assert response["erros"][0] == "O email precisa ser válido"


def test_login_error_without_email():
    login = Login("", "87654321")
    response = login.get_response().json()
    assert login.get_response().status_code == 400
    assert response["erros"][0] == "Campo email é obrigatório"


def test_login_without_password():
    login = Login("raimundo@dcx.ufpb.br", "")
    response = login.get_response().json()
    assert login.get_response().status_code == 400
    assert response["erros"][0] == "Campo senha é obrigatório"

