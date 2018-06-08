from model.contact import Contakt

def test_contact_add(app, json_contacts):
    contact = json_contacts
    old_contact_list = app.contact.get_contact_list()
    app.contact.create_new_cont(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contakt.id_or_max) == sorted(new_contact_list, key=Contakt.id_or_max)
