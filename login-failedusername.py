import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
            self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_failed_login_Username(self):
    # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("acakadut") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

# validasi
        response_data = driver.find_element(By.CLASS_NAME,"login_wrapper-inner").text
        self.assertIn('Epic sadface: Username and password do not match any user in this service', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
