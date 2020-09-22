#importing the required libraries
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#open the web brower using webdriver extention
Path = "chromedriver"
browser = webdriver.Chrome(Path)
#open the website you have to work on
browser.get("https://www.tripadvisor.com")

#click on hotels 
link = browser.find_element_by_link_text('Hotels').click()

#select the search option and type New Delhi
box = browser.find_element_by_xpath('/html/body/div[4]/div/form/input[1]')
box.send_keys('New Delhi')
box.submit()

#click on the Hotels Button
link2 = browser.find_element_by_link_text('Hotels').click()

#initialize different lists to store data 
n = []
p = []
r = []
rank = []

#give the exception command to avoid disturbances
try:
    pages = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "listing_title")))
#scrap the first item = name of hotels
    item1 = browser.find_elements_by_class_name('listing_title')
    for i in range(len(item1)):
        name = item1[i].text
        n.append(name)                                                        #append in the intialized list
#scrap the second item = prices displayed        
    item2 = browser.find_elements_by_class_name('price-wrap')
    for i in range(len(item2)):
        price = item2[i].text
        p.append(price)                                                       #append in the intialized list
#scrap the third item = number of reviews
    item3 = browser.find_elements_by_class_name('review_count')
    for i in range(len(item3)):
        reviews = item3[i].text
        r.append(reviews)                                                     #append in the intialized list
#scrap the fourth item = ranking
    item4 = browser.find_elements_by_class_name('popindex')
    for i in range(len(item4)):
        index = item4[i].text
        rank.append(index)                                                    #append in the intialized list
        
except:
    print("Data not located")

#take all the lists and convert them into data frame of 4 columns             
df = pd.DataFrame(list(zip(n, p, r, rank)), columns = ['Hotel Name', 'Prices', 'Number_of_Reviews', 'Ranking'])

#convert the stored data frame into csv file and store it in the same directory
CSV = df.to_csv('internship.csv', index=False)
 
