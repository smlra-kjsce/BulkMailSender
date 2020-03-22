import smtplib, ssl,csv
from getpass import getpass

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
		for L in reader:
			print(f"Sending email to {L[2]}, email: {L[1]}") #values wrt a particular CSV
			server.sendmail(sender_email, L[1], message.format(name=L[2].split()[0]))
	
