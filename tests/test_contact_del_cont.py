from model.contact import Contakt
from random import randrange


def test_test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_cont(Contakt(firstname="Test", midlname="testovich", lastname="Testov", nickname="Testikus",
                                     titl="Testi", company="Sirena-test", adress="1st test street", home_num="4",
                                     mob_nomber="7999999999", work_num="89999999999", fax="12", mail1="l@leg.er",
                                     mail2="2@leg.er", mail3="1l@leg.er", homepage="home", beyer="1988", ayer="1981",
                                     adress2="2nd street", home2="42", notes="good job"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    app.contact.delete_some_contact_by_index(index)
    assert len(old_contact_list) - 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list[index:index + 1] = []
    assert old_contact_list == new_contact_list