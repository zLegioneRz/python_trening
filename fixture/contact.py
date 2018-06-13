from selenium.webdriver.support.ui import Select
import re
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new(self, contact):
        wd = self.app.wd
        self.add_new_contact(wd)
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.go_to_page_home()
        self.contact_cash = None

    def go_to_page_home(self):
        wd = self.app.wd

        if not (wd.current_url.endswith("/addressbook") and
                len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # ФИО+nickname
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # данные компании
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        # адресс 1
        self.change_field_value("address", contact.address)
        # телефоны
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        # почта
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # даты
        self.pick_year_data("//select[@name='bday']", contact.birthday_date)
        self.pick_year_data("//select[@name='bmonth']", contact.birthday_month)
        self.change_field_value("byear", contact.byear)
        self.pick_year_data("//select[@name='aday']", contact.anniversary_date)
        self.pick_year_data("//select[@name='amonth']", contact.anniversary_month)
        self.change_field_value("ayear", contact.ayear)
        # адресс 2
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.secondary_phone)  # странно что "HOME" нашелся по имени "phone2"
        # заметка
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def pick_year_data(self, xpath_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_xpath(xpath_name)).select_by_value(text)

    def add_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def del_first_contact(self):
        self.del_contact_by_index(0)

    def del_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_page_home()
        # выбрать 1 контакт
        self.select_contact_by_index(index)
        # нажать на "удалить"
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.go_to_page_home()
        self.contact_cash = None

    def del_contact_by_id(self, id):
        wd = self.app.wd
        self.go_to_page_home()
        # выбрать 1 контакт
        self.select_contact_by_id(id)
        # нажать на "удалить"
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.go_to_page_home()
        self.contact_cash = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath(".//input[@value='%s']" % id).click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def mod_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.go_to_page_home()
        self.select_edit_button_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        # прейти на страницу с контактами
        self.go_to_page_home()
        self.contact_cash = None

    def mod_contact_by_id(self, new_contact_data):
        wd = self.app.wd
        self.go_to_page_home()
        self.select_edit_button_by_id(new_contact_data.id)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        # прейти на страницу с контактами
        self.go_to_page_home()
        self.contact_cash = None

    def select_edit_button_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def select_edit_button_by_id(self, id):
        wd = self.app.wd
        for row in wd.find_elements_by_name("entry"):
            if len(row.find_elements_by_xpath(".//input[@id='%s']" % id)) == 1:
                row.find_element_by_xpath(".//img[@alt='Edit']").click()
                break


    def mod_first_contact(self, new_contact_data):
        self.mod_contact_by_index(0, new_contact_data)

    def count(self):
        wd = self.app.wd
        self.go_to_page_home()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash = None

    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.go_to_page_home()
            self.contact_cash = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("id")
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cash.append(
                    Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                            all_emails_from_home_page=all_emails,
                            all_phones_from_home_page=all_phones))
        return self.contact_cash

    def get_contact_from_home_page_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        cells = row.find_elements_by_tag_name("td")
        lastname = cells[1].text
        firstname = cells[2].text
        id = row.find_element_by_name("selected[]").get_attribute("id")
        address = cells[3].text
        all_emails=cells[4].text
        all_phones = cells[5].text
        contact = Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                          all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails)
        return contact

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.go_to_page_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.go_to_page_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page_by_index(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute('value')
        address = wd.find_element_by_name("address").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        fax = wd.find_element_by_name("fax").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       address=address, home_phone=home_phone,
                       email=email, email2=email2, email3=email3, work_phone=work_phone,
                       mobile_phone=mobile_phone, fax=fax, secondary_phone=secondary_phone)

    def get_contact_from_view_page_by_index(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text)
        if home_phone is not None:
            home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text)
        if work_phone is not None:
            work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text)
        if mobile_phone is not None:
            mobile_phone = re.search("M: (.*)", text).group(1)
        fax = re.search("F: (.*)", text)
        if fax is not None:
            fax = re.search("F: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text)
        if secondary_phone is not None:
            secondary_phone = re.search("P: (.*)", text).group(1)
        all_phones="\n".join(filter(lambda x: x != "",
                                (map(lambda x: self.clear(x),
                                     filter(lambda x: x is not None,
                                            [home_phone, mobile_phone,
                                             work_phone, fax, secondary_phone])))))
        # return Contact(home_phone=home_phone, work_phone=work_phone,
        #            mobile_phone=mobile_phone, fax = fax, secondary_phone=secondary_phone)
        return Contact(all_phones_from_view_page=all_phones)



    def clear(self, phone):
        return re.sub("[() -]", "", phone)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                (map(lambda x: self.clear(x),
                                     filter(lambda x: x is not None,
                                            [contact.home_phone, contact.mobile_phone,
                                             contact.work_phone, contact.secondary_phone])))))


    def merge_phones_like_on_home_view_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                (map(lambda x: self.clear(x),
                                     filter(lambda x: x is not None,
                                            [contact.home_phone, contact.mobile_phone,
                                             contact.work_phone, contact.fax, contact.secondary_phone])))))


    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))

    def add_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.go_to_page_home()
        self.select_contact_by_id(contact_id)
        self.select_groups_by_value('to_group', group_id)
        wd.find_element_by_name('add').click()
        self.go_to_page_home()

    def select_groups_by_value(self, menu_name, value):
        wd = self.app.wd
        select = Select(wd.find_element_by_name(menu_name))
        select.select_by_value(value)


    def remove_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.go_to_page_home()
        self.select_groups_by_value('group', group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name('remove').click()
        self.go_to_page_home()
        self.select_groups_by_value('group', "")