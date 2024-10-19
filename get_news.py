from speech import speak
from google_news import google_news_search, parse_google_news_results
from web_browser import open_browser


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
