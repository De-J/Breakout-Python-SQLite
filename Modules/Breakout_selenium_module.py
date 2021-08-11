from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from collections import defaultdict

def search_function() -> [list]:
    driver = webdriver.Firefox(executable_path = r"C:\Program Files (x86)\geckodriver.exe")
    l = []
    companies = []    
    total_rooms = []
    
    for i in range(1, 5):
        driver.get(f"https://lock.me/en/usa/companies?page={i}&incremental=1")
        company_list = driver.find_elements_by_xpath("//main/section[@class = 'full_list']/div/div/article[@class = 'tile_full']")
        
        for company in company_list:
            total_rooms.append(((company.find_element_by_tag_name("li").text).strip(" rooms")))
            companies.append((company.find_element_by_tag_name("h4")).text)
    l.append(companies)
    l.append(total_rooms)
    return l 

if __name__ == "__main__":
   print(search_function())


'''
cl = sqlite3.connect("Company_List.db")
cur = cl.cursor()
cur.execute("CREATE TABLE Company_List (Company_name text, total_rooms_in_USA smallint")
cur.execute(f"INSERT INTO Company_List VALUES ({})"
'''


