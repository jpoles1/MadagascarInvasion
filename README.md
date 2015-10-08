# MadagascarInvasion
###An analysis of the invasive species resident in madagascar using the <a target="_blank" href="http://www.issg.org/database/welcome/">Global Invasive Species Database (GISD)</a>
1. Currently scraping data from the GISD using urllib3 for fetching, and BeautifulSoup for parsing.
2. Data is then cleaned and ordanized using pandas.
3. Data is plotted using matplotlib and Seaborn
4. 

###Initial Analysis of Types of Invsasive Species
Data was extracted from the GISD Madagascar search results: <a target="_blank" href="http://www.issg.org/database/species/search.asp?sts=sss&st=sss&fr=1&x=41&y=6&sn=&rn=Madagascar&hci=-1&ei=-1&lang=EN"><img src="https://github.com/jpoles1/MadagascarInvasion/raw/master/figures/madagascarsearch.png"></img></a>
- Processed using BeautifulSoup to extract the names of species and their organism type.
- Plotted using Seaborn

<img src="https://github.com/jpoles1/MadagascarInvasion/raw/master/figures/speciestypes.png"></img>

###Analysis of invasive species origins
Data was extracted from individual species pages:
<a target="_blank" href="http://www.issg.org/database/species/distribution.asp?si=51&fr=1&sts=sss&lang=EN"><img src="https://github.com/jpoles1/MadagascarInvasion/raw/master/figures/native.png"></img></a>
<img src="https://github.com/jpoles1/MadagascarInvasion/raw/master/figures/invasiveorigins.png"></img>
<img src="https://github.com/jpoles1/MadagascarInvasion/raw/master/figures/nativeranges.png"></img>
