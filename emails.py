#! /usr/bin/env python3

import smtplib
import mimetypes
import email.message
import os.path


def generate_email(sender, receiver, subject, body, attachment_path=""):
    message = email.message.EmailMessage()  # Generating an instance for the message
    message["From"] = sender    # Defining the email address that will send the message
    message["To"] = receiver    # Defining the email address that will receive the message
    message["Subject"] = subject    # The title of the message, which will be the subject of the email.
    message.set_content(body)   # Adding the content of the message, the body of the email.

    if os.path.isfile(attachment_path):     # Checking if a file attachment was provided, if not, the message will be
        # sent without any attachments.
        attachment_file = os.path.basename(attachment_path)    # Storing the name of the file withing the provided
        # directory.
        mime_type, _ = mimetypes.guess_type(attachment_path)    # Retrieving the format of the file.
        mime_type, mime_subtype = mime_type.split("/")  # Storing the file type and the subtype.
        with open(attachment_path, 'rb') as ap:    # Opening the file as Binary for reading
            message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_file)
            # Converting the contents of the attachment to a binary, so it can be transmitted through the SMTP service,
            # and attaching to the message to be sent.

    return message  # The function will return a complete message ready to be sent to through SMTP.


def send_email(message, host):
    email_server = smtplib.SMTP(host)   # Establishing SMTP connection to the given host.
    email_server.send_message(message)  # Sending the message to through the connection.
    email_server.quit()    # Ending the connection.
