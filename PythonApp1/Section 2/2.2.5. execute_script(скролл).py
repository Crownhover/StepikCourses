# В первую очередь WebDriver проверит, что ширина и высота элемента больше 0, чтобы по нему можно было кликнуть.

# Затем, если элемент находится за границей окна браузера, WebDriver автоматически проскроллит страницу, 

# чтобы элемент попал в область видимости, то есть не находился за границей экрана. Но это не гарантирует того, что элемент не перекрыт другим элементом,

# который тоже находится в области видимости

# А в какую точку элемента будет происходить клик? Selenium рассчитывает координаты центра элемента и производит клик в вычисленную точку.

# Это тоже приведёт к ошибке, если часть элемента всё-таки видна, но элемент перекрыт больше чем на половину своей высоты или ширины.

#"return arguments[0].scrollIntoView(true);" - скрипт для скролла. 
#
#browser.execute_script("return arguments[0].scrollIntoView(true);", button) - пример использования скрипта для скролла

# browser.execute_script("window.scrollBy(0, 100);") - ПРОСМОТР СТРАНИЦЫ НА ОПРЕДЕЛЁННОЕ КОЛИЧЕСТВО ПИКСЕЛЕЙ.
#


#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#browser = webdriver.Chrome()
#link = "https://SunInJuly.github.io/execute_script.html"
#browser.get(link)
#button = browser.find_element(By.TAG_NAME, "button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)

#time.sleep(5)
#button.click()