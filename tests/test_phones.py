from model.contact import Contact


def test_phones_on_home_page(app, orm):
    if len(orm.get_group_list()) == 0:
        app.contact.create_new(Contact(firstname="New",
                                       home_phone="8495123456",
                                       mobile_phone="79265314806",
                                       work_phone="89265314806",
                                       fax="+79265314806",
                                       secondary_phone="199144654456"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_index(0)
    assert contact_from_home_page.all_phones_from_home_page == \
           app.contact.merge_phones_like_on_home_page(contact_from_edit_page)



def test_phones_on_contact_view_page(app, orm):
    if len(orm.get_group_list()) == 0:
        app.contact.create_new(Contact(firstname="New",
                                       home_phone="8495123456",
                                       mobile_phone="79265314806",
                                       work_phone="89265314806",
                                       fax="+79265314806",
                                       secondary_phone="199144654456"))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_index(0)
    contact_from_view_page = app.contact.get_contact_from_view_page_by_index(0)
    assert app.contact.merge_phones_like_on_home_view_page(contact_from_edit_page) == \
           contact_from_view_page.all_phones_from_view_page
