from model.contact import Contakt


def test_test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_cont(Contakt(firstname="Test", midlname="testovich", lastname="Testov", nickname="Testikus",
                                     titl="Testi", company="Sirena-test", adress="1st test street", home_num="4",
                                     mob_nomber="7999999999", work_num="89999999999", fax="12", mail1="l@leg.er",
                                     mail2="2@leg.er", mail3="1l@leg.er", homepage="home", beyer="1988", ayer="1981",
                                     adress2="2nd street", home2="42", notes="good job"))
    old_contact_list = app.contact.get_contact_list()
    contact = Contakt(firstname="New Test Name")
    contact.id = old_contact_list[0].id
    if contact.firstname is None:
        contact.firstname = old_contact_list[0].firstname
    if contact.lastname is None:
        contact.lastname = old_contact_list[0].lastname
    app.contact.modify_first_cont(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact)
    old_contact_list[0] = contact
    # print(sorted(old_contact_list, key=Contakt.id_or_max))
    # print(sorted(new_contact, key=Contakt.id_or_max))
    assert sorted(old_contact_list, key=Contakt.id_or_max) == sorted(new_contact, key=Contakt.id_or_max)