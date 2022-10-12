import os
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# os.environ['PATH'] += r"./chromeDriver/"
# driver = webdriver.Chrome()
# driver.get("https://google.com")
# x=driver.title
# print(x)


userId="tsojan.ext@libertyglobal.com"
password ="Appu@1997"
driver = webdriver.Chrome(executable_path="./chromeDriver/chromedriver.exe")

#Signing in
driver.get("https://snf625.dynatrace-managed.com/")
driver.find_element("xpath","//input[@id='user']").send_keys(userId)
driver.find_element("xpath","//input[@id='password']").send_keys(password)
driver.find_element("xpath","//input[@value='Sign in']").click()
sleep(5)

#Service Page
driver.get("https://snf625.dynatrace-managed.com/e/367fef8e-4e50-4d71-9029-c4e067198777/ui/services?gtf=-24h%20to%20now&gf=-6895710036663692313&sorting=name;asc")
driver.implicitly_wait(3)
driver.find_element("xpath","//input[@class='dt-autocomplete-trigger dt-element-trigger dt-filter-field-input ng-tns-c79-6']").send_keys("Process group")
driver.find_element("xpath","//mark[@class='dt-highlight-mark']").click()
driver.implicitly_wait(2)
driver.find_element("xpath","//input[@placeholder='Enter a value to search']").send_keys("pl-oesp-customer-exp")
driver.implicitly_wait(2)
driver.find_element("xpath","//mark[@class='dt-highlight-mark']").click()




