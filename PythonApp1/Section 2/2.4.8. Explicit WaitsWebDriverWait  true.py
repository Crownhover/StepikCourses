# import math
# from tkinter import BUTT, Button
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time


# #WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "<ќт кого ждем>"), "<„то ждем>"))

# browser = webdriver.Chrome()
# browser.get("https://suninjuly.github.io/explicit_wait2.html")


# try:

#     def calc(x):
#         return (math.log(abs(12*math.sin(int(x)))))
    
    
#     WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
#     button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button1.click()
    
#     input_value = int(browser.find_element(By.ID,"input_value").text)
   
#     answer = browser.find_element(By.ID, "answer")
#     answer.send_keys(calc(input_value))

#     button2 = browser.find_element(By.ID,"solve")
#     button2.click()
    
      
   

# finally:
#      #успеваем скопировать код за 30 секунд
#     time.sleep(10)
#      #закрываем браузер после всех манипул€ций
#     browser.quit()