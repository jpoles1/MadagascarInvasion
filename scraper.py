# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:22:09 2015

@author: Jordan Poles
"""
#Imports
import urllib3
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import seaborn as sns
#Preferences
figsize = (22, 17)
pal="GnBu_d"
#Get webpage
http = urllib3.PoolManager()
dataurl = 'http://www.issg.org/database/species/search.asp?sts=sss&st=sss&fr=1&x=41&y=6&sn=&rn=Madagascar&hci=-1&ei=-1&lang=EN'
res = http.request('GET', dataurl)
rawhtml = res.data.decode('utf-8')
#Load up beautiful soup
soup = BeautifulSoup(rawhtml, 'html.parser')
alltext = soup.body.get_text();
#Names
namesdom = soup.find_all("span", class_="ListTitle")
names = []
for row in namesdom:
    try:
        names.append(row.i.get_text());
    except:
        pass;
#May taxonomic data
taxadom = soup.find_all("span", class_="Info")
taxa = []
for row in taxadom:
    taxa.append(row.get_text());
taxa = [row for row in taxa if row[0]==" "]
#Analysis
import pandas as pd
data = pd.DataFrame({"name": names, "taxa": taxa})
data = data.iloc[0:58,:] #Selects only the invasive species
#Cleaning
data["taxa"] = data["taxa"].apply(lambda st : st.strip().replace(")", "").replace("(", ""));
#Plotting
groupct = data["taxa"].value_counts();
plt.figure(figsize=figsize)
sns.barplot(y=groupct.index, x=groupct, palette=pal)
plt.ylabel("\nOrganism Type", fontsize=25)
plt.xlabel("# of Invasive Species\n", fontsize=25)
plt.title("\nDistribution of Various Invasive Species Types\n", fontsize=40)
plt.tick_params(labelsize=28)
plt.tight_layout()
plt.savefig("speciestypes.png")
plt.close()