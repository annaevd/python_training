from model.contact import Contact


def test_edit_contact(app):
    app.contact.ensure_not_empty_contact_list(Contact(firstname="First"))
    app.contact.edit_first_contact(Contact(firstname='Anna_new', lastname='Evdokimova_new', address='Saint-Petersburg_new', home='+79219999999', email='testnew@test.ru'))
