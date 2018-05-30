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

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("/html/body/div[1]/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def modify_first_cont(self, firstname):
        wd = self.app.wd
        self.return_home_page()
        wd.find_element_by_name("selected[]").click()
        #wd.find_element_by_xpath("1")
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        if firstname is not None:
            self.fill_fields_cont("firstname", firstname)
        wd.find_element_by_xpath("/html/body/div[1]/div[4]/form[1]/input[1]").click()

    def return_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_xpath("/html//table[@id='maintable']//a[@title='Sort on “Last name”']")) > 0 and len(wd.find_elements_by_xpath("//div[@id='content']/form[@name='MainForm']//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_xpath("//div[@id='nav']/ul//a[@href='./']").click()

    def count(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='nav']/ul//a[@href='./']").click()
        return len(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[2]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.return_home_page()
        contact_list = []
        for element in wd.find_elements_by_name("entry"):
            last_name = element.find_element_by_xpath(".//td[2]").text
            first_name = element.find_element_by_xpath(".//td[3]").text
            id = element.find_element_by_name("selected[]").get_attribute("id")
            contact_list.append(Contakt(lastname=last_name, firstname=first_name, id=id))
        return contact_list

