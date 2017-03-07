import imaplib
import email
import email.header
import datetime


class Email(object):
    def __init__(self):
        self.connected = False
        self.mids = []
        self.mails = []

    def connect(self, username, password, host):
        self._mail = imaplib.IMAP4_SSL(host)
        self._mail.login(username, password)
        self._mail.select('inbox')
        result, data = self._mail.search(None, 'ALL')
        self.mids = data[0].split()
        self.connected = True

    def get_mail(self):
        n = 0
        while(n < 10):
            rv, data = self._mail.fetch(self.mids[n], '(RFC822)')
            n+=1
            msg = email.message_from_bytes(data[0][1])
            hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
            subject = str(hdr)
            date_tuple = email.utils.parsedate_tz(msg['Date'])
            date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple))
            body_str = ''
            if msg.is_multipart():
                for part in msg.get_payload():
                    body = part.get_payload()
                    if isinstance(body,str):
                        body_str += body
            else:
                body_str = msg.get_payload()

            self.mails.append({'Date':date, 'Subject':subject, 'Body':body_str})