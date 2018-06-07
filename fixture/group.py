from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def count(self):
       wd = self.app.wd
       self.open_group()
       return len(wd.find_elements_by_name("selected[]"))


    def create(self, group):
        wd = self.app.wd
        self.open_group()
        wd.find_element_by_name("new").click()
        if group.group_name is not None:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.group_name)
        if group.header is not None:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
        if group.footer is not None:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.group_cache =None

    def open_group(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()
        #wd.find_element_by_link_text("groups").click()

    def delete_group_by_index(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self,index):
        wd = self.app.wd
        self.open_group()
        #Выбрать первую группу
        self.select_group_group_by_index(index)
        #Удалить первую группу
        wd.find_element_by_name("delete").click()
        self.return_group_page()
        self.group_cache = None

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_group()
        self.select_first_group()
        #Нажимаем кнопку редактирования группы
        wd.find_element_by_xpath("/html/body/div[1]/div[4]/form/input[3]").click()
        #wd.find_element_by_name("edit").click()
        self.fill_group_form(group)

    def fill_group_form(self, group):
        wd = self.app.wd
        if group.group_name is not None:
            self.change_field_value("group_name", group.group_name)
        if group.header is not None:
            self.change_field_value("group_header", group.header)
        if group.footer is not None:
            self.change_field_value("group_footer", group.footer)
        wd.find_element_by_name("update").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def modyfy_first_group(self):
        self.modyfy_group_by_index(0)

    def modyfy_group_by_index(self,index, new_group_data):
        wd = self.app.wd
        self.open_group()
        self.select_group_group_by_index(index)
        wd.find_element_by_xpath("/html/body/div[1]/div[4]/form/input[3]").click()
        self.fill_group_form(new_group_data)
        #wd.find_element_by_name("update").click()
        self.return_group_page()
        self.group_cache = None

    def return_group_page(self):
        wd = self.app.wd
        #self.return_group_page()
        wd.find_element_by_xpath("/html//div[@id='content']//a[@href='group.php']").click()

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(group_name=text, id=id))
        return list(self.group_cache)
