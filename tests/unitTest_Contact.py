import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_ll(self):

        fname = "Test"
        lname = "User"
        email = "testuser@testuser.com"
        msg = "Test Message"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")
        elem = driver.find_element_by_xpath("/html/body/div[1]/ul/a[2]").click()
        time.sleep(3)

        elem = driver.find_element_by_id("id_first_name")
        time.sleep(3)
        elem.send_keys(fname)
        elem = driver.find_element_by_id("id_last_name")
        time.sleep(3)
        elem.send_keys(lname)
        elem = driver.find_element_by_id("id_email_address")
        time.sleep(3)
        elem.send_keys(email)
        elem = driver.find_element_by_id("id_message")
        time.sleep(3)
        elem.send_keys(msg)

        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/div[3]/form/button").click()
        time.sleep(3)



        #assert "Logged in"
        try:
            # attempt to find the 'Shop Now' button - returned to home page if present
           elem = driver.find_element_by_xpath("/html/body/a/button")

           assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()