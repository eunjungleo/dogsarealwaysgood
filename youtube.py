from selenium import webdriver
import csv, itertools

chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)


driver.get('https://www.youtube.com/playlist?list=PLpuzWnAKjQgBBH113_kOsBGCZO8MVNazu')
get_url = driver.find_elements_by_css_selector('#content > a')
for u in get_url:
    url = u.get_attribute("href")
    print(url)

get_title = driver.find_elements_by_css_selector('#video-title')
for t in get_title:
    y_title = t.text
    print(y_title)

driver.quit()