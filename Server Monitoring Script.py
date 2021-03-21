# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

clusterList = ['127.0.0.1'

               ]
s = ''
s=s+"-------------------------------------------------------------------------------------------------------------"+'\n'

for ip in clusterList:
    try:

        url = 'http://'+ip+':81/serverStatistics.pl'
        response = requests.get(url,verify=False, timeout=2)
        soup = BeautifulSoup(response.text, 'html.parser')
        for heading in soup.find_all(["h1"]):
            s= s + ' ' + heading.text.replace('(Cluster TestCluster01)','').strip() + '\n'
        count=1    
        for heading in soup.find_all(["a"]):
            if count == 3:
                s = s + ' ' +'DB - '+ heading.text + '\n'     
            if(heading.text == "User (https) login"):
                s= s + ' ' + 'App - '+heading['href'].replace('.serverdetails.com','')+'\n'
            if(heading.text == "Internal (hosting) login"):
                s= s + ' ' + 'Internal - '+ heading['href'].replace('.serverdetails.com','') +'\n'
            
            count = count +1
    except requests.exceptions.Timeout:
        s= s + ' ' + ip +' Time out \n'   
               
    s=s+"-------------------------------------------------------------------------------------------------------------"+'\n'

print(s)    

