from model.contact import Contact


def test_delete_first_contact(app):
    app.contact.ensure_not_empty_contact_list(Contact(firstname="First"))
    app.contact.delete_first_contact()
