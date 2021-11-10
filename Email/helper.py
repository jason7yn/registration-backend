from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail,Attachment,FileContent, FileName, FileType, Disposition)
import os
from django.conf import settings
import base64
import json


def email_registration_detail(data,files):
    questions = json.loads(data.get('questions'))
    attachments=[]
    hasAttachments = json.loads(data.get('hasAttachments'))
    if hasAttachments:
        for f in files.getlist("files"):
            with f.open('rb') as uploaded_file:
                encodedFile = base64.b64encode(uploaded_file.read()).decode()
                attachedFile = Attachment(
                FileContent(encodedFile),
                FileName(f.name),
                FileType(f.content_type),
                Disposition('attachment'))
                attachments.append(attachedFile)


    templateId = 'd-36681768329f4a3ab973f25013d23bb0'
    message = Mail(
        from_email='jasonqi1993@gmail.com',
        to_emails='support@pursuittechnology.com.au',
        subject='Registration Request',
        html_content='<strong>You got new registration request</strong>'
        )
    message.dynamic_template_data = {
    'questions':questions,
    }
    message.attachment = attachments
    message.template_id = templateId
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return {'msg':'success','status':str(response.status_code)}
    except Exception as e:
        raise AttributeError("Error: {0}".format(e))