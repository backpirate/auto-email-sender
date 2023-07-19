import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, recipient_emails, cv_path):
    try:
        # Create message container
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = ", ".join(recipient_emails)
        message['Subject'] = 'Job Application'

        # Email body
        body = '''
       '''
        message.attach(MIMEText(body, 'plain'))

        # Attach CV
        cv_filename = cv_path.split('/')[-1]  # Extract filename from path
        with open(cv_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {cv_filename}")
            message.attach(part)

        # Connect and send email with SSL encryption
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_emails, message.as_string())
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def get_recipient_emails():
    recipient_type = input("Enter 's' to send email to a single recipient or 'm' to send to multiple recipients: ")

    if recipient_type == 's':
        # Prompt the user to enter the recipient's email address
        recipient_email = input("Enter the recipient's email address: ")
        return [recipient_email]
    elif recipient_type == 'm':
        # Prompt the user to enter multiple recipient email addresses separated by commas
        recipient_emails = input("Enter multiple recipient email addresses separated by commas: ").split(',')
        return [email.strip() for email in recipient_emails]
    else:
        print("Invalid input. Please try again.")
        return []

if __name__ == "__main__":
    
    sender_email = 'random_email'
    sender_password = 'random_password'

   
    recipient_emails = get_recipient_emails()

    if recipient_emails:
        
        cv_path = 'path'

        # Send the email
        send_email(sender_email, sender_password, recipient_emails, cv_path)
