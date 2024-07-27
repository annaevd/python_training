from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name group for MODIFY", header="Header group for MODIFY", footer="Footer group for MODIFY"))
    app.group.edit_first_group(Group(name="Update name group", header="Update header group", footer="Update footer group"))


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name group for MODIFY", header="Header group for MODIFY", footer="Footer group for MODIFY"))
    app.group.edit_first_group(Group(name="Update only name group"))


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name group for MODIFY", header="Header group for MODIFY", footer="Footer group for MODIFY"))
    app.group.edit_first_group(Group(header="Update only header group"))