

import smtplib
from email.mime.text import MIMEText

class Alerts:
    def __init__(self, smtp_server='smtp.example.com', port=587, sender_email='your_email@example.com', password='your_password'):
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.password = password

    def send_alert(self, recipient_email, subject, message):
        """Send an email alert."""
        try:
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = recipient_email

            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()
                server.login(self.sender_email, self.password)
                server.send_message(msg)
            return {'status': 'Email sent successfully'}
        except Exception as e:
            return {'error': str(e)}

