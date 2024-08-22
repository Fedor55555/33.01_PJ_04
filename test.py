import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=fc343b3b-9ff7-4786-bb30-e60caa7821cd&client_id=lk_b2c&tab_id=Zkmg4gt0e7A')
    element = WebDriverWait(driver, 20).until(
         EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))  )


    yield driver

    driver.quit()


def test_auth_unvalid_personal_account(driver):
    # '''Этот тест вводит в поля для авторизации несуществующий лицевой счет
    # в корректном формате и проверяет, что после ввода данных сайт выводит сообщение
    # "Неверный логин или пароль" '''
    driver.implicitly_wait(10)
    # На странице авторизации по коду кликаем кнопку "Войти с паролем"
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # явное ожидание присутствия элемента в структуре документа.
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'username')))
    # Вводим лицевой счет
    driver.find_element(By.ID, 'username').send_keys('125930410062')

    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys('_ucS7_!hQW8%ZXnh__')
    # явное ожидание присутствия элемента в структуре документа.
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, 'btn-success'))
    # )

    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    element = WebDriverWait(driver, 20).until(
         EC.presence_of_element_located((By.ID, 'from-error-message')))

    # Проверяем, что введены верные данные в поля логин(номер телефона, почта), пароль:
    assert driver.find_element(By.TAG_NAME, 'span').text == 'Неверный логин или пароль'

def test_auth_valid_login(driver):
    driver.get(
        'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=fc343b3b-9ff7-4786-bb30-e60caa7821cd&client_id=lk_b2c&tab_id=Zkmg4gt0e7A')
    sleep(30)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    sleep(15)
    # Вводим email
    driver.find_element(By.ID, 'username').send_keys('rtkid_1722854961169')
    # element = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable(By.CLASS_NAME, 'nav-link')

    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys('ucS7_!hQW8%ZXnh')
    # явное ожидание присутствия элемента в структуре документа.
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, 'btn-success'))
    # )

    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    sleep(20)

    # Проверяем, что введены верные данные в поля логин(номер телефона, почта), пароль:
    assert driver.find_element(By.CLASS_NAME, 'lfjrSy').text == 'Личный кабинет'


def test_auth_valid_mail_log(driver):
    driver.get(
        'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=fc343b3b-9ff7-4786-bb30-e60caa7821cd&client_id=lk_b2c&tab_id=Zkmg4gt0e7A')
    sleep(30)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    sleep(15)
    # Вводим email
    driver.find_element(By.ID, 'username').send_keys('natakhol@mail.ru')
    # element = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable(By.CLASS_NAME, 'nav-link')

    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys("*Jk'*e76cw-uL.J")
    # явное ожидание присутствия элемента в структуре документа.
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, 'btn-success'))
    # )

    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    sleep(15)

    # Проверяем, что введены верные данные в поля логин(номер телефона, почта), пароль:
    assert driver.find_element(By.CLASS_NAME, 'lfjrSy').text == 'Личный кабинет'


def test_enter_unregistrated_telephone_log(driver):
    driver.get(
        'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=fc343b3b-9ff7-4786-bb30-e60caa7821cd&client_id=lk_b2c&tab_id=S3eAnRX8uJw')
    sleep(30)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    sleep(15)
    # Вводим email
    driver.find_element(By.ID, 'username').send_keys('+79536370505')
    # element = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable(By.CLASS_NAME, 'nav-link')

    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys('ucS7_!hQW8%ZXnh*')
    # явное ожидание присутствия элемента в структуре документа.
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, 'btn-success'))
    # )

    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    sleep(5)

    #Проверяем, что введены неверные данные в поля логин(номер телефона, почта), пароль:
    assert driver.find_element(By.TAG_NAME, 'span').text == "Неверный логин или пароль" 'Неверно введен код с картинки'

#
#
#

#
def test_auth_valid_telephone_log(driver):
    driver.get(
        'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=fc343b3b-9ff7-4786-bb30-e60caa7821cd&client_id=lk_b2c&tab_id=S3eAnRX8uJw')
    sleep(15)
    driver.find_element(By.ID, 'standard_auth_btn').click()
        # Вводим email
    sleep(15)
    driver.find_element(By.ID, 'username').send_keys('+79536370505')
    #     # element = WebDriverWait(driver, 10).until(
