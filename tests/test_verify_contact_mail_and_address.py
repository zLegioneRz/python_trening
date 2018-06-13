from model.contact import Contact


def test_verify_random_contact_on_home_page(app, orm):
    if len(orm.get_group_list()) == 0:
        app.contact.create_new(Contact(
            # ФИО+nickname
            firstname="Ivanov",
            middlename="",
            lastname="Ivan",
            nickname="tester",
            # данные компании
            title="junior",
            company="sirena-testl",
            # адресс 1
            address="MSK",
            # телефоны
            home_phone="123654789",
            mobile_phone="3214569875",
            work_phone="7596845986",
            fax="+7585852585",
            # почта
            email="ivanov@inbox.ru",
            email2="ivanov2@inbox.ru",
            email3="ivanov2@inbox.ru",
            homepage="ivanov.ru",
            # выбор дат
            birthday_date="13",
            birthday_month="November",
            byear="1980",
            anniversary_date="1",
            anniversary_month="November",
            ayear="2010",
            # адресс 2
            address2="Россия",
            secondary_phone="199144654456",
            # заметка
            notes="testin test"
        ))
    contacts_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_db = sorted(orm.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_ui) == len(contacts_db)
    for i in range(len(contacts_ui)):
        assert contacts_ui[i].firstname == contacts_db[i].firstname
        assert contacts_ui[i].lastname == contacts_db[i].lastname
        assert contacts_ui[i].address == contacts_db[i].address
        assert contacts_ui[i].all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contacts_db[i])
        assert contacts_ui[i].all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contacts_db[i])


