

from model.group import Group


#Тест с заполненными данными

def test_test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="first group", header="Testing", footer="My first group")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    #Тест с незаполненными полями

def test_test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


