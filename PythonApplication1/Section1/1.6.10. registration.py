from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ��� ���, ������� ��������� ������������ ����
    elements = browser.find_element(By.CSS_SELECTOR,  "input:required")
    for element in elements:
        element.send_keys("Pizza time")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    time.sleep(5)
    button.click()
    # ���������� ����������� �����

    # ���������, ��� ������ ������������������
    # ���� �������� ��������
    time.sleep(1)

    # ������� �������, ���������� �����
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # ���������� � ���������� welcome_text ����� �� �������� welcome_text_elt
    welcome_text = welcome_text_elt.text

    # � ������� assert ���������, ��� ��������� ����� ��������� � ������� �� �������� �����
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()