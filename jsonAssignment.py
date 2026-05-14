import json
import urllib.request


url = input('Enter location: ')
uh = urllib.request.urlopen(url)
data = json.loads(uh.read())

sum = 0

for item in data['comments']:
    
    sum += int(item['count'])

print(sum)