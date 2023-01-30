from selenium import webdriver
import time


def set_browser_size():
    driver = webdriver.Firefox(executable_path="E:\\SQA\\Automation\\geckodriver.exe")

    driver.get("https://google.com")
    time.sleep(2)

    driver.get("https://facebook.com")
    time.sleep(2)
    # driver.set_window_size(600,800)

    driver.back()
    time.sleep(2)

    driver.forward()
    time.sleep(2)

    driver.refresh()

    driver.close()


set_browser_size()