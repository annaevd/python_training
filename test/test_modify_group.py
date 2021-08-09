from model.group import Group


def test_modify_group_name(app):
    app.group.ensure_not_empty_groups_list(Group(name="First"))
    old_groups = app.group.get_group_list()
    group = Group(name="ModifyName")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     app.group.ensure_not_empty_groups_list(Group(name="First"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="ModifyHeader"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

