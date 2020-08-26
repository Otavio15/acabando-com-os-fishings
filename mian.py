
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

while True:
    url = "http://control-2wcart.com/6cf5f7a669?fbclid=IwAR3BboLKaMPhTrGI3mJLW_CEanmGIXxxQkVuoohLr2-9mdULzz2y6gCPYlI"

    option = Options()
    option.headless = False
    driver = webdriver.Chrome(options=option)
    driver.get(url)

    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div[5]/div[1]/div[4]/div[2]/button/i").click()
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/a[2]/button').click()
    time.sleep(1)

    login = driver.find_element_by_xpath('//*[@id="input-login-e0a286fa"]')
    login.click()
    time.sleep(0.1)
    login.send_keys("Vai se fuder FDP")

    time.sleep(1)

    senha = driver.find_element_by_xpath('//*[@id="input-password-2de88008"]')
    senha.click()
    time.sleep(0.1)
    senha.send_keys("Vai roubar os dados da tua mãe fdp")

    driver.find_element_by_xpath('//*[@id="LoginBox-form"]/button').click()

    time.sleep(1.5)

    driver.quit()