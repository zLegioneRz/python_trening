from model.contact import Contakt
from random import randrange

def test_test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_cont(Contakt(firstname="Test"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len((old_contact_list)))
    contact = Contakt(firstname="New_Test_Name")
    contact.id = old_contact_list[index].id
    if contact.firstname is None:
        contact.firstname = old_contact_list[index].firstname
    if contact.lastname is None:
        contact.lastname = old_contact_list[index].lastname
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contact_list) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact_list[index] = contact
    # print(old_contact_list)
    # print(new_contact)
    assert sorted(old_contact_list, key=Contakt.id_or_max) == sorted(new_contact, key=Contakt.id_or_max)