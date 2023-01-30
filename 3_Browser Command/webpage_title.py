from selenium import webdriver


def get_title():
    driver = webdriver.Chrome(executable_path="E:\\SQA\\Automation\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://google.com")
    title = driver.title
    print(title)


get_title()
