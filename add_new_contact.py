import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(
            firstname="Anna", middlename="Maria", lastname="Tener", nickname="annate",
            title="Title Anna", company="Company Anna", address="Address Anna",
            tel_home="+79215674523", tel_mobile="+79991111111", tel_work="+7888222222", tel_fax="+77773333333",
            email="anna@test.ru",email2="anna2@test.ru", email3="anna3@test.ru",
            homepage="http://localhost/addressbook/",
            bday="1", bmonth="January", byear="2002", aday="7", amonth="June", ayear="2021"))
    app.logout()