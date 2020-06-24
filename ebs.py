from selenium import webdriver
import csv, itertools

chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

# ebs 

xpath = 'ul.lst_pro03 > li > div.txtcon_area'

for i in range(1,6):

    path_1="https://home.ebs.co.kr/baddog/replay/5/list?c.page=" + str(i) + "&searchKeywordValue=0&orderBy=NEW&searchConditionValue=0&vodSort=NEW&courseId=10016245&searchStartDtValue=0&brdcDsCdFilter=RUN&userId=&searchKeyword=&searchCondition=&searchEndDt=&searchEndDtValue=0&stepId=10017539&searchStartDt=&"
    path_2="https://home.ebs.co.kr/baddog/replay/14/list?c.page="+ str(i) +"&searchKeywordValue=0&orderBy=NEW&searchConditionValue=0&vodSort=NEW&courseId=10016245&searchStartDtValue=0&brdcDsCdFilter=RUN&userId=&searchKeyword=&searchCondition=&searchEndDt=&searchEndDtValue=0&stepId=10027901&searchStartDt=&"
    path_3="https://home.ebs.co.kr/baddog/replay/24/list?c.page="+ str(i) + "&searchKeywordValue=0&orderBy=NEW&searchConditionValue=0&courseId=10016245&vodSort=NEW&searchStartDtValue=0&brdcDsCdFilter=RUN&searchKeyword=&userId=&searchEndDt=&searchCondition=&searchEndDtValue=0&stepId=10035139&searchStartDt=&"
    path_list = [path_1, path_2, path_3]

    for p in path_list:
        driver.get(p)
        title = driver.find_elements_by_css_selector(xpath + '> strong > a')
        id_num = driver.find_elements_by_css_selector(xpath + '> span.num_info')
        date = driver.find_elements_by_css_selector(xpath + '> span.date_info')

        list = zip(id_num, title, date)

        for a,b,c in list:
            id = [ print(a.text) ]
            title = [ print(b.text) ]
            date = [ print(c.text) ]

            a_list = zip(id, title, date)

"""
            # csv
            f = open('ebs.csv', 'w', encoding='utf-8', newline='')
            wr = csv.writer(f)
            wr.writerow(a_list)
            f.close()
"""
        
driver.quit()
