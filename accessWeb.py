import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
 

url = input('Enter url-')
count = input('Enter count-')
position = input('Enter position-')
for i in range(int(count)):

    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')

    tags = soup.find_all('a')
    print(tags[int(position)-1])
    url = tags[int(position)-1]['href']
    print(url)




    
    


