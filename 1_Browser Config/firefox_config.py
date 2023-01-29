from selenium import webdriver

def firefox_launch():
    driver = webdriver.Firefox(executable_path="E:\\SQA\\Automation\\geckodriver.exe")

firefox_launch()
