from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
import time
import os
import fnmatch
f= len(fnmatch.filter(os.listdir(os.getcwd()+"/input/"), '*.jpg'))
#prox = Proxy()
#prox.proxy_type = ProxyType.MANUAL
#prox.ssl_proxy = "93.171.27.99:53281"
#capabilities = webdriver.DesiredCapabilities.CHROME
#prox.add_to_capabilities(capabilities)

for a in range(1,f+1):
    #browser = webdriver.Chrome(desired_capabilities=capabilities)
    browser = webdriver.Chrome()
    browser.get('https://images.google.com/') 
    browser.find_elements_by_class_name('S3Wjs')[0].click()
    av=browser.find_elements_by_class_name('qbtbha')
    browser.find_element_by_id("qbfile").send_keys(os.getcwd()+"/input/"+str(a)+".jpg")
    results = browser.find_elements_by_class_name('O1id0e')
    if results[0].text=="No other sizes of this image found.":
        try:
            fh = open(os.getcwd()+"/output/report.csv", 'r')
        except FileNotFoundError:
            fh = open(os.getcwd()+"/output/report.csv",'w')
            fh.close()
        f = open(os.getcwd()+"/output/report.csv", 'a')
        f.write(str(a)+",original\n")
        f.close()
        print(str(a)+" original")
    else :
        try:
            fh = open(os.getcwd()+"/output/report.csv", 'r')
        except FileNotFoundError:
            fh = open(os.getcwd()+"/output/report.csv",'w')
            fh.close()
        f = open(os.getcwd()+"/output/report.csv", 'a')
        f.write(str(a)+",duplicate\n")
        f.close()
        print(str(a)+" duplicate")
    browser.quit()