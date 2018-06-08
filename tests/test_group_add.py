from model.group import Group

def test_group_add(app, json_groups):
    group = json_groups
    old_group_list = app.group.get_group_list()
    # print("\n".join(map(str, old_group_list)))
    app.group.create(group)
    assert len(old_group_list) + 1 == app.group.count()
    new_group_list = app.group.get_group_list()
    # print(sorted(new_group_list, key=Group.id_or_max))
    old_group_list.append(group)
    # print(sorted(old_group_list, key=Group.id_or_max))
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)