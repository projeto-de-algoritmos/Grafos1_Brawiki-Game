#python3 -m pup install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from fake_useragent import UserAgent
from time import sleep 

base_url = 'https://pt.wikipedia.org/'

options = webdriver.ChromeOptions()
ua = UserAgent()
user_agent = ua.random
options.add_argument(f'--user-agent={user_agent}')
service = ChromeService(executable_path='../driver/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

def scrollToElement(title):
    
    sleep(3)
    driver.execute_script('$("#collapseButton0").click();')
    sleep(2)
    driver.execute_script('$([document.documentElement, document.body]).animate({scrollTop: $("a[title='+"'"+title+"'"+']").offset().top}, 3000);')
    sleep(4)
    driver.execute_script('$("a[title='+"'"+title+"'"+']").css({"background-color":"red","color":"yellow"})')
    sleep(2)
    print('window.location.href = "'+base_url+'wiki/'+title+'"')
    driver.execute_script('window.location.href = "'+base_url+'wiki/'+title+'"')

def pilot(path):
    driver.get(base_url+"/wiki/"+path[0]);
    print(path)
    for val in path[1:]:
        url = "/wiki/" + val
        print(url)
        scrollToElement(val)
        sleep(3)

