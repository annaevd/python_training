from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(
            firstname="Anna update", middlename="Maria update", lastname="Tener update", nickname="annate update",
            title="Title Anna update", company="Company Anna update", address="Address Anna update",
            tel_home="+79215674523", tel_mobile="+79991111111", tel_work="+7888222222", tel_fax="+77773333333",
            email="annaupdate@test.ru",email2="anna2update@test.ru", email3="anna3update@test.ru",
            homepage="http://localhost/addressbook/",
            bday="2", bmonth="January", byear="2022", aday="22", amonth="June", ayear="2022"))
    app.session.logout()