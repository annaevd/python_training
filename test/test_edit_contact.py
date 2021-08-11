from model.contact import Contact


def test_edit_contact(app):
    app.contact.ensure_not_empty_contact_list(Contact(firstname="First"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='Anna_new', lastname='Evdokimova_new', address='Saint-Petersburg_new', home='+79219999999', email='testnew@test.ru')
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
