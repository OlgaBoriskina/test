from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import authorization.authorization as authorization
import action.submenu as submenu
import unittest

base_url = "http://way2automation.com/way2auto_jquery"


class Test (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get(base_url)
        self.wait = WebDriverWait(self.driver, 10)
        authorization.authorize(self.wait)
        self.driver.refresh()
        self.driver.get(base_url + "/menu.php")

    def test_action_submenu(self):
        submenu_action = submenu.action(self.driver, self.wait)
        assert(submenu_action.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()