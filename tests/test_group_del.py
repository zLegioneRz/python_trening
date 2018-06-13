# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_del_some_group(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.create_new(Group(name="NEW"))
    old_group_list = orm.get_group_list()
    group = random.choice(old_group_list)
    app.group.del_group_by_id(group.id)
    new_group_list = orm.get_group_list()
    old_group_list.remove(group)
    assert old_group_list == new_group_list
    if check_ui:
        print("Проверка пользовательского интерфейса")
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
