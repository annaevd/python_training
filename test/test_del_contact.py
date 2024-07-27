from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Anna", middlename="Maria", lastname="Tener", nickname="annate",
            title="Title Anna", company="Company Anna", address="Address Anna",
            tel_home="+79215674523", tel_mobile="+79991111111", tel_work="+7888222222", tel_fax="+77773333333",
            email="anna@test.ru", email2="anna2@test.ru", email3="anna3@test.ru",
            homepage="http://localhost/addressbook/",
            bday="1", bmonth="January", byear="1911", aday="17", amonth="March", ayear="2021"))
    app.contact.delete_first_contact()