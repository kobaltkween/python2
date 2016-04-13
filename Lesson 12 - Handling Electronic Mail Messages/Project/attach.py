import os
import smtplib
import email
import datetime
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

SERVER = 'mail.oreillyschool.com'

def buildEmail(address, msgTxt, attachList = []):
    # Make a MIMEMultipart message
    msg = MIMEMultipart()
    msg['To'] = address
    msg['From'] = 'anybody@gmail.com'
    msg['Subject'] = 'Sending Email with Attachments'
    msg['Date'] = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S -0500")
    htmlMsg = MIMEText(msgTxt, 'html')
    msg.attach(htmlMsg)
    # If the list isn't empty
    # Code referenced from Python manual example
    if attachList:
        for apath in attachList:
            atype, encoding = mimetypes.guess_type(apath)
            # If type can't be guessed or file is compressed
            if atype is None or encoding is not None:
                atype = 'application/octet-stream'
            maintype, subtype = atype.split('/', 1)
            if maintype == 'text':
                with open(apath, 'r') as afile:
                    attach = MIMEText(afile.read(), _subtype = subtype)
            elif maintype == 'image':
                with open(apath, 'rb') as afile:
                    attach = MIMEImage(afile.read(), _subtype = subtype)
            elif maintype == 'audio':
                with open(apath, 'rb') as afile:
                    attach = MIMEAudio(afile.read(), _subtype = subtype)
            else:
                with open(apath, 'rb') as afile:
                    attach = MIMEBase(maintype, subtype)
                    attach.set_payload(afile.read())
                email.encoders.encode_base64(attach)
    
            # give the attachment a header
            attach.add_header('Content-Disposition', 'attachment', filename = os.path.basename(apath))
            # attach it to the main message
            msg.attach(attach)
    return msg

def sendEmail(msg):
    srvr = smtplib.SMTP('mail.oreillyschool.com', 25)
    srvr.sendmail(msg['From'], msg['To'], msg.as_string())
    srvr.quit()
