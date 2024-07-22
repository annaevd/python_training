from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="Update name group", header="Update header group", footer="Update footer group"))


def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="Update name group"))


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="Update header group"))