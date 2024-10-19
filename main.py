import requests
from weather import weather
from speech import speak,recognize_speech
from google_news import google_news_search, parse_google_news_results
from web_browser import open_browser
from chat import get_response
from model import NeuralNet
from open_apps import open_notepad, open_vscode, execute_command
from search_dir import find_directory, find_directory_name, find_file, find_file_name
from git_commands import initialize_git_repo, add_files, find_commit_message, commit_changes
from create_project import create_vite_project
from run_code import compile_and_run_js_code, compile_and_run_py_code
from getnews import getnews
from pdf_reader import extract_abstract

from whatsapp import send_whatsapp_message

from send_mail import send_email

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}





def main():
    print("Hello! How can I assist you today?")
    speak("Hello! How can I assist you today?")

    loop_count = 0

    while True:
        input_text = get_input()
        loop_count += 1

        if not input_text:
            continue  # Skip if no input was detected

        process_response(input_text, loop_count)


def get_input():
    """Handles user input through speech recognition."""
    return recognize_speech()


def process_response(input_text, loop_count):
    """Processes the user input and responds accordingly."""
    ans = get_response(input_text)

    if ans == "exit":
        speak(f"Goodbye! You have interacted {loop_count} times.")
        quit()

    if ans == "news":
        handle_news()
    elif ans == "tech_news":
        getnews("tech news")
    elif ans == "weather":
        weather("delhi")
    elif ans == "open_notepad":
        speak(open_notepad())
    elif "vs code" in input_text:
        handle_vscode(input_text)
    elif ans == "git":
        handle_git(input_text)
    elif "staging area" in input_text.lower():
        handle_staging_area()
    elif "commit" in input_text.lower():
        handle_commit()
    elif ans == "react_project":
        handle_react_project(input_text)
    elif ans == "execute_program":
        handle_execution(input_text)
    elif "open" in input_text.lower():
        execute_command(input_text)
    elif ans == "read_pdf":
        handle_read()
    elif ans == "send_whatsapp":
        handle_send_message()
    elif ans == "send_email":
        send_email()

    print(f"Loop count: {loop_count}")


def handle_news():
    """Handles news query from the user."""
    speak("Please provide the topic to be searched")
    news_query = recognize_speech()
    while news_query == "":
        news_query = recognize_speech()
    getnews(news_query)


def handle_vscode(input_text):
    """Handles opening Visual Studio Code."""
    directory_name = find_directory_name(input_text)
    directory_path = find_directory(directory_name, r"C:\Users\calgu\OneDrive\Desktop") if directory_name else None
    message = open_vscode(directory_path)
    speak(message)


def handle_git(input_text):
    """Handles Git commands."""
    directory_name = find_directory_name(input_text)
    directory_path = find_directory(directory_name, r"C:\Users\calgu\OneDrive\Desktop") if directory_name else None
    message = initialize_git_repo(
        directory_path) if directory_path else "Properly specify the folder for initialization"
    speak(message)


def handle_staging_area():
    """Adds all files to the staging area."""
    speak("Enter git directory")
    git_dir=recognize_speech()
    add_files(git_dir)
    speak("Added all files to staging area")


def handle_commit():
    """Commits changes to the Git repository."""
    speak("Enter commit message ")
    input_text=recognize_speech()
    message = find_commit_message(input_text)
    git_dir = r"C:\Users\calgu\OneDrive\Desktop\test"
    commit_changes(git_dir, message)
    speak(f"Committed changes to {git_dir} with message {message}")


def handle_react_project(input_text):
    """Handles creating a React project."""
    directory_name = find_directory_name(input_text)
    directory_path = find_directory(directory_name, r"C:\Users\calgu\OneDrive\Desktop") if directory_name else None
    message = create_vite_project(directory_path) if directory_path else "Properly specify the folder for creation"
    speak(message)


def handle_execution(input_text):
    """Executes a specified file."""
    file_name = find_file_name(input_text)
    file_path = find_file(file_name, r"C:\Users\calgu\OneDrive\Desktop") if file_name else None

    if file_path:
        if "js" in file_name:
            compile_and_run_js_code(file_path)
        elif "py" in file_name:
            compile_and_run_py_code(file_path)
    else:
        speak("Properly specify the file for execution")


def handle_read():
    """Reads and extracts abstract from a PDF file."""
    speak("Enter File name")
    pdf_path = recognize_speech().replace(" ", "_") + ".pdf"
    format, abstract = extract_abstract(pdf_path)
    speak(f"Abstract:\n{abstract}")


