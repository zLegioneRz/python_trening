from model.group import Group

def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="Ooops"))
    app.group.modify_first_group(Group(group_name="Got us", header="Whynull", footer="New footer"))
