import pywhatkit
from datetime import datetime, timedelta
from speech import speak
import json

with open('contacts.json') as f:
    contacts_dict = json.load(f)

str_time = int(datetime.now().strftime('%H'))

update = (datetime.now() + timedelta(minutes=2)).minute

def send_message():
   #  speak('Enter the number you want to send the message to')
    number = input('Enter the number: ')
   #  speak('Enter the message you want to send')
    message = input('Enter the message: ')
   #  speak('Sending the message in 2 minutes')
    pywhatkit.sendwhatmsg(number, message, time_hour=str_time, time_min=update,tab_close=True)

def send_message_to_group():
    # group_id = input('Enter group Id: ')

    message = input('Enter the message: ')

    pywhatkit.sendwhatmsg_to_group("JDOLVbPaz9p3oXRXcvXJ4s",message,time_hour=str_time, time_min=update,tab_close=True)





# # send_message()
# send_message_to_group()


def send_whatsapp_message(record,message):
    if(not contacts_dict[record]["group"]):
        
        number = contacts_dict[record]["phone"]
        pywhatkit.sendwhatmsg(number, message, time_hour=str_time, time_min=update,tab_close=True)

    else:
         pywhatkit.sendwhatmsg_to_group(contacts_dict[record]['group_id'],message,time_hour=str_time, time_min=update,tab_close=True)





