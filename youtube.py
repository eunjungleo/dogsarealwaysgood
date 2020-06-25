from selenium import webdriver
import csv, itertools

chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)


driver.get('https://www.youtube.com/playlist?list=PLpuzWnAKjQgBBH113_kOsBGCZO8MVNazu')

get_url = driver.find_elements_by_css_selector('#content > a')
get_title = driver.find_elements_by_css_selector('#video-title')

f = open('youtube.csv', mode='a', encoding='utf-8', newline='')
writer = csv.writer(f)
writer.writerow(["url", "y_title"])
for u in get_url:
    url = u.get_attribute("href")
for t in get_title:
    y_title = t.text
    writer.writerow([url, y_title])

driver.quit()