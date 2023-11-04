
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestRegistrationForm(unittest.TestCase):
    
    def test_regisration_form1(self):
        
        link_1form = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link_1form)
        
        firstname = browser.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your first name']")
        firstname.send_keys("Petya")
        
        lastname = browser.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your last name']")
        lastname.send_keys("Petropavlov")
        
        email = browser.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your email']")
        email.send_keys("PetruhaUbiitsa217@gmail.com")
        
        button = browser.find_element(By.CSS_SELECTOR,"button.btn")
        button.click()
        
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!",welcome_text,"Я не совсем понимаю, как это поможет локализовать ошибку, если я не буду знать где она конкретно?")
        
    def test_regisration_form2(self):
        
        link_1form = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link_1form)
        
        firstname = browser.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your first name']")
        firstname.send_keys("Petya")
        
        lastname = browser.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your last name']")
        lastname.send_keys("Petropavlov")
        
        email = browser.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your email']")
        email.send_keys("PetruhaUbiitsa217@gmail.com")
        
        button = browser.find_element(By.CSS_SELECTOR,"button.btn")
        button.click()
        
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!",welcome_text,"Ошибка в тесте 2")

        
        time.sleep(5)


    #     self.assertEqual(, "Required values ​​must be filled in")
        
    # def test_registration_form2(self):
    #     self.assertEqual(abs(-42), -42, "Required values ​​must be filled in")
        
if __name__ == "__main__":
    unittest.main()