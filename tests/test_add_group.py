# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

#Тест с заполненными данными

def test_test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="first group", header="Testing", footer="My first group"))
    app.session.logout()


    #Тест с незаполненными полями

def test_test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name=" ", header=" ", footer=" "))
    app.session.logout()

