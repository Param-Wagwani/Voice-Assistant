import requests

from speech import recognize_speech, speak
from google_news import google_news_search, parse_google_news_results
from web_browser import open_browser
from chat import get_response
from chat_bot.model import NeuralNet

from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


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


def getnews(news_query):
    query = news_query
    if query.strip() == "":
        speak("Please provide a news query.")

    html = google_news_search(query)
    search_results = parse_google_news_results(html)
    open_browser(query + "&tbm=nws")

    print("\nNews Search Results:")
    speak("Here are the news results I found.")
    count = 0
    for result in search_results:
        if count < 3:
            print(f"Title: {result['title']}")
            print(f"Link: {result['link']}")
            print(f"Source: {result['source']}")
            print()
            speak(result['title'])
            speak("From " + result['source'])
            count += 1


# from open_apps import open_notepad

def main():
    print("Hello! How can I assist you today?")
    speak("Hello! How can I assist you today?")

    loop_count = 0

    while True:
        input_text = recognize_speech()

        loop_count += 1
        ans = get_response(input_text)
        if input_text:
            speak(f"You said: {input_text}")

        if input_text.lower() == "exit":
            speak(f"Goodbye! You have interacted {loop_count} times.")
            break
        elif ans == "news":
            speak("Please provide the topic to be searched")
            news_query = recognize_speech()
            while news_query == "":
                news_query = recognize_speech()
            getnews(news_query)
        elif ans == "tech_news":
            getnews("tech news")
        elif ans == "weather":
            weather("mumbai")
        elif ans == "exit":
            speak("See you next time")
            break
        # elif input_text.lower() == "open notepad":
        #     message = open_notepad()
        #     speak(message)

        # elif input_text.lower().__contains__("news"):
        # #     query = input_text  # query
        # #     if query.strip() == "":
        # #         speak("Please provide a news query.")
        # #         continue
        # #
        # #     html = google_news_search(query)
        # #     search_results = parse_google_news_results(html)
        # #     open_browser(query + "&tbm=nws")
        # #
        # #     print("\nNews Search Results:")
        # #     speak("Here are the news results I found.")
        # #
        # #     for result in search_results:
        # #         print(f"Title: {result['title']}")
        # #         print(f"Link: {result['link']}")
        # #         print(f"Source: {result['source']}")
        # #         print()
        # #         speak(result['title'])
        # #         speak("From " + result['source'])
        # #
        # # elif input_text.strip() != "":
        # #     open_browser(input_text)

        print(f"Loop count: {loop_count}")


if __name__ == "__main__":
    main()
