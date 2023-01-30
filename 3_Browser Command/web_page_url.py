from selenium import webdriver

def get_url():
    driver = webdriver.Chrome(executable_path="E:\\SQA\\Automation\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://google.com")
    url = driver.current_url
    print(url)


get_url()
