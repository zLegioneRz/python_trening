
import pytest
from model.group import Group
from data.add_group import testdata
import string

#Тест с заполненными данными

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
        # pass
        old_groups = app.group.get_group_list()
        #group = Group(group_name="first group", header="Testing", footer="My first group")
        app.group.create(group)
        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

