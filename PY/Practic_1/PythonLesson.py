# C = float(input("temperature in Chuy: "))
# N = float(input("temperature in Naryn: "))
# I = float(input("temperature in Issyk-Kul: "))
# B = float(input("temperature in Batken: "))
# O = float(input("temperature in Osh: "))
# D = float(input("temperature in Djalal_adad: "))
# T = float(input("temperature in Talas: "))
#
# middle_temperature=(C + N +I +B + O + D +T)/7
# print(f"Middle temperature is {round(middle_temperature, 1)}")

import requests
appid = "e79dbe05c50393c9d818a4047cb4d1fb"
sum = 0

def get_city_id(s_city_name):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city_name, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()

        city_id = data['list'][0]['id']

    except Exception as e:
        print("Exception (find):", e)
        pass
    assert isinstance(city_id, int)
    return city_id

City_name = input('City name: ')
city_id = get_city_id(City_name)

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("temp:", data['main']['temp'])

except Exception as e:
    print("Exception (weather):", e)
    pass



Regions = ['Talas', 'Bishkek', 'Cholpon-Ata', 'Naryn', 'Osh', 'Batken', 'Zhalal-Abad']
print('''List of available cities in Kyrgyzstan: 
Talas, Bishkek, Cholpon-Ata, Naryn, Osh, Batken, Zhalal-Abad ''')

for i in Regions:
    def get_city_id(s_city_name):
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/find",
                               params={'q': s_city_name, 'type': 'like', 'units': 'metric', 'lang': 'ru',
                                       'APPID': appid})
            data = res.json()

            city_id = data['list'][0]['id']

        except Exception as e:
            print("Exception (find):", e)
            pass
        assert isinstance(city_id, int)
        return city_id

    City_name = i
    city_id = get_city_id(City_name)


    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                        params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    temp = data['main']['temp']
    sum = sum + temp




print(sum)