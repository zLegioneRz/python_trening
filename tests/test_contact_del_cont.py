from model.contact import Contact
import random


def test_del_some_contact(app, orm, check_ui):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_new(Contact(nickname="New"))
    old_contact_list = orm.get_contact_list()
    contact = random.choice(old_contact_list)
    app.contact.del_contact_by_id(contact.id)
    new_contact_list = orm.get_contact_list()
    old_contact_list.remove(contact)
    assert old_contact_list == new_contact_list
    if check_ui:
        print("Проверка пользовательского интерфейса")
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)