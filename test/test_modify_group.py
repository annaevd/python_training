from model.group import Group


def test_modify_group_name(app):
    app.group.ensure_not_empty_groups_list(Group(name="First"))
    app.group.modify_first_group(Group(name="ModifyName"))


def test_modify_group_header(app):
    app.group.ensure_not_empty_groups_list(Group(name="First"))
    app.group.modify_first_group(Group(header="ModifyHeader"))
