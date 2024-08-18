from speech import recognize_speech, speak
from google_news import google_news_search, parse_google_news_results
from web_browser import open_browser
from bs4 import BeautifulSoup
from open_apps import open_notepad

def main():
    print("Hello! How can I assist you today?")
    speak("Hello! How can I assist you today?")
    
    loop_count = 0
    
    while True:
        input_text = recognize_speech()
        loop_count += 1  

        if input_text:
            speak(f"You said: {input_text}")

        if input_text.lower() == "stop":
            speak(f"Goodbye! You have interacted {loop_count} times.")
            break

        elif input_text.lower() == "open notepad":
            message = open_notepad()
            speak(message)
        
        elif  input_text.lower().__contains__("news"):
            query = input_text   #query
            if query.strip() == "":
                speak("Please provide a news query.")
                continue
            
            html = google_news_search(query)
            search_results = parse_google_news_results(html)
            open_browser(query + "&tbm=nws")

            print("\nNews Search Results:")
            speak("Here are the news results I found.")
            
            for result in search_results:
                print(f"Title: {result['title']}")
                print(f"Link: {result['link']}")
                print(f"Source: {result['source']}")
                print()
                speak(result['title'])
                speak("From " + result['source'])
        
        elif input_text.strip() != "":
            open_browser(input_text)
        
        print(f"Loop count: {loop_count}")

if __name__ == "__main__":
    main()
