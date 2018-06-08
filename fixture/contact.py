from model.contact import Contakt
import re
from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create_new_cont(self,Contakt):
        wd = self.app.wd
        self.add_new_cont()
        self.fill_contact_form(Contakt)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_home_page()
        self.contact_cache = None

    def fill_contact_form(self, Contakt):
        wd = self.app.wd
        #Name
        self.change_field_value("firstname", Contakt.firstname)
        self.change_field_value("middlename", Contakt.midlname)
        self.change_field_value("lastname", Contakt.lastname)
        self.change_field_value("nickname", Contakt.nickname)
        # Company
        self.change_field_value("title", Contakt.titl)
        self.change_field_value("company", Contakt.company)
        # Adress
        self.change_field_value("address", Contakt.adress)
        # Tel:
        self.change_field_value("home", Contakt.home_num)
        self.change_field_value("mobile", Contakt.mob_nomber)
        self.change_field_value("work", Contakt.work_num)
        self.change_field_value("fax", Contakt.fax)
        # mail
        self.change_field_value("email", Contakt.mail1)
        self.change_field_value("email2", Contakt.mail2)
        self.change_field_value("email3", Contakt.mail3)
        self.change_field_value("homepage", Contakt.homepage)
        # Date
        self.pick_year_data("//select[@name='bday']", Contakt.birthday_date)
        self.pick_year_data("//select[@name='bmonth']", Contakt.birthday_month)
        self.change_field_value("byear", Contakt.beyer)
        self.pick_year_data("//select[@name='aday']", Contakt.anniversary_date)
        self.pick_year_data("//select[@name='amonth']", Contakt.anniversary_month)
        self.change_field_value("ayear", Contakt.ayer)
        # Adress
        self.change_field_value("address2", Contakt.adress2)
        self.change_field_value("phone2", Contakt.home2)
        # Note
        self.change_field_value("notes", Contakt.notes)

    def pick_year_data(self, xpath_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_xpath(xpath_name)).select_by_value(text)


    def add_new_cont(self):
        wd = self.app.wd
        self.return_home_page()
        wd.find_element_by_link_text("add new").click()


    def delete_first_contact(self):
        self.delete_some_contact_by_index(0)

    def delete_some_contact_by_index(self, index):
        wd = self.app.wd
        self.return_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self):
        self.select_edit_button_by_index(0)

    def select_edit_button_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def modify_contact_by_index(self, index, firstname):
        wd = self.app.wd
        self.return_home_page()
        self.select_edit_button_by_index(index)
        self.fill_contact_form(firstname)
        wd.find_element_by_name("update").click()
        # прейти на страницу с контактами
        self.return_home_page()
        self.contact_cash = None


    def return_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and
                len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("id")
                all_phones = cells[5].text
                self.contact_cache.append(
                    Contakt(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones))
        return self.contact_cache

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_from_home_page_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        cells = row.find_elements_by_tag_name("td")
        lastname = cells[1].text
        firstname = cells[2].text
        id = row.find_element_by_name("selected[]").get_attribute("id")
        address = cells[3].text
        all_emails = cells[4].text
        all_phones = cells[5].text
        contact = Contakt(firstname=firstname, lastname=lastname, id=id, adress2=address,
                          all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails)
        return contact

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
        return Contakt(firstname=firstname, lastname=lastname, id=id,
                       adress2=address, home_num=home_phone,
                       mail1=email, mail2=email2, mail3=email3, work_num=work_phone,
                       mob_nomber=mobile_phone, fax=fax, home2=secondary_phone)

    def get_contact_from_view_page_by_index(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        try:
            home_phone = re.search("H: (.*)", text).group(1)
        except:
            home_phone = None
        try:
            work_phone = re.search("W: (.*)", text).group(1)
        except:
            work_phone = None
        try:
            mobile_phone = re.search("M: (.*)", text).group(1)
        except:
            mobile_phone = None
        try:
            fax = re.search("F: (.*)", text).group(1)
        except:
            fax = None
        try:
            secondary_phone = re.search("P: (.*)", text).group(1)
        except:
            secondary_phone=None
        return Contakt(home_num=home_phone, work_num=work_phone,
                       mob_nomber=mobile_phone, fax = fax, home2=secondary_phone)

    def clear(self, phone):
        return re.sub("[() -]", "", phone)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                (map(lambda x: self.clear(x),
                                     filter(lambda x: x is not None,
                                            [contact.home_num, contact.mob_nomber,
                                             contact.work_num, contact.home2])))))

    def merge_phones_like_on_home_view_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                (map(lambda x: self.clear(x),
                                     filter(lambda x: x is not None,
                                            [contact.home_num, contact.mob_nomber,
                                             contact.work_num, contact.fax, contact.home2])))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.mail1, contact.mail2, contact.mail3])))