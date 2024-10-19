import requests
from bs4 import BeautifulSoup
from speech import speak


def weather(city):
    city = city.replace(" ", "+")
    url = "https://www.google.com/search?q=" + "weather" + city

    # requests instance
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    # this contains time and sky description
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    # format the data
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    # particular list with required data
    # formatting the string
    temp = int(temp[:-2])

    speak("Temperature of " + city + f" is {temp} degree celcius at " + time + " and is " + sky)
    print("Temperature is", temp)
    # print("Time: ", time)
    # print("Sky Description: ", sky)
