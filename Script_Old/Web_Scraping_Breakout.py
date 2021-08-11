from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import defaultdict
import pandas as pd
import numpy as np
driver = webdriver.Firefox(executable_path = r"C:\Program Files (x86)\geckodriver.exe")

driver.get("https://worldofescapes.com/map")
states = driver.find_elements_by_xpath("//section[@class = 'container cities']/div/div[@class = 'col-lg-3 col-md-4 col-sm-6 col-xs-6 state-item']")
#print(states.text)

'''
d = defaultdict(list)

for state in states:
    state_name = state.find_element_by_tag_name('h3')     
    state_cities = state.find_elements_by_tag_name('a')
    #d.setdefault(f"{state_name.text}")
    for i in state_cities:
        d[f"{state_name.text}"].append(i.text)
#dataset = pd.DataFrame(d)

for i in d.keys():
    print(d[i])
'''
d = []
names = []
for state in states:
    state_name = state.find_element_by_tag_name('h3')
    d.append(state_name.text)
    state_cities = state.find_elements_by_tag_name('a')
    l = []
    for i in state_cities:
        l.append(i.text)
    names.append(np.array(l))
#print(d)
#print(names)
dataset = pd.DataFrame(names, index = d)
b = dataset.transpose()
del b['Unnamed: 0']
#b.drop(b.columns[0], axis = 1, inplace = True)
b.to_csv('breakout_selenium.csv')
