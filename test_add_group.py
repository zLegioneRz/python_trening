# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

#Тест с заполненными данными

def test_test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(group_name="first group", header="Testing", footer="My first group"))
    app.logout()


    #Тест с незаполненными полями

def test_test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(group_name=" ", header=" ", footer=" "))
    app.logout()

