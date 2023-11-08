import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc

def make_driver(head=False):
    viewport_sizes = [
    "1366x768",
    "1440x900",
    "1600x900",
    "1920x1080",
    "2560x1440"]
    options = uc.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito")
    options.headless=head
    viewport_size = random.choice(viewport_sizes)
    driver = uc.Chrome(options=options)
    return driver

def scroll_and_connect(url, driver, mail, password):
    driver.execute_script(f'''window.open("{url}","_blank");''')

    driver.switch_to.window(driver.window_handles[-1])

    time.sleep(2)
    try:
        dialog_tag = driver.find_element(By.CSS_SELECTOR, 'form[data-testid="royal_login_form"]')
    except:
        dialog_tag = 0
    
    
    if dialog_tag:
        email_element = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        email_element.send_keys(mail)

        password_element = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
        password_element.send_keys(password)
        password_element.send_keys(Keys.ENTER)
    
    time.sleep(4)


    

    return 1

def scroll_and_search(driver, search_word):
    
    search_tag = driver.find_element(By.CSS_SELECTOR,'input[aria-label="Rechercher sur Facebook"]')
    search_tag.send_keys(search_word)
    search_tag.send_keys(Keys.ENTER)
    
    time.sleep(3)

def scroll_and_click_publication(driver):
    publication_tag = driver.find_element(By.XPATH, "//span[text()='Publications']")
    publication_tag.click()
    time.sleep(3)

def scroll_and_get_hrefs(driver):
    res=[]
    href_tags = driver.find_elements(By.CSS_SELECTOR, 'div[data-ad-comet-preview="message"]')
    for a_tag in href_tags:
        href = a_tag.text
        res.append(href)
    return res

def scroll_and_get_html(driver):

    html = driver.page_source
    delay = random.uniform(3, 5)
    i=0
    last_height = driver.execute_script('return document.body.scrollHeight')
    res=[]
    while True:
        i+=1
        driver.execute_script('window.scrollTo(0, 0);')
        time.sleep(5)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(3)
        new_height = driver.execute_script('return document.body.scrollHeight')            
        if new_height == last_height or i==20:
            break
        last_height = new_height
        res+=scroll_and_get_hrefs(driver)
    
    
    html = driver.page_source

    driver.quit()
    
    return res