#     #     EC.element_to_be_clickable(By.CLASS_NAME, 'nav-link')
#
#     # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys('ucS7_!hQW8%ZXnh')
#     # явное ожидание присутствия элемента в структуре документа.
#     # element = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.CLASS_NAME, 'btn-success'))
#     # )
# #
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    sleep(10)

    # Проверяем, что введены верные данные в поля логин(номер телефона, почта), пароль:
    assert driver.find_element(By.CLASS_NAME, 'lfjrSy').text == 'Личный кабинет'
#


def test_enter_unvalid_telephone_log(driver):
    driver.get(
        'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=fc343b3b-9ff7-4786-bb30-e60caa7821cd&client_id=lk_b2c&tab_id=S3eAnRX8uJw')
    sleep(30)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    sleep(15)
    # Вводим email
    driver.find_element(By.ID, 'username').send_keys('+7953637050537')
    # element = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable(By.CLASS_NAME, 'nav-link')

    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys('ucS7_!hQW8%ZXnh*')
    # явное ожидание присутствия элемента в структуре документа.
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, 'btn-success'))
    # )

    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    sleep(5)

    #Проверяем, что введены неверные данные в поля логин(номер телефона, почта), пароль:
    assert driver.find_element(By.TAG_NAME, 'span').text == "Неверный логин или пароль" 'Неверно введен код с картинки'
#

def test_auth_blank_value_log(driver):
    # driver.get(
    #     'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=fc343b3b-9ff7-4786-bb30-e60caa7821cd&client_id=lk_b2c&tab_id=S3eAnRX8uJw')
    sleep(30)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    sleep(15)
    # Вводим email

    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    sleep(5)

    #Проверяем, что введены неверные данные в поля логин(номер телефона, почта), пароль:
    assert driver.find_element(By.ID, 'username-meta').text == 'Введите номер телефона', 'Введите адрес, указанный при регистрации' 'Введите логин, указанный при регистрации'



def test_registration(driver):
#     driver.get(
#         'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=fc343b3b-9ff7-4786-bb30-e60caa7821cd&client_id=lk_b2c&tab_id=mnsoNU_1Yzo')
    sleep(15)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    sleep(10)
    driver.find_element(By.ID, 'kc-register').click()
    # Вводим email
    sleep(15)
    driver.find_element(By.NAME, 'firstName').send_keys('Наталья')
    driver.find_element(By.NAME, 'lastName').send_keys('Мамина')
    # driver.find_element(By.XPATH, "//input[@autocomplete='new-password']").clear()
    # driver.find_element(By.XPATH, "//input[@autocomplete='new-password']").send_keys('Саратовская обл')
    driver.find_element(By.ID, 'address').send_keys('natamamina2503@yandex.ru')
    driver.find_element(By.ID, 'password').send_keys('ucS7_!hQW8%ZXnh__')
    driver.find_element(By.ID, 'password-confirm').send_keys('ucS7_!hQW8%ZXnh__')
    driver.find_element(By.NAME, 'register').click()
    sleep(30)
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Подтверждение email'


def test_registration_incorrect_filling(driver):
    driver.get(
        'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=fc343b3b-9ff7-4786-bb30-e60caa7821cd&client_id=lk_b2c&tab_id=mnsoNU_1Yzo')
    sleep(15)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    sleep(10)
    driver.find_element(By.ID, 'kc-register').click()
    # Вводим email
    sleep(15)
    driver.find_element(By.NAME, 'firstName').send_keys('Natalya')
    driver.find_element(By.NAME, 'lastName').send_keys('M')
    # driver.find_element(By.XPATH, "//input[@autocomplete='new-password']").clear()
    # driver.find_element(By.XPATH, "//input[@autocomplete='new-password']").send_keys('Саратовская обл')
    driver.find_element(By.ID, 'address').send_keys('j;dskfj@klsdjf.ru')
    driver.find_element(By.ID, 'password').send_keys('ucS7_!h')
    driver.find_element(By.ID, 'password-confirm').send_keys('ucS7_!hQW8%ZXnh__')
    driver.find_element(By.NAME, 'register').click()
    sleep(30)
    assert driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error').text == (
        'Необходимо заполнить поле кириллицей. От 2 до 30 символов.')
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text != 'Подтверждение email'



