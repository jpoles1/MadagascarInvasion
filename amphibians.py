import urllib3
import xml.etree.ElementTree as ET
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
def fetchWebpage(dataurl):
    #Get webpage html data
    http = urllib3.PoolManager()
    res = http.request('GET', dataurl)
    rawhtml = res.data.decode('utf-8')
    return rawhtml;
url = "http://amphibiaweb.org/cgi/amphib_ws_locality?orderbyaw=Order&rel-isocc=eq&where-isocc=MG"
dat = fetchWebpage(url)
tree = ET.fromstring(dat)
