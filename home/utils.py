from django.core.mail import send_mail , EmailMessage
from django.conf import settings 





def Send_email_to_client():

    subject = "this email is from django server"
    message = "this is a test massage from django server"
    from_email = settings.EMAIL_HOST_USER 
    recipient_list = ["graphicsprinting123@gmail.com"]

    send_mail(subject,message,from_email,recipient_list)


def Send_email_with_attachment(subject,message,recipient_list,file_path):


    mail = EmailMessage(
        subject= subject,
        body= message,
        from_email = settings.EMAIL_HOST_USER,
        to= recipient_list 
    )
    mail.attach_file(file_path)
    mail.send(Send_email_with_attachment)