def test_login_using_authorization_code(driver):
    driver.get(
        'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_b2c&redirect_uri=https%3A%2F%2Flk-api.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%252F%252Fstart.rt.ru%252F&response_type=code&scope=openid')
    sleep(15)
    driver.find_element(By.ID, 'address').send_keys('natakhol@mail.ru')
    driver.find_element(By.ID, 'otp_get_code').click()
    sleep(10)
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Код подтверждения отправлен' 'Авторизация по коду'


def test_recover_password(driver):
    driver.get(
        'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=bcd7aed6-e47f-4631-a37c-60b64f653e36')
    sleep(15)
    driver.find_element(By.ID, 'forgot_password').click()
    sleep(10)
    driver.find_element(By.ID, 'username').send_keys('natakhol@mail.ru')
#     # Вводим email
#     sleep(15)
    driver.find_element(By.ID, 'reset').click()
    sleep(10)
    assert driver.find_element(By.ID, 'card-title').text == 'Восстановление пароля'





def test_auth_valid_log_keyrtru(driver):
    driver.get(
        'https://key.rt.ru')
    sleep(20)
    driver.find_element(By.CLASS_NAME, 'go_mobile_kabinet').click()
        # Вводим email
    sleep(20)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    sleep(20)
    driver.find_element(By.ID, 'username').send_keys('+79536370505')
    #     # element = WebDriverWait(driver, 10).until(
#     #     EC.element_to_be_clickable(By.CLASS_NAME, 'nav-link')
#
#     # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys('ucS7_!hQW8%ZXnh')
#     # явное ожидание присутствия элемента в структуре документа.
#     # element = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.CLASS_NAME, 'btn-success'))
#     # )
# #
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    sleep(10)

    # Проверяем, что введены верные данные в поля логин(номер телефона, почта), пароль:
    assert driver.find_element(By.CLASS_NAME, 'lfjrSy').text == 'Личный кабинет'



def test_registration_keyrtru(driver):
    driver.get(
        'https://key.rt.ru')
    sleep(20)
    driver.find_element(By.CLASS_NAME, 'go_kab').click()
    sleep(10)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    sleep(15)
    driver.find_element(By.ID, 'kc-register').click()
    # Вводим email
    sleep(15)
    driver.find_element(By.NAME, 'firstName').send_keys('Наталья')
    driver.find_element(By.NAME, 'lastName').send_keys('Мамина')
    # driver.find_element(By.XPATH, "//input[@autocomplete='new-password']").clear()
    # driver.find_element(By.XPATH, "//input[@autocomplete='new-password']").send_keys('Саратовская облdriver.find_element(By.ID, 'address').send_keys('natamamina2503@yandex.ru')
    driver.find_element(By.ID, 'address').send_keys('+79536370503')
    driver.find_element(By.ID, 'password').send_keys('ucS7_!hQW8%ZXnh__')
    driver.find_element(By.ID, 'password-confirm').send_keys('ucS7_!hQW8%ZXnh__')
    driver.find_element(By.NAME, 'register').click()
    sleep(30)
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Подтверждение телефона'

def test_recover_password_keyrtru(driver):
    driver.get('https://key.rt.ru')
    sleep(20)
    driver.find_element(By.CLASS_NAME, 'go_mobile_kabinet').click()
    sleep(10)
    driver.find_element(By.ID, 'forgot_password').click()
    sleep(10)
    driver.find_element(By.ID, 'username').send_keys('natakhol@mail.ru')
#     # Вводим email
#     sleep(15)
    driver.find_element(By.ID, 'reset').click()
    sleep(10)
    assert driver.find_element(By.ID, 'card-title').text == 'Восстановление пароля'







def test_auth_unregistered_telephone_log_smarthomertru(driver):
    driver.get(
        'https://lk.smarthome.rt.ru')
    sleep(20)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    sleep(20)
    driver.find_element(By.ID, 'username').send_keys('+79536370503')
    #     # element = WebDriverWait(driver, 10).until(
#     #     EC.element_to_be_clickable(By.CLASS_NAME, 'nav-link')
#
#     # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys('ucS7_!hQW8%ZXnh')
#     # явное ожидание присутствия элемента в структуре документа.
#     # element = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.CLASS_NAME, 'btn-success'))
#     # )
# #
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    sleep(10)

    # Проверяем, что введены верные данные в поля логин(номер телефона, почта), пароль:
    assert driver.find_element(By.CLASS_NAME, 'sc-aXZVg').text == 'Создание нового аккаунта'

