from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://icarro-v1.netlify.app/login")

    input("Press enter to close the browser...")

    first_a = driver.find_element(By.CSS_SELECTOR, "a")

    h1 = driver.find_element(By.CSS_SELECTOR, "h1")

    first_input = driver.find_element(By.CSS_SELECTOR, "input")

    registration_card = driver.find_element(By.CSS_SELECTOR, ".login-registration-card")

    root = driver.find_element(By.CSS_SELECTOR, "#root")

    placeholder_email = driver.find_element(By.CSS_SELECTOR, "[type='email']")

    link_search = driver.find_element(By.CSS_SELECTOR, "[href='/search']")

    first_tag_with_class_starting_from_input = (
        driver.find_element(By.CSS_SELECTOR, "[class^='input-']"))


    first_tag_with_class_ending_with_navigator = (
        driver.find_element(By.CSS_SELECTOR, "[class$='-navigator']"))

    first_tag_having_container_in_class = (
        driver.find_element(By.CSS_SELECTOR, "[class*='container']"))

finally:
    driver.quit()