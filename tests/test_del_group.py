from model.group import Group



def test_test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    app.group.delete_first_group()

