import smtplib, ssl,csv
from getpass import getpass
from time import time

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "abc@gmail.com"  # Enter your address
#receiver_email = "xyz@gmail.com"  # Enter receiver address if 1-to-1 communication
password = getpass("Type your password and press enter: ")
filename= input("Enter exact filename with extension of the CSV file: ") #make sure the file is in the same directory as this script
message = """\
Subject: Enter your subject here!

Hi {name},
    This mail is sent using Python.
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    with open(filename) as mail_list:
        reader = csv.reader(mail_list)

        next(reader)  # Skip header row

        #If you want to resume sending from row X of CSV, due to SMTPConnection Refusal, 
        #uncomment the lines below:

        #for i in range(X-1): # -1 compensates for the header that has been skipped
        #	next(reader)
        

        for i,L in enumerate(reader):
            if i%50 == 0:
                time.sleep(2.5) #pause for 2.5 seconds to avoid connection refused error

            print(f"Sending email to {L[2]}, email: {L[1]}") #values wrt a particular CSV
            server.sendmail(sender_email, L[1], message.format(name=L[2].split()[0]))
            time.sleep(0.25) #pause for 0.25 seconds to avoid connection refused error