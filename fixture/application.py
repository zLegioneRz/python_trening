from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self, browser,baseurl):
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "chrome":
            self.wd = webdriver.Chrome("c:\Windows\System32\chromedriver.exe")
        elif browser == "ie":
            self.wd = webdriver.Ie("c:\Windows\System32\IEDriverServer.exe")
        else:
            raise ValueError("Unrecognize browser %s" % browser)
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.baseurl = baseurl

    def open_home_page(self):
        wd = self.wd
        # Открываем страницу
        wd.get(self.baseurl)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

