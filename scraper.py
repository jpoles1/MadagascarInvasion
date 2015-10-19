# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:22:09 2015

@author: Jordan Poles
"""
#Imports
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import re
#Preferences
figsize = (22, 17)
pal="GnBu_d"
urlprefix = "http://www.issg.org/database/species/"
def runAnalysis():
    madagascarURL = 'http://www.issg.org/database/species/search.asp?sts=sss&st=sss&fr=1&x=41&y=6&sn=&rn=Madagascar&hci=-1&ei=-1&lang=EN';
    madagascarHTML = fetchWebpage(madagascarURL);
    locationData = scrapeLocaleData(madagascarHTML, 58);
    organismTypeAnalysis(locationData);
    #nativeAnalysis(locationData);
    locationData = topHundred(locationData);
    return locationData;
def topHundred(locationData):
    topURL = "http://www.issg.org/database/species/search.asp?st=100ss&fr=1&str=&lang=EN"
    topHTML = fetchWebpage(topURL);
    topData = scrapeLocaleData(topHTML, 100);
    locationData["top"] = locationData["name"].apply(lambda x : any(topData.name == x));
    locationData["name"][locationData["top"]].to_csv("worstInvasivesMadagascar.csv") 
    propPlotData = pd.DataFrame(locationData["top"].value_counts());
    plt.figure(figsize=figsize)    
    sns.barplot(data=propPlotData, x=propPlotData.index, y=0)
    plt.ylabel("\nNumber of Species\n", fontsize=25)
    plt.xlabel("In The Top 100 List?\n", fontsize=25)
    plt.title("\nNumber of Madagascar Invasives in the Top 100 Worst Invasives List\n", fontsize=40)
    plt.tick_params(labelsize=28)
    plt.tight_layout()
    plt.savefig("figures/topProp.png")
    plt.close()
    return locationData
def nativeAnalysis(data):
    global nativeobs;
    global nativeframe;
    global nativect;
    global nativesper;
    nativeobs = [];
    nativesper = []; #How many Native Countries Per Species
    nativeframe = pd.DataFrame();
    data["natives"] = data["distlinks"].apply(findNativeRange);
    for natives in data["natives"]:
        nativeobs = nativeobs + natives;
        nativesper.append(len(natives));
    nativeframe = pd.DataFrame(nativeobs);
    nativect = nativeframe[0].value_counts();
    nativectframe = pd.DataFrame(nativect);#pd.DataFrame({"country": nativect.index, "counts": nativect});
    cleanNativeGIS(nativectframe);
    plotct = nativect[0:25];
    plt.figure(figsize=figsize)
    sns.barplot(y=plotct.index, x=plotct, palette=pal)
    plt.ylabel("\nNative Range\n", fontsize=25)
    plt.xlabel("# of Invasive Species\n", fontsize=25)
    plt.title("\nDistribution of Madagascar Invasive Species Origins\n", fontsize=40)
    plt.tick_params(labelsize=28)
    plt.tight_layout()
    plt.savefig("figures/invasiveorigins.png")
    plt.close()
    return nativect;
def cleanNativeGIS(nativectframe):
    nativectframe["name"] = nativectframe.index;
    nativectframe.loc[nativectframe["name"].isin(["United States (USA)"]), "name"] = "United States"
    pd.DataFrame(nativectframe).to_csv("gis/nativeranges.csv");
def findNativeRange(disturl):
    try:
        distHTML = fetchWebpage(urlprefix+disturl);
        soup = BeautifulSoup(distHTML, 'html.parser');
        nativelist = soup.find_all('a', href=re.compile("Native"))
        nativeloc = [];
        for native in nativelist:
            nativeloc.append(native.span.string)
        print(str(nativeloc))
        return nativeloc
    except:
        return -1
def fetchWebpage(dataurl):
    #Get webpage html data
    http = urllib3.PoolManager()
    res = http.request('GET', dataurl)
    rawhtml = res.data.decode('utf-8')
    return rawhtml;
def scrapeLocaleData(rawhtml, nrows):
    #Load up beautiful soup
    soup = BeautifulSoup(rawhtml, 'html.parser')
    #Fetch Species Names
    namesdom = soup.find_all("span", class_="ListTitle")
    names = []
    links = []
    for row in namesdom:
        try:
            names.append(row.i.get_text());
            links.append(row.a["href"])
        except:
            pass;
    #Fetch organism type data
    taxadom = soup.find_all("span", class_="Info")
    taxa = []
    for row in taxadom:
        taxa.append(row.get_text());
    taxa = [row for row in taxa if row[0]==" "]
    #Organism Type Analysis
    data = pd.DataFrame({"name": names, "taxa": taxa, "ecolink": links})
    data = data.iloc[0:nrows,:] #Selects only the invasive species
    #data = data.iloc[0:5,:]
    #Cleaning
    data["taxa"] = data["taxa"].apply(lambda st : st.strip().replace(")", "").replace("(", ""));
    data["distlinks"] = data["ecolink"].apply(lambda st : st.replace("ecology.asp", "distribution.asp"))
    return data;
def organismTypeAnalysis(data):
    #Plotting Organism Types
    groupct = data["taxa"].value_counts();
    plt.figure(figsize=figsize)
    sns.barplot(y=groupct.index, x=groupct, palette=pal)
    plt.ylabel("\nOrganism Type", fontsize=25)
    plt.xlabel("# of Invasive Species\n", fontsize=25)
    plt.title("\nDistribution of Various Invasive Species Types\n", fontsize=40)
    plt.tick_params(labelsize=28)
    plt.tight_layout()
    plt.savefig("figures/speciestypes.png")
    plt.close()
data = runAnalysis();