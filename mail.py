import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:

    mail_host = "smtp.gmail.com"
    mail_port = 587
    user = 'email-destino@gmail.com'
    password = 'opnreuqqaouvthiy'
    sender = "alguem@gmail.com"

    @classmethod
    def send_mail(cls, to: str, body: str):
        smtp = None
        try:

            msg = MIMEMultipart()
            msg['From'] = cls.sender
            msg['To'] = to
            msg['Subject'] = "Test"

            text = MIMEText(body, 'html', 'utf-8')
            msg.attach(text)

            smtp = smtplib.SMTP(cls.mail_host, 25)
            smtp.connect(cls.mail_host, cls.mail_port)
            smtp.starttls()
            smtp.login(cls.user, cls.password)
            smtp.sendmail(cls.sender, to.split(','), msg.as_string().encode('utf-8'))
            smtp.quit()

        except Exception as e:
            print('DEU RUIM ' + str(e))
        finally:
            if smtp:
                smtp.close()


if __name__ == '__main__':
    Email.send_mail('email-destino@gmail.com', 'CHEGOU?')
