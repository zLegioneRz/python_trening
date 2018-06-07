from random import randrange
from model.contact import Contakt


def test_verify_random_contact_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.add_new_cont(Contakt(firstname="Alex",midlname="",lastname="asdf", nickname="tester",
                                         titl="sdaf", company="adsf-adsf",   adress="adsf",   home_num="32412341",
                                         mob_nomber="123413243241",work_num="123413241324", fax="+12341234",
                                         mail1="ldsf@inb33.ru", mail2="lu3322@1324.ru", mail3="123432@134.ru",
                                       homepage="dsasadf.ru", beyer="1980", birthday_month="November",
                                       year="1991", anniversary_date="31",anniversary_month="November", ayer="2000",
                                         adress2="Россия",home2="199144654456",notes="testin test"
        ))
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_from_home_page_by_index(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_index(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.adress == contact_from_edit_page.adress
    assert contact_from_home_page.all_emails_from_home_page == \
           app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == \
           app.contact.merge_phones_like_on_home_page(contact_from_edit_page)