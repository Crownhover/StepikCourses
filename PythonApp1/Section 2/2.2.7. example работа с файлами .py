
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time 
# import os 

# link = "https://SunInJuly.github.io/execute_script.html"
# browser = webdriver.Chrome()
# browser.get(link)

# try:
#     answer = browser.find_element(By.ID, "answer")
#     current_dir = os.path.abspath(os.path.dirname(__file__))    # �������� ���� � ���������� �������� ������������ ����� 
#     file_path = os.path.join(current_dir, 'text.txt')           # ��������� � ����� ���� ��� ����� 
#     answer.send_keys(file_path)

# finally:
#     time.sleep(10)
#     browser.quit()