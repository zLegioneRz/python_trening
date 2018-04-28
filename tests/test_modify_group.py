from model.group import Group

def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(group_name="null",header="null",footer="null", group_name_new="modify name", header_new="mod header", footer_new="Oops it`s new footer"))
    app.session.logout()