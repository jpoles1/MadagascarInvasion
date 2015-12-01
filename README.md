# MadagascarInvasion - Reporting On The State of Chytrid In Madagascar
This repository contains the code I utilized in order to write a <a target="_blank" href="https://github.com/jpoles1/MadagascarInvasion/raw/master/ChytridReport.pdf">section of a report</a> to a conservation organization regarding an analysis of invasive species on Madagascar. I begin with an analysis of invasive species on Madagascar, before focusing in on Chytrid.
Chytrid was introduced to Madagascar very recently; evidence points to an introduction in the period from 2010-2014. It threatens the numerous amphibians endemic to Madagascar (>240 unique species of frog). 
###Analysis Process
1. Invasive species data scraped from the <a target="_blank" href="http://www.issg.org/database/welcome/">GISD</a> using urllib3 for fetching, and BeautifulSoup for parsing.
2. Madagascar amphibian data aquired from the <a target="_blank" href="http://amphibiaweb.org/ws_locality.html">AmphibiaWeb API</a>
2. Data was cleaned and ordanized using pandas.
3. Data was plotted using matplotlib and Seaborn.

###Initial Analysis of Types of Invsasive Species
Data was extracted from the GISD Madagascar search results:
<a target="_blank" href="http://www.issg.org/database/species/search.asp?sts=sss&st=sss&fr=1&x=41&y=6&sn=&rn=Madagascar&hci=-1&ei=-1&lang=EN"><img src="https://github.com/jpoles1/MadagascarInvasion/raw/master/figures/madagascarsearch.png"></img></a>

<img src="https://github.com/jpoles1/MadagascarInvasion/raw/master/figures/speciestypes.png"></img>

###Comparison with <a target="_blank" href="http://www.issg.org/database/species/search.asp?st=100ss&fr=1&str=&lang=EN">List of Top 100 Invasive Species</a>

#####<a target="_blank" href="https://github.com/jpoles1/MadagascarInvasion/blob/master/worstInvasivesMadagascar.csv">Resulting list of Top 100 Invasives present in Madagascar</a>

<img src="https://github.com/jpoles1/MadagascarInvasion/raw/master/figures/topProp.png"></img>

###Analysis of invasive species origins
Data was extracted from individual species pages:
<a target="_blank" href="http://www.issg.org/database/species/distribution.asp?si=51&fr=1&sts=sss&lang=EN"><img src="https://github.com/jpoles1/MadagascarInvasion/raw/master/figures/native.png"></img></a>
<img src="https://github.com/jpoles1/MadagascarInvasion/raw/master/figures/invasiveorigins.png"></img>
<img src="https://github.com/jpoles1/MadagascarInvasion/raw/master/figures/nativeranges.png"></img>

#Amphibian Risk Analysis
Data was extracted from amphibiaweb.org
<img src="https://github.com/jpoles1/MadagascarInvasion/raw/master/figures/frogIUCN.png"></img>
<img src="https://github.com/jpoles1/MadagascarInvasion/raw/master/figures/frogFamily.png"></img>
<img src="https://github.com/jpoles1/MadagascarInvasion/raw/master/figures/frogGenus.png"></img>

