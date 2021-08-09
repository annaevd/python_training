from model.group import Group


def test_delete_first_group(app):
    app.group.ensure_not_empty_groups_list(Group(name="First"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)

