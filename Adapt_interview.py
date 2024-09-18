from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from time import sleep
def setup():
    driver=WebDriver()
    option=Options()
    option.add_argument('--disable-Notifications')
    return driver
patent=setup()
patent.get("https://patinformed.wipo.int/")
patent.implicitly_wait(10)
patent.maximize_window()
sleep(1)
patent.find_element('xpath','//input[@class="searchField"]').send_keys("tigecycline")
# pop=patent.switch_to.alert
# pop.accept()
sleep(1)
patent.find_element('xpath',"//button[text()='I have read and agree to the terms']").click()
sleep(1)
patent.find_element('xpath',"//div[contains(text(),'Novel 7-substituted-9- Substituted Amino-6-demethyl-6-deoxytetracyclines')]").click()
sleep(1)
column_names=patent.find_elements('xpath','//table[@class="patentDetails noBorder"]/tr/td/b')
column_values=patent.find_elements('xpath','//table[@class="patentDetails noBorder"]/tr/td/b/../../td[2]')
heading_names=[]
for name in column_names:
    heading_names.append(name.text)
for nam in heading_names:
    if nam not in ("Filing date","Grant date","Grant number"):
        data=patent.find_element('xpath',f'//table[@class="patentDetails noBorder"]/tr/td/b[text()="{nam}"]/../../td[2]').text
        print(nam,"-",data)
        print('Not Found Publication date')
sleep(3)
print("Juridiction and Publication data displayed below:")
#Juridiction and Publication data:
patent.find_element('xpath',"//div[contains(text(),'TIGECYCLINE COMPOSITIONS AND METHODS OF PREPARATION')]").click()
sleep(1)
J=patent.find_elements('xpath',f'//ul[@class="results flex space-between"]/li[@class="result card container showButtonsOnHover"]/table[@class="patentDetails noBorder"]/tr/td/b[text()="Jurisdiction"]/../../td[2]')
P=patent.find_elements('xpath',f'//ul[@class="results flex space-between"]/li[@class="result card container showButtonsOnHover"]/table[@class="patentDetails noBorder"]/tr/td/b[text()="Publication date"]/../../td[2]')
for i in J:
    print(i.text)
for k in P:
    if k.text == None:
        print('Not Found Publish date')
    else:
        print(k.text)

# col_names=patent.find_elements('xpath','//table[@class="patentDetails noBorder"]/tr/td/b')
# col_values=patent.find_elements('xpath','//ul[@class="results flex space-between"]/li[@class="result card container showButtonsOnHover"]//table[@class="patentDetails noBorder"]/tr/td/b/../../td[2]')
# head_names=[]
# for item in col_names:
#     head_names.append(item.text)
# print(head_names)
# for patents in head_names:
#     if patents == "Jurisdiction":
#       J=patent.find_elements('xpath',f'//ul[@class="results flex space-between"]/li[@class="result card container showButtonsOnHover"]/table[@class="patentDetails noBorder"]/tr/td/b[text()="{patents}"]/../../td[2]')
#       for i in J:
#           print(i.text)
#     elif patents=="Publication date":
#         P=patent.find_elements('xpath',f'//ul[@class="results flex space-between"]/li[@class="result card container showButtonsOnHover"]/table[@class="patentDetails noBorder"]/tr/td/b[text()="{patents}"]/../../td[2]')
#         for pub_date in P:
#             print(pub_date.text)
#     else:
#         print("Not found")
patent.close()






