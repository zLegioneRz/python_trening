

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_group()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()

    def open_group(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='nav']/ul//a[@href='group.php']").click()
        #wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group()
        #Выбрать первую группу
        wd.find_element_by_name("selected[]").click()
        #Удалить первую группу
        wd.find_element_by_name("delete").click()

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
        self.change_field_value("group_name", group.group_name)
        self.change_field_value("group_header", group.header)
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


    def modyfy_first_group_new(self, new_group_data):
        wd = self.app.wd
        self.open_group()
        self.select_first_group()
        wd.find_element_by_xpath("/html/body/div[1]/div[4]/form/input[3]").click()
        self.fill_group_form(new_group_data)
        #wd.find_element_by_name("update").click()
        self.return_group_page()

    def return_group_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html//div[@id='content']//a[@href='group.php']").click()