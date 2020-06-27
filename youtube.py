from selenium import webdriver
import csv, itertools, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

# approach youtube playlist
driver.get('https://www.youtube.com/playlist?list=PLpuzWnAKjQgBBH113_kOsBGCZO8MVNazu')

body = driver.find_element_by_tag_name('body')

num_of_pagedowns = 300
while num_of_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    num_of_pagedowns -= 1


# get url
get_url = driver.find_elements_by_class_name('yt-simple-endpoint.style-scope.ytd-playlist-video-renderer')

get_title = driver.find_elements_by_css_selector('#video-title')


f = open('youtube.csv', mode='w', encoding='utf-8', newline='')
writer = csv.writer(f)
writer.writerow(["url", "y_title", "join_title"])
for list in zip(get_url, get_title):
    url = list[0].get_attribute("href")
    title = list[1].text
    join_title = join_title = title.replace("세상에 나쁜 개는 없다 -",'').replace(" ","")[:5]
    writer.writerow([url, title, join_title])


driver.quit()