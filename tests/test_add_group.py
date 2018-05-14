

from model.group import Group

#Тест с заполненными данными

def test_test_add_group(app):
    app.group.create(Group(group_name="first group", header="Testing", footer="My first group"))




    #Тест с незаполненными полями

def test_test_add_empty_group(app):
    app.group.create(Group(group_name=" ", header=" ", footer=" "))


