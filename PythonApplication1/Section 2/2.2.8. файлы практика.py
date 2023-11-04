
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time 
# import os 

# link ="https://suninjuly.github.io/file_input.html"
# browser = webdriver.Chrome()
# browser.get(link)

# try:
#     # elements = browser.find_elements(By.CSS_SELECTOR, "input[placeholder]")
#     # for element in elements:
#     #     element.send_keys("I wanna pizza")
        
#     firstname = browser.find_element(By.NAME,"firstname")
#     firstname.send_keys("Stepan")
    
#     lastname = browser.find_element(By.CSS_SELECTOR, "input[placeholder = 'Enter last name']")
#     lastname.send_keys("Petrov")
    
#     email = browser.find_element(By.NAME,"email")
#     email.send_keys ("popov123123@gmail.com")
  


#     file = browser.find_element(By.NAME,"file")
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     file_path = os.path.join(current_dir, 'text.txt')
    
#     file.send_keys(file_path)
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
      
    
# finally:
#     time.sleep(10)
    
#     browser.quit()
    





#find_element(By.NAME, value) — поиск по атрибуту name элемента;