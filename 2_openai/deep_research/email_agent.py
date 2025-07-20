import os
from typing import Dict

import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content, To
from agents import Agent, function_tool

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """ Send out an email with the given subject and HTML body """
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("jai.300012723027@csvtu.ac.in") # Change this to your verified email
    to_email = To("ksharma9719@gmail.com") # Change this to your email
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    response = sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}


INSTRUCTIONS = """
    You are able to send a nicely formatted HTML email based on a detailed report.
    You will be provided with detailed report. You should use your tool to send one email, 
    providing the report converted into clean, well presented HTML with an appropriate subject line.
"""

email_agent = Agent(
    name = "Email Agent",
    instructions = INSTRUCTIONS,
    model='gpt-4o-mini',
    tools=[send_email]
)