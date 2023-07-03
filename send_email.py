import smtplib
import imghdr
from email.message import EmailMessage

pw = "YOUR GOOGLE APP PW"
sender_address = "AN EMAIL ADDRESS"
receiver_address = "AN EMAIL ADDRESS"

def send_mail(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New person showed up in your room"
    email_message.set_content("Hello. Someone just appeared in your room..")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image",
                                 subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender_address, pw)
    gmail.sendmail(sender_address, receiver_address, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_mail()
