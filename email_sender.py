import smtplib, ssl

gmail_username = ''
gmail_password = ''


server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.ehlo()
server.login(gmail_username, gmail_password)


def send_mail(message):
    message["Subject"] = "CPU Report"
    message["From"] = gmail_username
    message["To"] = gmail_username
    server.sendmail(gmail_username, gmail_username, message.as_string())
