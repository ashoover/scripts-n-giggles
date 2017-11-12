import smtplib
import http.client, urllib
import urllib.request
import logging
import json


# Settings (later to be migrated to config.json)
receiver_email = 'test@domain.com'
sender_email = 'status_checker_thing@noreply.com'
url_to_check = 'https://httpstat.us/200'
extended_check = 'N'
extended_check_word = 'Error'
logging_type = 'info'
log_file_location = ''


# SMTP Settings
email_server = 'localhost:2557'
email_server_username = 'username'
email_server_password = 'password'

# Pushover Info
po_token: "Pushover APP_TOKEN"
po_user: "Pushover USER_KEY"


def url_status_check(url_to_check):
    url = url_to_check
    try:
        req = urllib.request.urlopen(url)
        usc = req.getcode()

    except urllib.error.URLError as e:
        url_response = e.reason + ' ' + 'HTTP Status Code : ' + str(e.code)
        usc = url_response

    return usc


def status_message():
    msg = "Alert Test"
    return msg


def send_dat_email():
    msg_header = 'From: Sender Name {s_email}\n'\
                 'To: Receiver Name {r_email}\n'\
                 'Cc: Receiver2 Name {r_email}\n'\
                 'MIME-Version: 1.0\n' \
                 'Content-type: text/html\n'\
                 'Subject: Any subject\n'.format(s_email=sender_email, r_email=receiver_email)
    title = 'Status Checker Thing Alert'
    msg_content = '<h2>{title} > <font color="green">OK</font></h2>\n'.format(title=title)
    msg_full = (''.join([msg_header, msg_content])).encode()

    server = smtplib.SMTP(email_server)
    # server.starttls()
    # server.login(email_server_username, email_server_password)
    server.sendmail('sender@server.com',
                    ['receiver@server.com', 'receiver@server.com'],
                    msg_full)
    server.quit()


def push_dat_notif():
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": po_token,
                     "user": po_user,
                     "message": status_message,
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()


print(url_status_check(url_to_check))
