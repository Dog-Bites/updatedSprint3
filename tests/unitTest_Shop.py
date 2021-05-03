import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_ll(self):
        user = "testuser"
        pwd = "test123"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")
        elem = driver.find_element_by_xpath("/html/body/div[1]/ul/a[4]").click()
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[1]/ul/a[3]").click()


        #assert "Logged in"
        try:
            # attempt to find the 'Logout' button - if found, logged in
           elem = driver.find_element_by_xpath("/html/body/div[1]/ul/a[4]")

           assert True

        except NoSuchElementException:
            self.fail("Shop Tab Failed - user may not be signed in")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()