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
        fname = "Test"
        lname = "User"
        email = "testuser@testuser.com"
        address = "1110 S 67 St"
        zip = "68112"
        city = "Omaha"



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
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[1]/div/div/h3/a").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div[2]/form/input[3]").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/p/a[2]").click()
        time.sleep(3)

        elem = driver.find_element_by_id("id_first_name")
        time.sleep(3)
        elem.send_keys(fname)
        elem = driver.find_element_by_id("id_last_name")
        time.sleep(3)
        elem.send_keys(lname)
        elem = driver.find_element_by_id("id_email")
        time.sleep(3)
        elem.send_keys(email)
        elem = driver.find_element_by_id("id_address")
        time.sleep(3)
        elem.send_keys(address)
        elem = driver.find_element_by_id("id_postal_code")
        time.sleep(3)
        elem.send_keys(zip)
        elem = driver.find_element_by_id("id_city")
        time.sleep(3)
        elem.send_keys(city)

        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/form/input[2]").click()

        time.sleep(3)
        #assert "Logged in"
        try:
            # attempt to find the checkout confirmation page
           elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/h3")

           assert True

        except NoSuchElementException:
            self.fail("Checkout Failed")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()