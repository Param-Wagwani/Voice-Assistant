import requests

from speech import recognize_speech, speak
from google_news import google_news_search, parse_google_news_results
from web_browser import open_browser
from chat import get_response
from model import NeuralNet
from open_apps import open_notepad,open_vscode,execute_command
from search_dir import find_directory, find_directory_name,find_file,find_file_name
from git_commands import initialize_git_repo,add_files,find_commit_message,commit_changes
from create_project import create_vite_project
from run_code import compile_and_run_js_code,compile_and_run_py_code

from pdf_reader import extract_abstract

from whatsapp import send_whatsapp_message

from send_mail import send_email


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

    git_dir = ''

    loop_count = 0

    while True:
        input_text = recognize_speech()
        loop_count += 1
        ans = get_response(input_text)
        # print("Ans: ",ans)
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
        elif ans == "open_notepad":
            message = open_notepad()
            speak(message)
        elif  "vs code" in input_text:
            directory_name = find_directory_name(input_text)
            if directory_name is not None:
                print(directory_name)
                directory_path = find_directory(directory_name,r"C:\Users\calgu\OneDrive\Desktop")
                message = open_vscode(directory_path)
            else:
                message = open_vscode(None)    
            speak(message)
            input_text = ''

        elif ans=="git":
            directory_name = find_directory_name(input_text)
            if directory_name is not None:
                print(directory_name)
                directory_path = find_directory(directory_name,r"C:\Users\calgu\OneDrive\Desktop")
                message = initialize_git_repo(directory_path)
                git_dir = directory_path
            else:
                message = "Properly specify the folder for initalization"    
            speak(message)
            input_text = ''

        elif "staging area" in input_text.lower():
            print(git_dir)
            add_files(git_dir)
            speak("Added all files to staging area")

        elif "commit" in input_text.lower():
            message = find_commit_message(input_text)
            git_dir = r"C:\Users\calgu\OneDrive\Desktop\test"
            print(message)
            commit_changes(git_dir,message)
            speak(f"commited changes to {git_dir} with message {message}" )

        elif ans == "react_project":
            directory_name = find_directory_name(input_text)
            
            if directory_name is not None:
                print(directory_name)
                directory_path = find_directory(directory_name,r"C:\Users\calgu\OneDrive\Desktop")
                print(directory_path)
                message = create_vite_project(directory_path)
            else:
                message = "Properly specify the folder for creation"    
            speak(message)
            input_text = ''

        elif "execute" in input_text.lower():
            file_name = find_file_name(input_text)
            
            if file_name is not None:
                print(file_name)
                file_path = find_file(file_name,r"C:\Users\calgu\OneDrive\Desktop")
                print("file_path : ",file_path)
                if "js" in file_name:
                    compile_and_run_js_code(file_path)
                if "py" in file_name:
                    compile_and_run_py_code(file_path)

            else:
                message = "Properly specify the file for execution" 
                speak(message)
                input_text = ''

        elif "open" in input_text.lower():
            execute_command(input_text)

        elif "read" in input_text.lower():
            print("Enter file Name: ")
            speak("Enter File name")
            pdf_path = recognize_speech()
            pdf_path = pdf_path.replace(" ","_") + ".pdf"
            format, abstract = extract_abstract(pdf_path)
            print(f"Paper format: {format}")
            print(f"Abstract:\n{abstract}")
            speak(f"Abstract:\n{abstract}")

        elif "send message" in input_text:
            print("To whom you want to send: ")
            speak("To whom do you want to send: ")
            record = recognize_speech()
            record = record.replace(" ","").lower()
            print('Enter the message: ')
            speak("Enter message: ")
            message = recognize_speech()
            send_whatsapp_message(record,message)

        elif "mail" in input_text:
            send_email()
            



        



            


    




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
