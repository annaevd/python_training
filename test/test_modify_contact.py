from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    app.contact.ensure_not_empty_contact_list(Contact(firstname="First"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname='NameModify', lastname='Evdokimova_new', address='Saint-Petersburg_new', home='+79219999999', email='testnew@test.ru')
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
