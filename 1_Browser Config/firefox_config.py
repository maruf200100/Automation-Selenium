from selenium import webdriver


def firefox_launch():
    driver = webdriver.Firefox(executable_path="E:\\SQA\\Automation\\geckodriver.exe")
    #driver.close()
    driver.get("https://google.com")
    title = driver.title
    print(title)



firefox_launch()

