#find_element(By.ID, value) � ����� �� ����������� �������� id ��������. ���� ���� ������������ ����������� ���� ��������� � ���������� ���������� id, �� ��� �������,

# � �� ���� ����� ����� ������������ ���� �����, ��� ��� �� �������� ����������;

#find_element(By.CSS_SELECTOR, value) � ����� �������� � ������� ������ �� ������ CSS. ��� ������������� ����� ������,��� ��� ����������� ���-���������� ���������� CSS ��� ������ � ������� 
#���������� ���������.

#  ���� find_element_by_id ��� �� �������� ��-�� ���������� id � ���������, �� ������ ����� �� ������ ������������ ������ ���� ����� � ����� ������;

#find_element(By.XPATH, value) � ����� � ������� ����� �������� XPath, ��������� ��������� ����� ������ ����� ���������;

#find_element(By.NAME, value) � ����� �� �������� name ��������;

#find_element(By.TAG_NAME, value) � ����� �������� �� �������� ���� ��������;

#find_element(By.CLASS_NAME, value) � ����� �� �������� �������� class;

#find_element(By.LINK_TEXT, value) � ����� ������ �� �������� �� ������� ����������;

#find_element(By.PARTIAL_LINK_TEXT, value) � ����� ������ �� ��������, ���� ����� ��������� ��������� � ����� ������ ������ ������.

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time

#link = "http://suninjuly.github.io/simple_form_find_task.html"

#try:
#   browser = webdriver.Chrome()
    #browser.get(link)
    #button = browser.find_element(By.ID, "submit_button")
    #time.sleep(2)
    #button.click()
    #time.sleep(3)

#finally:
    # ��������� ������� ����� ���� �����������
    #browser.quit()
