

from model.group import Group

#Тест с заполненными данными

def test_test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(group_name="first group", header="Testing", footer="My first group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


    #Тест с незаполненными полями

def test_test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(group_name=" ", header=" ", footer=" "))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


