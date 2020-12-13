#Description: Send emails using Python. Attaches a Subject, To, From, Images, Links, and paragraphs within a email.
# Adds HTML with Python
#SMTP - Simple Mail Transfer Protocol
import smtplib # allows the actual sending function
import ssl # Secure Sockets Layer - designed to create a secure connection between the client and server
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Multipurpose Internal Mail Extensions - Internet standard that extends the format of email messages to support text
# ,and other attachments
# Multipart - allows more than one attachment

sender_email = "sender's email" # define the sender's email
sender_password = "password of sender's email" # define the sender's password to allow access
receiver_email = "receiver's email" # define the receiver's email

email = MIMEMultipart() # allow more than one attachment within the email
email['Subject'] = "Anthony Amendolare's Github" # adds the 'Subject' of the email
email['From'] = sender_email # adds the 'From' of the email
email['To'] = receiver_email # adds the 'To' of the email

# HTML within Python
HTML = """
<html>
    <body>
        <h1>Want to learn Python?</h1>
        <img src = "https://everythingcomputerscience.com/Photos/Python_Image.png" alt ="Python Image width="640" height="360"" </img>
        <h2>
            <p> Hey, <br>
                Check out my GitHub account for python coding: <a href="https://github.com/anthonyamendolare00"> Click this link to check it out! </a>
                Let's get to coding!
            </p>
        </h2>
    </body>
</html>
"""

# make the MIMEText for the HTML code that is an object in Python
MTObj = MIMEText(HTML, "html")

# adds the MTObj into the email
email.attach(MTObj)

# create the SSL object
SSL_context = ssl.create_default_context()

# create the connection for the SMTP
server = smtplib.SMTP('smtp.gmail.com', 587) # port 587 - preferred port option for sending emails
server.starttls() #TLS - Transport Layer Security - connects to TLS mode
# logs into the sender's email
server.login(sender_email, sender_password)
# sends the email to the receiver with the email attached as a string in Python
server.sendmail(sender_email, receiver_email , email.as_string())
# the system quits/ exits out
server.quit()