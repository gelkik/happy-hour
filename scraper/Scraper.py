import requests
from bs4 import BeautifulSoup


# text = 'geeksforgeeks'
# url = 'https://google.com/search?q=' + text

# doc=BeautifulSoup(requests.get(url).text,'html.parser')
# # print(doc)
# heading_object = doc.find_all('h3')
# for info in heading_object:
#     print(info.getText())
#     print("------")




# browser = webdriver.Chrome('C:\\path\\to\\chromedriver.exe')
# browser = webdriver.Chrome('C:\\Users\\gelki\\Downloads\\chromedriver_win32\\chromedriver')
# browser = webdriver.Chrome("C:\\Users\\gelki\\Downloads\\chromedriver_win32\\chromedriver.exe")
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only

# browser = webdriver.Chrome(driver)

url = 'http://www.juniperbarnyc.com/'
data = requests.get(url)
html = BeautifulSoup(data.text, 'html.parser')

print(html)