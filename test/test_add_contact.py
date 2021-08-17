# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='Marfa', lastname='Evdokimova', address='Saint-Petersburg', home='+79211111111',
                      mobile="+72222222222", work="+73333333333", fax="+744444444", email='test@test.ru')
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
