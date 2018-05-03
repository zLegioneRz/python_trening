# -*- coding: utf-8 -*-
from fixture.application import Application
from model.contact import Contakt


def test_add_new_cont(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new_cont(Contakt(firstname="Test", midlname="testovich", lastname="Testov", nickname="Testikus",
                                     titl="Testi", company="Sirena-test", adress="1st test street", home_num="4",
                                     mob_nomber="7999999999", work_num="89999999999", fax="12", mail1="l@leg.er",
                                     mail2="2@leg.er", mail3="1l@leg.er", homepage="home", beyer="1988", ayer="1981",
                                     adress2="2nd street", home2="42", notes="good job",firstname_new="NewTest"))
    app.session.logout()
