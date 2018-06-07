from model.group import Group
from random import randrange

#Тест с заполненными данными

def test_test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len((old_groups)))
    group = Group(group_name='New group')
    group.id = old_groups[index].id
    app.group.modyfy_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



# def test_test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(group_name="test"))
#     old_groups = app.group.get_group_list()
#     group = Group(header='New header')
#     group.id = old_groups[0].id
#     app.group.modyfy_first_group_new(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#
# def test_test_modify_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(group_name="test"))
#     old_groups = app.group.get_group_list()
#     group = Group(footer='New footer')
#     group.id = old_groups[0].id
#     app.group.modyfy_first_group_new(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
