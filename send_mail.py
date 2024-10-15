import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from speech import speak,recognize_speech


def send_email():
    from_email = "wizmuser@gmail.com"
    password = "udna lymb fcki qflf"

    speak("Whom should i send this?")
    to_email = recognize_speech()
    to_email = to_email.lower().strip().replace(" at the rate ","@").replace(" ","")

    print(to_email)

    speak("Can you tell me the Subject")
    subject = recognize_speech()


    speak("Pleae provide the messge: ")
    message = recognize_speech()

    # message = f"<p>{message}</p>"

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["subject"] = subject
    

    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f"Email successfully sent to {to_email}")
        speak(f"Email successfully sent to {to_email}")
    except smtplib.SMTPException as e:
        print("Error!! Unable to send mail")
        print(e)


# body = "Hello,\n\nKuch bannana hai ki \nBro"
# send_email("Happy Birthday",body,"wizardparam@gmail.com")

send_email()



