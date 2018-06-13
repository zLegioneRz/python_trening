from model.group import Group

def test_group_add(app, orm, json_groups, check_ui):
    group = json_groups
    old_group_list = orm.get_group_list()
    app.group.create_new(group)
    new_group_list = orm.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        print("Проверка пользовательского интерфейса")
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
