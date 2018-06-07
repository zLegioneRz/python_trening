# -*- coding: utf-8 -*-
from fixture.application import Application
from model.contact import Contakt


def test_add_new_cont(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contakt(firstname="Test", midlname="testovich", lastname="Testov", nickname="Testikus",
                                     titl="Testi", company="Sirena-test", adress="1st test street", home_num="4",
                                     mob_nomber="7999999999", work_num="89999999999", fax="12", mail1="l@leg.er",
                                     mail2="2@leg.er", mail3="1l@leg.er", homepage="home", beyer="1988", ayer="1981",
                                     adress2="2nd street", home2="42", notes="good job")
    app.contact.add_new_cont(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contakt.id_or_max) == sorted(new_contact, key=Contakt.id_or_max)
