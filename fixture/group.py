from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create_new(self, group):
        wd = self.app.wd
        self.open_page_group()
        # создаем группу
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # завершили создание новой группы
        wd.find_element_by_name("submit").click()
        self.open_page_group()
        self.group_cash = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)  # название имени группы

    def open_page_group(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def del_first_group(self):
        self.del_group_by_index(0)

    def del_group_by_index(self, index):
        wd = self.app.wd
        self.open_page_group()
        # выбрать 1 группу
        self.select_group_by_index(index)
        # нажать на "удалить"
        wd.find_element_by_name("delete").click()
        self.open_page_group()
        self.group_cash = None

    def del_group_by_id(self, id):
        wd = self.app.wd
        self.open_page_group()
        # выбрать 1 группу
        self.select_group_by_id(id)
        # нажать на "удалить"
        wd.find_element_by_name("delete").click()
        self.open_page_group()
        self.group_cash = None

    def mod_firt_group(self, new_group_data):
        self.mod_group_by_index(0, new_group_data)

    def mod_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_page_group()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        # вводим новые данные
        self.fill_group_form(new_group_data)
        # завершили обновление группы
        wd.find_element_by_name("update").click()
        self.open_page_group()
        self.group_cash = None

    def mod_group_by_id(self, new_group_data):
        wd = self.app.wd
        self.open_page_group()
        self.select_group_by_id(new_group_data.id)
        wd.find_element_by_name("edit").click()
        # вводим новые данные
        self.fill_group_form(new_group_data)
        # завершили обновление группы
        wd.find_element_by_name("update").click()
        self.open_page_group()
        self.group_cash = None

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='%s']" % id).click()

    def count(self):
        wd = self.app.wd
        self.open_page_group()
        return len(wd.find_elements_by_name("selected[]"))

    group_cash = None

    def get_group_list(self):
        if self.group_cash is None:
            wd = self.app.wd
            self.open_page_group()
            self.group_cash = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cash.append(Group(name=text, id=id))
        return list(self.group_cash)