def test_auth_blank_value_log_smarthomertru(driver):
    driver.get(
        'https://lk.smarthome.rt.ru')
    sleep(20)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    sleep(20)
#
# #
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    sleep(10)

    # Проверяем, что введены верные данные в поля логин(номер телефона, почта), пароль:
    assert driver.find_element(By.ID, 'username-meta').text == 'Введите номер телефона', 'Введите адрес, указанный при регистрации' 'Введите логин, указанный при регистрации'
#




def test_registration_smarthomertru(driver):
    driver.get(
        'https://lk.smarthome.rt.ru')
    sleep(20)
    driver.find_element(By.ID, 'standard_auth_btn').click()

    sleep(10)
    driver.find_element(By.ID, 'kc-register').click()
    # Вводим email
    sleep(15)
    driver.find_element(By.NAME, 'firstName').send_keys('Наталья')
    driver.find_element(By.NAME, 'lastName').send_keys('Мамина')
    # driver.find_element(By.XPATH, "//input[@autocomplete='new-password']").clear()
    # driver.find_element(By.XPATH, "//input[@autocomplete='new-password']").send_keys('Саратовская облdriver.find_element(By.ID, 'address').send_keys('natamamina2503@yandex.ru')
    driver.find_element(By.ID, 'address').send_keys('+79536370503')
    driver.find_element(By.ID, 'password').send_keys('ucS7_!hQW8%ZXnh__')
    driver.find_element(By.ID, 'password-confirm').send_keys('ucS7_!hQW8%ZXnh__')
    driver.find_element(By.NAME, 'register').click()
    sleep(30)
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Подтверждение телефона'


def test_registration_smarthomertru_registered_account(driver):
    driver.get(
        'https://lk.smarthome.rt.ru')
    sleep(20)
    driver.find_element(By.ID, 'standard_auth_btn').click()

    sleep(10)
    driver.find_element(By.ID, 'kc-register').click()
    # Вводим email
    sleep(15)
    driver.find_element(By.NAME, 'firstName').send_keys('Наталья')
    driver.find_element(By.NAME, 'lastName').send_keys('Мамина')
    # driver.find_element(By.XPATH, "//input[@autocomplete='new-password']").clear()
    # driver.find_element(By.XPATH, "//input[@autocomplete='new-password']").send_keys('Саратовская облdriver.find_element(By.ID, 'address').send_keys('natamamina2503@yandex.ru')
    driver.find_element(By.ID, 'address').send_keys('+79536370505')
    driver.find_element(By.ID, 'password').send_keys('ucS7_!hQW8%ZXnh__')
    driver.find_element(By.ID, 'password-confirm').send_keys('ucS7_!hQW8%ZXnh__')
    driver.find_element(By.NAME, 'register').click()
    sleep(30)
    assert driver.find_element(By.CLASS_NAME, 'card-modal__title').text == 'Учётная запись уже существует'

def test_recover_password_smarthomertru_incorrect(driver):
    driver.get('https://lk.smarthome.rt.ru')
    sleep(30)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    sleep(10)
    driver.find_element(By.ID, 'forgot_password').click()
    sleep(10)
    driver.find_element(By.ID, 'username').send_keys('natakhol@mail')
#     # Вводим email
#     sleep(15)
    driver.find_element(By.ID, 'reset').click()
    sleep(10)
    assert driver.find_element(By.ID, 'card-title').text == 'Восстановление пароля'
    assert driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или текст с картинки'

def test_login_using_authorization_code_smarthomertru_incorrect_email(driver):
    driver.get('https://lk.smarthome.rt.ru')
    sleep(15)
    driver.find_element(By.ID, 'address').send_keys('+795363705')
    driver.find_element(By.ID, 'otp_get_code').click()
    sleep(10)
    assert driver.find_element(By.ID, 'address-meta').text == 'Неверный формат телефона'
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text != 'Код подтверждения отправлен' 'Авторизация по коду'

def test_login_using_authorization_code_smarthomertru_with_email(driver):
    driver.get(
        'https://lk.smarthome.rt.ru')
    sleep(15)
    driver.find_element(By.ID, 'address').send_keys('natakhol@mail.ru')
    driver.find_element(By.ID, 'otp_get_code').click()
    sleep(10)
    assert driver.find_element(By.ID, 'address-meta').text == 'Введите номер телефона'



