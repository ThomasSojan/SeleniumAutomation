import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# options = webdriver.ChromeOptions() 
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
userId="tsojan.ext@libertyglobal.com"
password ="Appu@1997"
serv_obj = Service("./chromeDriver/chromedriver.exe")
driver = webdriver.Chrome(service = serv_obj)
driver.implicitly_wait(10)
auto_wait = WebDriverWait(driver,60)
driver.get("https://snf625.dynatrace-managed.com/e/367fef8e-4e50-4d71-9029-c4e067198777/ui/services?gtf=-24h%20to%20now&gf=-6895710036663692313&sorting=name;asc")
driver.maximize_window()


def authenticateDT(userId,password):
    driver.find_element(By.XPATH,"//input[@id='user']").send_keys(userId)
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys(password)
    driver.find_element(By.XPATH,"//input[@value='Sign in']").click()
    print(driver.title)
    if(driver.title == "Services - LGI PROD - Dynatrace"):
        print("Sucessfully Logged In")
    else:
        print("Failed Logging In")
        exit() 

def moduleCheck(moduleInfo):
    print(moduleInfo.get('moduleName')+" in-progress")
    searchboxProcessGroup=auto_wait.until(EC.presence_of_element_located((By.XPATH,"//input[@class='dt-autocomplete-trigger dt-element-trigger dt-filter-field-input ng-tns-c79-6']")))
    searchboxProcessGroup.send_keys("Process group")
    auto_wait.until(EC.presence_of_element_located((By.XPATH,"//mark[@class='dt-highlight-mark']"))).click()
    time.sleep(2)
    searchBox = auto_wait.until(EC.presence_of_element_located((By.XPATH,"//input[@class='dt-autocomplete-trigger dt-element-trigger dt-filter-field-input ng-tns-c79-6']"))) 
    searchBox.send_keys(moduleInfo.get('moduleName'))
    moduleNameXPATH = "//mark[text()='"+moduleInfo.get('moduleName')+"']"
    auto_wait.until(EC.presence_of_element_located((By.XPATH,moduleNameXPATH))).click()
    #time.sleep(5)
    # compleateServices = auto_wait.until(EC.presence_of_all_elements_located((By.XPATH,"//dt-table[@class='dt-table cdk-table dt-table-interactive-rows']//a")))
    # for element in compleateServices:
    #     print(element.text)

    for service in moduleInfo.get("services"):
        print(service)
        serviceNameXPATH="//span[text()='"+service+"']"
        auto_wait.until(EC.presence_of_element_located((By.XPATH,serviceNameXPATH))).click()
        analyzeModule()
        driver.back()
        driver.back()
        time.sleep(5)


    print(moduleInfo.get('moduleName')+" finished")

def analyzeModule():
    auto_wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Failure rate']"))).click()
    apiNameXPATH="//*[@id='rootPageContentElementId']/div/div[2]/div[1]/div[4]/div[2]/div/div[1]/div[1]/div/div/div/div/div/div[2]/table/tbody/tr/td/a[1]"
    failureRateXPATH="//*[@id='rootPageContentElementId']/div/div[2]/div[1]/div[4]/div[2]/div/div[1]/div[1]/div/div/div/div/div/div[2]/table/tbody/tr/td[3]"
    failure_4xx = "//*[@id='rootPageContentElementId']/div/div[2]/div[1]/div[4]/div[2]/div/div[1]/div[1]/div/div/div/div/div/div[2]/table/tbody/tr/td[4]"
    failure_5xx = "//*[@id='rootPageContentElementId']/div/div[2]/div[1]/div[4]/div[2]/div/div[1]/div[1]/div/div/div/div/div/div[2]/table/tbody/tr/td[5]"
    
    time.sleep(10)




authenticateDT(userId,password)
moduleInfo = {
    'moduleName':'ch-asap-provision-int',
    'services':['ASAPProvisionV1','VoipProvisionV1']
}
moduleCheck(moduleInfo)

    


time.sleep(10)
driver.close()

