from imports import *

def send_fail(receiver_address):
    mail_content_file = open('fail_body.txt')
    #this is the password of the email ID from which the email is sent. It is not provided here because it is one of our team member's personal email ID. Hence the mail won't work in this phase but works normally.
    sender_address = 'r5assistineducation@gmail.com'
    sender_pass = 'ConstantV'
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = "R5 Assist"
    message['To'] = receiver_address
    message['Subject'] = 'Information Summarization'
    # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content_file.read(), 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Fail Mail Sent')

def send_mail(zipfile_name, receiver_address):
    mail_content_file = open('mail_body.txt')
    #this is the password of the email ID from which the email is sent. It is not provided here because it is one of our team member's personal email ID. Hence the mail won't work in this phase but works normally.
    sender_address = 'r5assistineducation@gmail.com'
    sender_pass = 'ConstantV' 
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = "R5 Assist"
    message['To'] = receiver_address
    message['Subject'] = 'Information Summarization'
    # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content_file.read(), 'plain'))
    attach_file_name = f'{zipfile_name}'
    attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
    payload = MIMEBase('application', 'zip')
    payload.set_payload(attach_file.read())
    encoders.encode_base64(payload)  # encode the attachment

    payload.add_header('Content-Disposition', f'attachment; filename= {attach_file_name}')
    # add payload header with filename
    message.attach(payload)
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
