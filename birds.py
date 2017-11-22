import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = 'http://ebird.org/ws1.1/data/obs/hotspot/recent?r=L99381&r=L104031&back=5&maxResults=500&detail=simple&locale=en_US&fmt=xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
response = ET.fromstring(data)

lst = response.findall('result/sighting')
print('Sighting count:', len(lst), '\n')

for item in lst:
    print('Common name:', item.find('com-name').text)
    print('Scientific name:', item.find('sci-name').text)
    print('Quantity:', item.find('how-many').text)
    print('Observed:', item.find('obs-dt').text, '\n')