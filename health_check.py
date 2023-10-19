#! /usr/bin/env python3

import socket
import psutil
from emails import generate_email, send_email
import os


def health_checks(host):
    errors = []

    if psutil.cpu_percent(15) > 80.00:  # Checking for CPU load, if the load is above 80%, the error will be triggered.
        errors.append("Error - CPU usage is over 80%")

    if psutil.disk_usage(os.getcwd()).percent > 80.00:  # Checking for the available disk space, if the used disk space
        # is above 80%, it means that the free disk space is less than 20%, therefore the error will be triggered
        errors.append("Error - Available disk space is less than 20%")

    if psutil.disk_usage(os.getcwd()).free//(10**6) < 500:  # Checking for free memory on the disk, if the free memory
        # is less than 500MB, the error will be triggered.
        errors.append("Error - Available memory is less than 500MB")

    if socket.gethostbyname(f"{host}") != "127.0.0.1":  # Checking if the hostname resolves on "127.0.0.1", if not the
        # error will be triggered.
        errors.append("Error - localhost cannot be resolved to 127.0.0.1")

    return errors


def main():
    host = "192.168.0.1"    # This is the server host, this host will be used to check if it's resolved on '127.0.0.1'.
    email_host = "localhost"    # The email SMTP host.
    errors = health_checks(host)    # Executing the checks.
    message_sender = "sender@example.com"   # The address from which the message will  be sent from.
    message_receiver = "receiver@example.com"    # The address from which the message will be sent to.
    message_body = "Please check your system and resolve the issue as soon as possible."    # The body of the email.

    if errors:  # Checking if errors occurred.
        for error in errors:    # If the errors occurred, the message returned by the error will be used as the subject
            # of the email.
            message = generate_email(message_sender, message_receiver, error, message_body)    # Generating the message
            # to be transmitted over SMTP.
            send_email(message, email_host)    # Sending the message over SMTP connection.


if __name__ == "__main__":
    main()
