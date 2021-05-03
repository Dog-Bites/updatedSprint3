import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_ll(self):


        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")


        elem = driver.find_element_by_xpath("/html/body/div[1]/ul/a[1]").click()



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