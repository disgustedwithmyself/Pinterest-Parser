import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from logs import *


# Link
url = "your link"

# Absolute path to chromedriver.exe
driver = webdriver.Chrome(executable_path="path")

try:
    driver.get(url)
    time.sleep(5)
    login_button = driver.find_element(By.XPATH, "//div[@data-test-id='login-button']").click()
    time.sleep(3)

    # **Sing Up without google or facebook account**

    email_input = driver.find_element(By.XPATH, "//input[@autocomplete='email']")
    email_input.clear()
    email_input.send_keys(login_pin)
    time.sleep(5)

    pass_input = driver.find_element(By.XPATH, "//input[@autocomplete='new-password']")
    pass_input.clear()
    pass_input.send_keys(pass_pin)
    time.sleep(5)

    sing_up_button = driver.find_element(By.CLASS_NAME, "SignupButton").click()
    time.sleep(5)

    for i in range(0, 20):
        non_pin_images = driver.find_elements(By.XPATH, "//div[@data-test-id='non-story-pin-image']")
        non_pin_images[i].click()
        print('Картинка открыта')
        time.sleep(5)
        try:
            other_button = driver.find_element(By.XPATH, "//div[@data-test-id='closeup-more-options']").click()
            print('Другие варианты открыты')
            time.sleep(3.5)
            download_button = driver.find_element(By.XPATH, "//div[@data-test-id='pin-action-dropdown-download']").click()
            time.sleep(3.5)
            print(f'Изображение номер {i} успешно загрузилось')
            driver.back()
            time.sleep(5)
        except Exception as ex:
            print(ex)
        finally:
            continue
    print('Все картинки скачаны')

    # ////////////////////////////////////////

    time.sleep(15)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
