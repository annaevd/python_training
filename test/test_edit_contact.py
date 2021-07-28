from model.contact import Contact

def test_add_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.edit_first_contact(Contact(firstname='Anna_new', lastname='Evdokimova_new', address='Saint-Petersburg_new', home='+79219999999', email='testnew@test.ru'))
    app.session.logout()