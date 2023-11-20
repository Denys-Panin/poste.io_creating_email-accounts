import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from helpers import generate_random_password
from dotenv import load_dotenv

load_dotenv()

start = int(input('Enter start: '))
stop = int(input('Enter stop: '))


def login(user, password):
    # --REGISTRATION--
    # Define options for running the chromedriver WITH USER INTERFACE
    service = webdriver.ChromeService(executable_path='chrome_driver/chromedriver')
    browser = webdriver.Chrome(service=service)

    # Define options for running the chromedriver for DOCKER
    # chrome_options = Options()
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # browser = webdriver.Chrome(options=chrome_options)

    browser.get(os.getenv('URL_LOGIN'))
    browser.get(os.getenv('URL_LOGIN'))

    email_input = browser.find_element("id", "email")
    email_input.clear()
    email_input.send_keys(user)

    pass_input = browser.find_element('id', 'password')
    pass_input.clear()
    pass_input.send_keys(password)
    pass_input.send_keys(Keys.ENTER)

    # --CREATE A NEW EMAIL POST--
    for index, _ in enumerate(range(start, stop + 1), start=start):
        password = generate_random_password()
        email = f'{index}admin'
        browser.get(os.getenv('URL_CREATE'))

        name_input = browser.find_element('id', 'name')
        name_input.clear()
        name_input.send_keys(f'{index}admin@xneo.site')

        email_input_1 = browser.find_element('id', 'user')
        email_input_1.clear()
        email_input_1.send_keys(email)

        # show_password = browser.find_element('id', 'show-password')
        # show_password.click()

        reg_pass_input = browser.find_element('id', 'passwordPlaintext')
        reg_pass_input.clear()
        reg_pass_input.send_keys(password)
        reg_pass_input.send_keys(Keys.ENTER)

        with open('data.txt', 'a') as file:
            file.write(f'{email}@example.site;{password}\n')

    browser.get(os.getenv('URL_LIST'))
    browser.close()
    browser.quit()


login(os.getenv('USER_'), os.getenv('PASSWORD_'))
