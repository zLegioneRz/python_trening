from model.contact import Contakt

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_fields_cont(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def add_new_cont(self, Contakt):
        wd = self.app.wd
        self.return_home_page()
        wd.find_element_by_link_text("add new").click()
        #wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        if Contakt.firstname is not None:
            self.fill_fields_cont("firstname", Contakt.firstname)
        if Contakt.midlname is not None:
            self.fill_fields_cont("middlename", Contakt.midlname)
        if Contakt.lastname is not None:
            self.fill_fields_cont("lastname", Contakt.lastname)
        if Contakt.nickname is not None:
            self.fill_fields_cont("nickname", Contakt.nickname)
        if Contakt.titl is not None:
            self.fill_fields_cont("title", Contakt.titl)
        if Contakt.company is not None:
            self.fill_fields_cont("company", Contakt.company)
        if Contakt.adress is not None:
            self.fill_fields_cont("address", Contakt.adress)
        if Contakt.home_num is not None:
            wd.find_element_by_name("theform").click()
            self.fill_fields_cont("home", Contakt.home_num)
        if Contakt.mob_nomber is not None:
            wd.find_element_by_name("theform").click()
            self.fill_fields_cont("mobile", Contakt.mob_nomber)
        if Contakt.work_num is not None:
            self.fill_fields_cont("work", Contakt.work_num)
        if Contakt.fax is not None:
            self.fill_fields_cont("fax", Contakt.fax)
        if Contakt.mail1 is not None:
            self.fill_fields_cont("email", Contakt.mail1)
        if Contakt.mail2 is not None:
            self.fill_fields_cont("email2", Contakt.mail2)
        if Contakt.mail3 is not None:
            self.fill_fields_cont("email3", Contakt.mail3)
        if Contakt.homepage is not None:
            self.fill_fields_cont("homepage", Contakt.homepage)
        if Contakt.beyer is not None:
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[9]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[9]").click()
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()
            self.fill_fields_cont("byear", Contakt.beyer)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[12]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[4]").click()
        if Contakt.ayer is not None:
            self.fill_fields_cont("ayear", Contakt.ayer)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[4]").click()
            wd.find_element_by_name("theform").click()
        if Contakt.adress2 is not None:
            self.fill_fields_cont("address2", Contakt.adress2)
        if Contakt.home2 is not None:
            self.fill_fields_cont("phone2", Contakt.home2)
        if Contakt.notes is not None:
            self.fill_fields_cont("notes", Contakt.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None



    def delete_first_contact(self):
        self.delete_some_contact_by_index(0)

    def delete_some_contact_by_index(self, index):
        wd = self.app.wd
        self.return_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("/html/body/div[1]/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_home_page()
        self.contact_cache = None

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self,index):
        self.select_contact_by_index(0)

    def modify_contact_by_index(self, index, firstname):
        wd = self.app.wd
        self.return_home_page()
        self.select_contact_by_index(index)
        #wd.find_element_by_xpath("1")
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        if firstname is not None:
            self.fill_fields_cont("firstname", firstname)
        wd.find_element_by_xpath("/html/body/div[1]/div[4]/form[1]/input[1]").click()
        self.return_home_page()
        self.contact_cache = None


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
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                last_name = element.find_element_by_css_selector("td:nth-of-type(2)").text
                first_name = element.find_element_by_css_selector("td:nth-of-type(3)").text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contakt(lastname=last_name, firstname=first_name, id=id,
                                                  home_num=all_phones[0], mob_nomber=all_phones[1],
                                                  work_num=all_phones[2], fax=all_phones[3]))
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
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_num = wd.find_element_by_name("home").get_attribute("value")
        mob_nomber = wd.find_element_by_name("mobile").get_attribute("value")
        work_num = wd.find_element_by_name("work").get_attribute("value")
        fax = wd.find_element_by_name("phone2").get_attribute("value")
        return Contakt(firstname=firstname,lastname=lastname,id=id,home_num=home_num,mob_nomber=mob_nomber,
                       work_num=work_num ,fax=fax)


