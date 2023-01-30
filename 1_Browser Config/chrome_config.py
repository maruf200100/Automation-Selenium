from selenium import webdriver


def chrome_launch():
    driver = webdriver.Chrome(executable_path="E:\\SQA\\Automation\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://google.com")


chrome_launch()
