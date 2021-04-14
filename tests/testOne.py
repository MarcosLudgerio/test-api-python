from external import InitialTest, User

objTest = InitialTest("https://api-course-test-automatized.herokuapp.com")


def test_email_first_user():
    response = objTest.status_code_connection()
    assert response == 200


def test_all_users():
    response = objTest.get_all_users()
    assert len(response) == 9


def test_get_one_user():
    response = objTest.login("raimundo@dcx.ufpb.br", "87654321")
    response = objTest.get_one_user(response.text)
    user = User(response["id"], response["name"], response["email"], response["posts"])
    assert user.get_email() == "raimundo@dcx.ufpb.br"
    assert user.get_name() == "Marcos Ludgério"

