from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pprint import pformat
from time import sleep



def mylousyprintfunction(eventdata):
    if eventdata.get("params")
    print(pformat(eventdata))


if __name__ == '__main__':
    import undetected_chromedriver.v2 as uc
    print("Insert your OF email")
    # username=input()
    username="crypm"
    print("Insert your OF password (yah, that sucks, but we ain't doing nothing with it)")
    # password=input()
    password=""
    print("Opening chrome to login...")
    driver = uc.Chrome(enable_cdp_events=True)
    delay = 15  # seconds
    captcha_delay = 75  # seconds
    driver.get("https://www.onlyfans.com")

    try:
        loginForm = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'input-27')))
        loginForm.send_keys(username)
        passForm = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'input-29')))
        passForm.send_keys(password)
        passForm.send_keys(Keys.ENTER)
        print("Please solve the captcha")
        driver.add_cdp_listener('Network.requestWillBeSent', mylousyprintfunction)
        driver.add_cdp_listener('Network.dataReceived', mylousyprintfunction)
        success = WebDriverWait(driver, captcha_delay).until(EC.presence_of_element_located((By.ID, 'new_post_text_input')))
        print("Should be logged in now")
    except TimeoutException:
        print("Loading took too much time!")
    for i in range(10): sleep(1);print("Gathering cookies...")

    driver.quit()