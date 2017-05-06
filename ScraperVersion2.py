
# Navigate to a webpage
from selenium import webdriver


from selenium.webdriver.common.keys import Keys #Importing keys
import os
#print os.getcwd() #to understand the working directory

driver = webdriver.Chrome()
#Pull Search Terms from a CSV File
file = open('searchdata.txt', 'r')
while True:
	srchtxt = file.readline()
	if not srchtxt: break
	driver.get('http://www.justdial.com/') #opening justdial

	search_box = driver.find_element_by_id("srchbx") #findng searchbox
	search_box.send_keys(srchtxt, Keys.RETURN) #sending text and Enter
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #to scroll to page bottom
#BROWSER WAIT to be included

text_file = open('urllist.txt', 'a') #open text file to copy all urls
#using append instead of write
#content = driver.find_element_by_class_name('cntanr')
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    #print elem.get_attribute("href")
    text_file.write(elem.get_attribute("href") + "\n")
clss = driver.find_elements_by_class_name('cntanr')
for cls in clss:
	text_file.write(cls.text + "\n")

text_file.close()



file.close()








#close browser
driver.close()
