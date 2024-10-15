import pywhatkit
from datetime import datetime, timedelta
from speech import speak

str_time = int(datetime.now().strftime('%H'))

update = (datetime.now() + timedelta(minutes=2)).minute

def send_message():
   #  speak('Enter the number you want to send the message to')
    number = input('Enter the number: ')
   #  speak('Enter the message you want to send')
    message = input('Enter the message: ')
   #  speak('Sending the message in 2 minutes')
    pywhatkit.sendwhatmsg(number, message, time_hour=str_time, time_min=update)

send_message()

