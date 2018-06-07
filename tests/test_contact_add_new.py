# -*- coding: utf-8 -*-
from fixture.application import Application
from model.contact import Contakt
import random
import string


def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata=[Contakt(firstname="", midlname="", lastname="", nickname="",
                                     titl="", company="", adress="", home_num="",
                                     mob_nomber="", work_num="", fax="", mail1="",
                                     mail2="", mail3="", homepage="", beyer="", ayer="",
                                     adress2="", home2="", notes="")] + [

Contakt(firstname=random_string("firstname", 10), midlname=random_string("midlname", 10), lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                                     titl=random_string("titl", 10), company=random_string("company", 10), adress=random_string("adress", 10), home_num=random_string("home_num", 10),
                                     mob_nomber=random_string("mob_nomber", 10), work_num=random_string("work_num", 10), fax=random_string("fax", 10), mail1=random_string("mail1", 10),
                                     mail2=random_string("mail2", 10), mail3=random_string("mail3", 10), homepage=random_string("homepage", 10), beyer=random_string("beyer", 10), ayer=random_string("ayer", 10),
                                     adress2=random_string("adress2", 10), home2=random_string("home2", 10), notes=random_string("notes", 10))
]
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_cont(app,contact):
    old_contacts = app.contact.get_contact_list()
     # contact = Contakt(firstname="Test", midlname="testovich", lastname="Testov", nickname="Testikus",
     #                                 titl="Testi", company="Sirena-test", adress="1st test street", home_num="4",
     #                                 mob_nomber="7999999999", work_num="89999999999", fax="12", mail1="l@leg.er",
     #                                 mail2="2@leg.er", mail3="1l@leg.er", homepage="home", beyer="1988", ayer="1981",
     #                                 adress2="2nd street", home2="42", notes="good job")
    app.contact.add_new_cont(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contakt.id_or_max) == sorted(new_contact, key=Contakt.id_or_max)
