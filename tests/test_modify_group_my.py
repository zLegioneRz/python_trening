from model.group import Group

def test_modify_group(app):
    app.group.modify_first_group(Group(group_name="Got us", header="Whynull", footer="New footer"))
    app.session.logout()