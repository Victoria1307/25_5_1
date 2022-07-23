import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_implicit_wait():
    # Тест с неявным ожиданием
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.implicitly_wait(5)  # неявные ожидания

    # Open PetFriends base page:

    driver.get("https://petfriends.skillfactory.ru/")

    # click on the new user button
    btn_newuser = driver.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()

    # click existing user button
    btn_exist_acc = driver.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = driver.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys("vandro1307@gmail.com")

    # add password
    field_pass = driver.find_element_by_id("pass")
    field_pass.clear()
    field_pass.send_keys("PetFriends")

    # click submit button
    btn_submit = driver.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    # Берем первого питомца
    pet = driver.find_element_by_css_selector('body > div > div > div.card-deck > div:nth-child(1)')
    # Проверяем что есть фотка
    assert len(pet.screenshot_as_png) > 0

    # Имя и возраст в элементе идут в одном поле "text", поэтому разбиваем строку по переносу строки
    name_age = pet.text.split("\n")
    # Проверяем имя
    assert len(name_age[0]) > 1
    # Проверяем возраст
    assert len(name_age[1]) > 1


def test_explicit_wait():
    # Тест с явным ожиданием
    driver = webdriver.Chrome(executable_path='chromedriver.exe')

    driver.get("https://petfriends.skillfactory.ru/")

    # click on the new user button
    btn_newuser = driver.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()

    # click existing user button
    btn_exist_acc = driver.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = driver.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys("vandro1307@gmail.com")

    # add password
    field_pass = driver.find_element_by_id("pass")
    field_pass.clear()
    field_pass.send_keys("PetFriends")

    # click submit button
    btn_submit = driver.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div > div > div.card-deck > div:nth-child(1) > div.card-body > h5'))
    )

    # Имя присутствует
    assert name is not None

    body = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > div > div > div.card-deck > div:nth-child(1) > div.card-body > p'))
    )

    # возраст находится в поле text
    assert body.text is not None

    image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > div > div > div.card-deck > div:nth-child(1) > div.text-center.align-self-center.align-middle > img')
        )
    )

    assert image is not None





