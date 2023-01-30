from selenium import webdriver


def set_browser_size():
    driver = webdriver.Chrome(executable_path="E:\\SQA\\Automation\\chromedriver.exe")
    driver.set_window_size(400,800)
set_browser_size()
