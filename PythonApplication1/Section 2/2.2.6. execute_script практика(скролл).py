# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math

# link = "https://SunInJuly.github.io/execute_script.html"
# browser = webdriver.Chrome()
# browser.get(link)

# try:
#     input_value = int(browser.find_element(By.ID,"input_value").text)
    
#     def calc(x):
#        return (math.log(abs(12*math.sin(int(x)))))
    
#     answer = browser.find_element(By.ID, "answer")
#     answer.send_keys(calc(input_value))
    
#     robotCheckbox = browser.find_element(By.ID,"robotCheckbox")
#     robotCheckbox.click()
    
#     browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
    
#     robotsRule = browser.find_element(By.ID,"robotsRule")
#     robotsRule.click()
    
#     button = browser.find_element(By.CSS_SELECTOR,'button.btn')
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
