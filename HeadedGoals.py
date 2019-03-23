from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')

browser = webdriver.Chrome(ChromeDriverManager().install())
url="https://www.premierleague.com/stats/top/clubs/att_hd_goal?se=79"

browser.get(url)
soup = BeautifulSoup(browser.page_source,features="html5lib")

rows = soup.find_all('tr')
for row in rows[1:4]:
    row_td_club = str(row.find_all())
    print(row_td_club)

'''
select = Select(browser.find_element_by_class('dropDown mobile'))
select.select_by_visible_text('2017/18')
print(select)
'''

'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get('url')

select = Select(driver.find_element_by_id('fruits01'))

# select by visible text
select.select_by_visible_text('Banana')

# select by value 
select.select_by_value('1')
'''