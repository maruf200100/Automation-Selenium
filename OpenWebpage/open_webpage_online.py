from lib2to3.pgen2 import driver

from selenium import webdriver


def open_webpage_online():
    # driver = webdriver.Firefox(executable_path="E:\\SQA\\Automation\\geckodriver.exe")

    driver.get("file:///E:/SQA/Automation/Demo Site.html")
    driver.close()
    # driver.get("https://facebook.com")


open_webpage_online()
