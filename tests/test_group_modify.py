# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_mod_group_name(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.create_new(Group(name="NEW"))
    old_group_list = orm.get_group_list()
    new_group = Group(header="NEW NAME")
    mod_group = random.choice(old_group_list)
    new_group.id = mod_group.id
    if new_group.name is None:
        new_group.name = mod_group.name
    app.group.mod_group_by_id(new_group)
    new_group_list = orm.get_group_list()
    old_group_list.remove(mod_group)
    old_group_list.append(new_group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        print("Проверка пользовательского интерфейса")
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

