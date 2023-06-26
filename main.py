import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
TIMEOUT = 60



def login():
    bot=driver.get("http://localhost/glpi/index.php?noAUTO=1")


    print("[Info] - Logging in...")
    login_name = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/form/div/div/div[2]/input")
    login_name.send_keys("glpi")
    password = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/form/div/div/div[3]/input")
    password.send_keys("glpi")
    sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/form/div/div/div[6]/button")
    sign_in.click()

def imprimante():
    time.sleep(4)
    imp = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/main/div/div/div/div/div/div[1]/div[2]/div[3]/div[13]/div/a')
    imp.click()
    imp = driver.find_element(By.XPATH, '/html/body/div[2]/header/div/ul/li[1]/a')
    imp.click()
    time.sleep(6)

def insert_data():
    dropdown = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div/div/div/div/form/div/div[3]/div/div/div/div/div[2]/div/div/select')  # replace 'dropdown_id' with the actual ID of the dropdown element
    time.sleep(7)
    options = dropdown.options
    for option in options:
        print(option.text)
    time.sleep(555)


if __name__ == '__main__':
    login()
    imprimante()
    insert_data()
