from model.contact import Contakt


def test_test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_cont(Contakt(firstname="Test", midlname="testovich", lastname="Testov", nickname="Testikus",
                                     titl="Testi", company="Sirena-test", adress="1st test street", home_num="4",
                                     mob_nomber="7999999999", work_num="89999999999", fax="12", mail1="l@leg.er",
                                     mail2="2@leg.er", mail3="1l@leg.er", homepage="home", beyer="1988", ayer="1981",
                                     adress2="2nd street", home2="42", notes="good job"))
    old_contact = app.contact.get_contact_list()
    contact = Contakt(firstname="NewTest")
    contact.id = old_contact[0].id
    app.contact.modify_first_cont(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contakt.id_or_max) == sorted(new_contact, key=Contakt.id_or_max)