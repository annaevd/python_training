from model.group import Group

def test_edit_group(app):
    app.group.edit_first_group(Group(name="TestName_new", header="TestHeader_new", footer="TestFooter_new"))
