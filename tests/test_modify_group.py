from model.group import Group

#Тест с заполненными данными

def test_test_modify_group_name(app):
    app.group.modyfy_first_group_new(Group(group_name='New group'))


def test_test_modify_group_header(app):
    app.group.modyfy_first_group_new(Group(header='New header'))


def test_test_modify_group_footer(app):
    app.group.modyfy_first_group_new(Group(footer='New footer'))
