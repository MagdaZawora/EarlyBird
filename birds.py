import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

def get_observations(url):
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    response = ET.fromstring(data)

    lst = response.findall('result/sighting')
    print('Sighting count', len(lst), ':')

    birds_lst = []
    for item in lst:
        common_name = item.find('com-name').text
        # birds.append(common_name)
        scientific_name = item.find('sci-name').text
        # quantity = item.find('how-many').text
        observed = item.find('obs-dt').text
        birds_lst.append(common_name)
        # print('Common name:', common_name)
        # print('Scientific name:', scientific_name)
        # print('Observed:', observed)
        # print('Quantity:', quantity, '\n')
    observations = ', '.join(birds_lst) + '.'
    print(observations, '\n')
    return observations

# print(get_observations(
    # 'http://ebird.org/ws1.1/data/obs/hotspot/recent?r=L99381&back=5&maxResults=500&detail=simple&locale=en_US&fmt=xml'))

def check_must_have(observations, must_have):
    must_have_lst = []
    for bird in must_have:
        if bird in observations:
            must_have_lst.append(bird)
        return must_have_lst


# print(check_must_have(get_observations(
    # 'http://ebird.org/ws1.1/data/obs/hotspot/recent?r=L99381&back=5&maxResults=500&detail=simple&locale=en_US&fmt=xml'),
    # ['Redhead', 'Sparrow']))

'''

must_have_info = 'Please notice that among them ' + str(
                len(common_lst)) + ' from our "must-have" list: ' + ','.join(common_lst) + '!'
        else:
            must_have_info = 'This time none from our "must-have" list, but still worth watching!'
'''

def get_hotspots(self):
    url = 'http://ebird.org/ws1.1/ref/hotspot/region?rtype=country&r=PL&fmt=xml'

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    response = ET.fromstring(data)

    lst = response.findall('result/location')
    print('Location count:', len(lst), '\n')

    for item in lst:
        location_id = item.find('loc-id').text
        longitude = item.find('lng').text
        latitude = item.find('lat').text
        subnational_code = item.find('subnational1-code').text
        location_name = item.find('loc-name').text
        print('Location ID:', location_id)
        print('Longitude:', longitude)
        print('Latitude:', latitude)
        print('Subnational code:', subnational_code)
        print('Location name:', location_name, '\n')

# get_hotspots()
