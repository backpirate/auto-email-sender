import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, recipient_emails, cv_path):
    # Create message container
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ", ".join(recipient_emails)
    message['Subject'] = 'Job Application'

    # Email body
    body = '''
    Dear Hiring Manager,

    Please find attached my CV for the job application. Thank you for your consideration.

    Kind regards,
    Your Name
    '''
    message.attach(MIMEText(body, 'plain'))

    # Attach CV
    cv_filename = cv_path.split('/')[-1]  # Extract filename from path
    attachment = open(cv_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {cv_filename}")
    message.attach(part)

    # Connect and send email with SSL encryption
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_emails, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")

# Provide your email credentials
sender_email = 'random_email'
sender_password = 'random_password'

# Prompt the user to choose recipient type
recipient_type = input("Enter 's' to send email to a single recipient or 'm' to send to multiple recipients: ")

if recipient_type == 's':
    # Prompt the user to enter the recipient's email address
    recipient_email = input("Enter the recipient's email address: ")
    recipient_emails = [recipient_email]
elif recipient_type == 'm':
    # Prompt the user to enter multiple recipient email addresses separated by commas
    recipient_emails = input("Enter multiple recipient email addresses separated by commas: ").split(',')
else:
    print("Invalid input. Please try again.")
    exit()

# Provide the path to your CV
cv_path = 'path'

# Send the email
send_email(sender_email, sender_password, recipient_emails, cv_path)
