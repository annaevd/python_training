# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname='Anna', lastname='Evdokimova', address='Saint-Petersburg', home='+79211111111', email='test@test.ru'))
