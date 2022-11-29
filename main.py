from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
#weather_scrapper
from bs4 import BeautifulSoup
from requests import get

s = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, service=s)

#get the first page
def login_twitter():
    try:
        driver.get("https://twitter.com/i/flow/login")
        driver.implicitly_wait(3)
        driver.maximize_window()



        #username
        username = driver.find_element(By.XPATH, '//input[@autocomplete="username"]')
        username.send_keys("") #account username 
        nextButton = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        nextButton.click()
        driver.implicitly_wait(5)

        #twitter username / unusual login

        unusual_login = driver.find_element(By.XPATH, '//input[@autocapitalize="none"]')
        unusual_login.send_keys('') #your twitter account name (in case of unusual login)
        driver.implicitly_wait(4)

        nextB = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        nextB.click()
        driver.implicitly_wait(5)

        #password
        password = driver.find_element(By.XPATH, '//input[@autocomplete="current-password"]')
        password.send_keys('') #your twitter account password
        logIn = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div')
        logIn.click()

        #cookies
        #cookies_accept = driver.find_element(By.LINK_TEXT, 'Refuse non-essential cookies')

    except Exception as e:
        print(e)

#call login
login_twitter()

#weather_scrapper
URL = 'https://pogoda.interia.pl/'

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

def parse_city(city):
    return str(city.replace(',', ''))

for weather in bs.find_all('section', class_ = 'weather-places-group cities-weather is-legend'): #pobieramy html tabeli
    city = weather.find('ul', class_ = 'weather-index').get_text().split()

    #print(*city, sep = '\n')

    break
data = []
for x in range(0,len(city),2):
   data.append([{city[x]: city[x+1]}])
   if x == 28:
       break

#storing the city names in variable
text = ''
city = iter(city[:-3])
for x in city:
    text += x +": " + next(city) + "\n"
# print(text)

# post tweet

def create_tweet():
    try:
        write_tweet = driver.find_element(By.XPATH, '//div[@aria-label="Tweet text"]')
        write_tweet.send_keys(text)
        driver.implicitly_wait(5)
        refuse_cookies = driver.find_element(By.XPATH, '(//span[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"])[6]')
        refuse_cookies.click()
        driver.implicitly_wait(5)
        post_tweet = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        post_tweet.click()
    except Exception as e:
        print(e)

create_tweet()

driver.quit()
