# import requests
# from bs4 import BeautifulSoup


# text = 'geeksforgeeks'
# url = 'https://google.com/search?q=' + text

# doc=BeautifulSoup(requests.get(url).text,'html.parser')
# # print(doc)
# heading_object = doc.find_all('h3')
# for info in heading_object:
#     print(info.getText())
#     print("------")

from selenium import webdriver
# import pandas as pd
import time
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
from parsel import Selector
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


chrome_options = Options()

#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only

chrome_options.add_argument("--headless")
browser = webdriver.Chrome()
url = 'https://www.google.com/maps/search/nyc+happy+hour/@40.7561842,-74.026765,13z/data=!3m1!4b1?entry=ttu'
browser.get(url)
page_content = browser.page_source
response = Selector(page_content)
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

############ OPENS SOMETHING
action = ActionChains(browser)
element = browser.find_element(By.XPATH,'//body[1]/div[3]/div[9]/div[9]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]')

##################################################################
### THIS ACTION OPENS THE MAPS SEARCH AND TRIES TO SCROLL DOWN
# action.move_to_element(element).click()
# browser.action.scroll_by(100, 200).perform
# time.sleep(2.5)
# scroll_origin = ScrollOrigin.from_element(element, 10, 10)

# action.scroll_from_origin(scroll_origin, 0, 1000).perform()
# time.sleep(2.5)
##################################################################


# def scroll(response):
#     for i in range(6,25,3): 
#         # last_review = self.find_elements_by_css_selector('div[jstcache="192"]')
#         last_review = response.find_elements(By.CSS_SELECTOR,'div[jstcache="192"]')
#         response.execute_script('arguments[0].scrollIntoView(true);', last_review[i])
#         time.sleep(5)
# scroll(browser)

## TRYING TO SCROLL TO BOTTOM

# def scroll_to_bottom(driver):
#     container = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//div[@id="pane"]/div/div/div/div[1]'))
#     )

#     prev_height = 0
#     curr_height = container.size['height']

#     while curr_height > prev_height:
#         prev_height = curr_height
#         driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight);', container)
#         driver.implicitly_wait(1)
#         curr_height = container.size['height']
# scroll_to_bottom(browser)

##########LOOKS FOR LINK AND TITLE
results = []
def extracting_maps(results):
    for el in response.xpath('//div[contains(@aria-label, "Results for")]/div/div[./a]'):
        results.append({
            'link': el.xpath('./a/@href').extract_first(''),
            'title': el.xpath('./a/@aria-label').extract_first(''),
        })
    return results
extracting_maps(results)


############CLICKS ON THE REVIEWS FOR EACH LISTING
def finding_links(results):
    reviews = []
    for i in results:
        url = i['link']
        browser.get(url)
        # page_content = browser.page_source
        # response = Selector(page_content)
        action = ActionChains(browser)
        name = browser.find_element(By.XPATH,"//h1[normalize-space()]").text
        element = browser.find_element(By.XPATH,f'//button[@aria-label="Reviews for {name}"]')
        action.move_to_element(element).click().perform()
        # time.sleep(3)
        try:
            ####NOT CLICKING ON HAPPY HOUR IN REVIEWS#####
            rev_num = browser.find_element(By.CSS_SELECTOR,"span[class='bC3Nkc fontBodySmall']").text
            element = browser.find_element(By.XPATH,f'//button[contains("@aria-label=happy hour, mentioned in {rev_num} reviews")]')
            print(element)
            action.move_to_element(element).click().perform()
        except:
            pass
    return reviews
# finding_links(results)


def finding_photos(results):
    for i in results:
        url = i['link']
        browser.get(url)
        action = ActionChains(browser)
        element = browser.find_element(By.XPATH,f"//button[@aria-label='All']")
        action.move_to_element(element).click().perform()
        time.sleep(1)
        #### CLICKS ON MENU IN THE PHOTOS TAB
        try:
            menu_click = browser.find_element(By.XPATH,f"//div[contains(text(),'Menu')]")
            action.move_to_element(menu_click).click().perform()
            time.sleep(3)
        except:
            pass
        ##### CLICKS ON EVERY PIC IN MENU TAB IN 'ALL' PHOTOS
        try:
            for x in range(1,21):
                menu_pics = browser.find_element(By.XPATH,f"//body[1]/div[3]/div[9]/div[9]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[{x}]/div[1]/a[1]/div[1]/div[1]")
                action.move_to_element(menu_pics).click().perform()
        except:
            pass

finding_photos(results)


















def rev_click():
    url = "https://www.google.com/maps/place/Cooper's+Craft+%26+Cocktails/@40.742705,-74.000776,17z/data=!4m8!3m7!1s0x89c259beaae61525:0x788974106dcc4597!8m2!3d40.742705!4d-74.000776!9m1!1b1!16s%2Fg%2F11b6dqyjhl?authuser=0&hl=en&entry=ttu"
    browser.get(url)
    action = ActionChains(browser)
    name = browser.find_element(By.XPATH,"//h1[normalize-space()]").text
    element = browser.find_element(By.XPATH,f'//button[@aria-label="Reviews for {name}"]')
    action.move_to_element(element).click().perform()
    time.sleep(5)
# rev_click()



# url = i[0]
# browser.get(url)
# page_content = browser.page_source
# response = Selector(page_content)
# websites.append(response.xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[11]/div[6]/a/div/div[2]/div[2]/text()').get())
# print(websites)