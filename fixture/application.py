from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, browser, base_url):

        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "chrome":
            self.wd = webdriver.Chrome("c:\Windows\System32\chromedriver.exe")
        elif browser == "ie":
            self.wd = webdriver.Ie("c:\Windows\System32\IEDriverServer.exe")
        elif browser == "opera":
            self.wd = webdriver.Opera("c:\Windows\System32\operadriver.exe")
        else:
            raise ValueError("Unrecognize browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url=base_url
        # self.wd.implicitly_wait(5) - для учебного приложения не нужно

    def open_start_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
