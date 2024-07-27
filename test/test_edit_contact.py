from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Anna", middlename="Maria", lastname="Tener", nickname="annate",
            title="Title Anna", company="Company Anna", address="Address Anna",
            tel_home="+79215674523", tel_mobile="+79991111111", tel_work="+7888222222", tel_fax="+77773333333",
            email="anna@test.ru", email2="anna2@test.ru", email3="anna3@test.ru",
            homepage="http://localhost/addressbook/",
            bday="1", bmonth="January", byear="1911", aday="17", amonth="March", ayear="2021"))
    app.contact.edit_first_contact(Contact(
            firstname="Anna update", middlename="Maria update", lastname="Tener update", nickname="annate update",
            title="Title Anna update", company="Company Anna update", address="Address Anna update",
            tel_home="+79215674523", tel_mobile="+79991111111", tel_work="+7888222222", tel_fax="+77773333333",
            email="annaupdate@test.ru",email2="anna2update@test.ru", email3="anna3update@test.ru",
            homepage="http://localhost/addressbook/",
            bday="2", bmonth="October", byear="2022", aday="22", amonth="June", ayear="2022"))


def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Anna", middlename="Maria", lastname="Tener", nickname="annate",
            title="Title Anna", company="Company Anna", address="Address Anna",
            tel_home="+79215674523", tel_mobile="+79991111111", tel_work="+7888222222", tel_fax="+77773333333",
            email="anna@test.ru", email2="anna2@test.ru", email3="anna3@test.ru",
            homepage="http://localhost/addressbook/",
            bday="1", bmonth="January", byear="1911", aday="17", amonth="March", ayear="2021"))
    app.contact.edit_first_contact(Contact(firstname="New Anna update"))


def test_edit_first_contact_bmonth(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Anna", middlename="Maria", lastname="Tener", nickname="annate",
            title="Title Anna", company="Company Anna", address="Address Anna",
            tel_home="+79215674523", tel_mobile="+79991111111", tel_work="+7888222222", tel_fax="+77773333333",
            email="anna@test.ru", email2="anna2@test.ru", email3="anna3@test.ru",
            homepage="http://localhost/addressbook/",
            bday="1", bmonth="January", byear="1911", aday="17", amonth="March", ayear="2021"))
    app.contact.edit_first_contact(Contact(bmonth="December"))