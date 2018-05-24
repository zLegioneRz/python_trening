

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def fill_fields_cont(self, field_name,text):
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
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(Contakt.firstname)
        if Contakt.midlname is not None:
            wd.find_element_by_name("middlename").click()
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(Contakt.midlname)
        if Contakt.lastname is not None:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(Contakt.lastname)
        if Contakt.nickname is not None:
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(Contakt.nickname)
        if Contakt.titl is not None:
            wd.find_element_by_name("title").click()
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(Contakt.titl)
        if Contakt.company is not None:
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(Contakt.company)
        if Contakt.adress is not None:
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(Contakt.adress)
        if Contakt.home_num is not None:
            wd.find_element_by_name("theform").click()
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(Contakt.home_num)
        if Contakt.mob_nomber is not None:
            wd.find_element_by_name("theform").click()
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(Contakt.mob_nomber)
        if Contakt.work_num is not None:
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(Contakt.work_num)
        if Contakt.fax is not None:
            wd.find_element_by_name("fax").click()
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(Contakt.fax)
        if Contakt.mail1 is not None:
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(Contakt.mail1)
        if Contakt.mail2 is not None:
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(Contakt.mail2)
        if Contakt.mail3 is not None:
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(Contakt.mail3)
        if Contakt.homepage is not None:
            wd.find_element_by_name("homepage").click()
            wd.find_element_by_name("homepage").click()
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(Contakt.homepage)
        if Contakt.beyer is not None:
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[9]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[9]").click()
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(Contakt.beyer)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[12]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[4]").click()
        if Contakt.ayer is not None:
            wd.find_element_by_name("ayear").click()
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys(Contakt.ayer)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[4]").click()
            wd.find_element_by_name("theform").click()
        if Contakt.adress2 is not None:
            wd.find_element_by_name("address2").click()
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys(Contakt.adress2)
        if Contakt.home2 is not None:
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(Contakt.home2)
        if Contakt.notes is not None:
            wd.find_element_by_name("notes").click()
            wd.find_element_by_name("notes").clear()
            wd.find_element_by_name("notes").send_keys(Contakt.notes)
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
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_xpath("/html/body/div[1]/div[4]/form[1]/input[1]").click()


    def return_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_xpath("/html//table[@id='maintable']//a[@title='Sort on “Last name”']")) >0 and len(wd.find_elements_by_xpath("//div[@id='content']/form[@name='MainForm']//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_xpath("//div[@id='nav']/ul//a[@href='./']").click()

    def count(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='nav']/ul//a[@href='./']").click()
        return len(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[2]"))