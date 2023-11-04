# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math

# browser = webdriver.Chrome()
# link = "https://suninjuly.github.io/alert_accept.html"
# browser.get(link)

# try:
    
#     def calc(x):
#         return (math.log(abs(12*math.sin(int(x)))))
    
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
    
#     confirm = browser.switch_to.alert
#     confirm.accept()
    
#     answer = browser.find_element(By.ID,"answer")
    
#     input_value = int(browser.find_element(By.ID,"input_value").text)
    
#     answer.send_keys(calc(input_value))
    

#     button_next = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button_next.click()
    










# finally:
#     time.sleep(10)
    
#     browser.quit()