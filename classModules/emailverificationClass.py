import random
import smtplib as email_smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def generateOTP(otp_size = 6):
    final_otp = ''
    for i in range(otp_size):
        final_otp = final_otp + str(random.randint(0,9))
    return final_otp
    
def sendEmailVerificationRequest(sender="gadgetswave.sales@gmail.com",receiver="ankithmurgeplar07@gmail.com", custom_text="Hello, Your GadgetsWave OTP is ",subject=" GadgetsWave"):
    server = email_smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    google_app_password = "zxtngftfusvhxpkw"
    server.login(sender,google_app_password)
    cur_otp = generateOTP()
    message_body = custom_text +  cur_otp
    msg = MIMEMultipart()
    msg.attach(MIMEText(message_body, 'plain'))
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver
    server.sendmail(sender,receiver,msg.as_string())
    server.quit()
    return cur_otp

