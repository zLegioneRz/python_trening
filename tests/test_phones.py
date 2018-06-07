from model.contact import Contakt


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contakt(firstname="New",
                                       home_num="811113456",
                                       mob_nomber="79265314806",
                                       work_num="891115314806",
                                       fax="+79265314806",
                                       home2="199111154456"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_index(0)
    assert contact_from_home_page.all_phones_from_home_page == \
           app.contact.merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contakt(firstname="New",
                                       home_num="811123456",
                                       mob_nomber="7911114806",
                                       work_num="89265311116",
                                       fax="+79265311116",
                                       home2="199111154456"))
    contact_from_view_page = app.contact.get_contact_from_view_page_by_index(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_index(0)
    if contact_from_view_page.home_num is None:
        contact_from_view_page.home_num = contact_from_edit_page.home_num
    if contact_from_view_page.work_num is None:
        contact_from_view_page.work_num = contact_from_edit_page.work_num
    if contact_from_view_page.fax is None:
        contact_from_view_page.fax = contact_from_edit_page.fax
    if contact_from_view_page.mob_nomber is None:
        contact_from_view_page.mob_nomber = contact_from_edit_page.mob_nomber
    if contact_from_view_page.home2 is None:
        contact_from_view_page.home2 = contact_from_edit_page.home2
    assert contact_from_view_page.home_num == contact_from_edit_page.home_num
    assert contact_from_view_page.mob_nomber == contact_from_edit_page.mob_nomber
    assert contact_from_view_page.work_num == contact_from_edit_page.work_num
    assert contact_from_view_page.fax == contact_from_edit_page.fax
    assert contact_from_view_page.home2 == contact_from_edit_page.home2