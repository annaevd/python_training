from model.group import Group


def test_delete_first_group(app):
    app.group.ensure_not_empty_groups_list(Group(name="First"))
    app.group.delete_first_group()
