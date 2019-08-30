import smtplib
import email.message
from datetime import datetime

To = ['email_receiver@mail.com']

def date_generator():
    now = datetime.now()
    date = now.strftime("%d%m%Y")
    hour = now.strftime("%H%M%S")
    d = str(date+'_'+hour)
    return d

def send_email_net():
    date_str = date_generator()

    # This example uses the day of execution. You can change it, or create a schedulated .bat to check if the current day is equal to a number, to send the email.
    days = input('Which days would you like to send the email?' )
    days_list = days.split(",")
    
    try:

        msg = email.message.Message()

        for day in days_list:
            if int(day) == int(date_str[0:2]):
                email_content = """
                <html>
                    <head>Title 1</head>
                    <p>Content 1</p>
                </html>
                """
                msg['Subject'] = 'Enter Subject'

            #insert user passoword and email, respectively in password and msg['From]
            password = "Your_Password"
            msg['From'] = "your_email@mail.com"
            msg['To'] = ', '.join(To)
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(email_content)

            s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            s.login(msg['From'], password)
            s.sendmail(msg['From'],To, msg.as_string())
            s.close()
            print ("successfully sent email to %s:" % (msg['To']))
    except Exception as e:
        print('Process send_email ERROR!\n{0}'.format(e)) 

send_email_net()
