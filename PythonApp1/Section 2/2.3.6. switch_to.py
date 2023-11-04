# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math

# browser = webdriver.Chrome()
# link = "https://suninjuly.github.io/redirect_accept.html"
# browser.get(link)

# try:
    

#     buttontroll = browser.find_element(By.CSS_SELECTOR, "button.trollface")
#     buttontroll.click()
    
#     first_win = browser.window_handles[0]
#     second_win = browser.window_handles[1]

#     browser.switch_to.window(second_win)

    
#     def calc(x):
#         return (math.log(abs(12*math.sin(int(x)))))
    
    
#     #confirm = browser.switch_to.alert
#     #confirm.accept()
    
#     answer = browser.find_element(By.ID,"answer")
    
#     input_value = int(browser.find_element(By.ID,"input_value").text)
    
#     answer.send_keys(calc(input_value))
    

#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
    

# finally:
#     time.sleep(10)
    
#     browser.quit()