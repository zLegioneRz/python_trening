# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_mod_some_cotact(app, orm, check_ui):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_new(Contact(firstname="New"))
    old_contact_list = orm.get_contact_list()
    new_contact = Contact(firstname="NEW NAME")
    mod_contact = random.choice(old_contact_list)
    new_contact.id = mod_contact.id
    if new_contact.firstname is None:
        new_contact.firstname = mod_contact.firstname
    if new_contact.lastname is None:
        new_contact.lastname = mod_contact.lastname
    app.contact.mod_contact_by_id(new_contact)
    new_contact_list = orm.get_contact_list()
    old_contact_list.remove(mod_contact)
    old_contact_list.append(new_contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        print("Проверка пользовательского интерфейса")
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)