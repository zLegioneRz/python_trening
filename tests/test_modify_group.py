from model.group import Group

#Тест с заполненными данными

def test_test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modyfy_first_group_new(Group(group_name='New group'))
    app.session.logout()


def test_test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modyfy_first_group_new(Group(header='New group'))
    app.session.logout()


def test_test_modify_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modyfy_first_group_new(Group(footer='New group'))
    app.session.logout()