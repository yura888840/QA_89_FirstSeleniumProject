from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://icarro-v1.netlify.app/login")

    input("Press enter to close the browser...")

    first_a = driver.find_element(By.XPATH, "//a")

    first_div = driver.find_element(By.XPATH, "//div")

    first_h1 = driver.find_element(By.XPATH, "//h1")

    main_tag_class_main = driver.find_element(By.XPATH, "//main[@class='main']")

    root = driver.find_element(By.XPATH, '//*[@id="root"]')

    tag_with_inner_text = driver.find_element(By.XPATH, "//*[text()='Type your data and hit Yalla!']")

    search_link = driver.find_element(By.XPATH, "//*[@href='/search']")

    input_label = driver.find_element(By.XPATH, "//label[@class='input-label ']")

    element_with_inner_not_registered = (
        driver.find_element(By.XPATH, "//*[text()='Not registered? ']"))

    carro_logo = driver.find_element(By.XPATH, "//div[@class='footer-container']//img[@alt='IlCarro logo']")


finally:
    driver.quit()