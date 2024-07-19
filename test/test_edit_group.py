from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Update name group", header="Update header group", footer="Update footer group"))
    app.session.logout()