def handle_send_message():
    """Handles sending a message via WhatsApp."""
    speak("To whom do you want to send: ")
    recipient = recognize_speech().replace(" ", "").lower()
    speak("Enter message: ")
    message = recognize_speech()
    send_whatsapp_message(recipient, message)


if __name__ == "__main__":
    main()


















#
# def main():
#     print("Hello! How can I assist you today?")
#     speak("Hello! How can I assist you today?")
#
#     git_dir = ''
#
#     loop_count = 0
#
#     while True:
#         input_text = recognize_speech()
#         loop_count += 1
#         ans = get_response(input_text)
#         # print("Ans: ",ans)
#         if input_text:
#             speak(f"You said: {input_text}")
#
#         if input_text.lower() == "exit":
#             speak(f"Goodbye! You have interacted {loop_count} times.")
#             break
#         elif ans == "news":
#             speak("Please provide the topic to be searched")
#             news_query = recognize_speech()
#             while news_query == "":
#                 news_query = recognize_speech()
#             getnews(news_query)
#         elif ans == "tech_news":
#             getnews("tech news")
#         elif ans == "weather":
#             weather("mumbai")
#         elif ans == "exit":
#             speak("See you next time")
#             break
#         elif ans == "open_notepad":
#             message = open_notepad()
#             speak(message)
#         elif "vs code" in input_text:
#             directory_name = find_directory_name(input_text)
#             if directory_name is not None:
#                 print(directory_name)
#                 directory_path = find_directory(directory_name, r"C:\Users\calgu\OneDrive\Desktop")
#                 message = open_vscode(directory_path)
#             else:
#                 message = open_vscode(None)
#             speak(message)
#             input_text = ''
#
#         elif ans == "git":
#             directory_name = find_directory_name(input_text)
#             if directory_name is not None:
#                 print(directory_name)
#                 directory_path = find_directory(directory_name, r"C:\Users\calgu\OneDrive\Desktop")
#                 message = initialize_git_repo(directory_path)
#                 git_dir = directory_path
#             else:
#                 message = "Properly specify the folder for initalization"
#             speak(message)
#             input_text = ''
#
#         elif "staging area" in input_text.lower():
#             print(git_dir)
#             add_files(git_dir)
#             speak("Added all files to staging area")
#
#         elif "commit" in input_text.lower():
#             message = find_commit_message(input_text)
#             git_dir = r"C:\Users\calgu\OneDrive\Desktop\test"
#             print(message)
#             commit_changes(git_dir, message)
#             speak(f"commited changes to {git_dir} with message {message}")
#
#         elif ans == "react_project":
#             directory_name = find_directory_name(input_text)
#
#             if directory_name is not None:
#                 print(directory_name)
#                 directory_path = find_directory(directory_name, r"C:\Users\calgu\OneDrive\Desktop")
#                 print(directory_path)
#                 message = create_vite_project(directory_path)
#             else:
#                 message = "Properly specify the folder for creation"
#             speak(message)
#             input_text = ''
#
#         elif "execute" in input_text.lower():
#             file_name = find_file_name(input_text)
#
#             if file_name is not None:
#                 print(file_name)
#                 file_path = find_file(file_name, r"C:\Users\calgu\OneDrive\Desktop")
#                 print("file_path : ", file_path)
#                 if "js" in file_name:
#                     compile_and_run_js_code(file_path)
#                 if "py" in file_name:
#                     compile_and_run_py_code(file_path)
#
#             else:
#                 message = "Properly specify the file for execution"
#                 speak(message)
#                 input_text = ''
#
#         elif "open" in input_text.lower():
#             execute_command(input_text)
#
#         elif "read" in input_text.lower():
#             print("Enter file Name: ")
#             speak("Enter File name")
#             pdf_path = recognize_speech()
#             pdf_path = pdf_path.replace(" ", "_") + ".pdf"
#             format, abstract = extract_abstract(pdf_path)
#             print(f"Paper format: {format}")
#             print(f"Abstract:\n{abstract}")
#             speak(f"Abstract:\n{abstract}")
#
#         elif "send message" in input_text:
#             print("To whom you want to send: ")
#             speak("To whom do you want to send: ")
#             record = recognize_speech()
#             record = record.replace(" ", "").lower()
#             print('Enter the message: ')
#             speak("Enter message: ")
#             message = recognize_speech()
#             send_whatsapp_message(record, message)
#
#         elif "mail" in input_text:
#             send_email()
#
#         print(f"Loop count: {loop_count}")
