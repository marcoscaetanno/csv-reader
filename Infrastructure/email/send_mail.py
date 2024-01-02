import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..configurations.configurations import Settings

def get_settings():
    return Settings()

email_settings = get_settings()

class EmailSender:
    async def send_email(subject: str, receiver: str, email_body: str):
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = email_settings.sender_email
        message["To"] = receiver
        message.attach(MIMEText(email_body, "html"))
        
        try:
            with smtplib.SMTP(host=email_settings.smpt_server, port=email_settings.port) as server:
                server.connect(host=email_settings.smpt_server, port=email_settings.port)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(user=email_settings.sender_email, password=email_settings.password)
                server.helo()
                server.sendmail(from_addr=email_settings.sender_email, to_addrs=receiver, msg=message.as_string())
        except Exception as e:
            print(e)
        finally:
            server.close()    
    