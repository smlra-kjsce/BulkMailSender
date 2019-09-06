import smtplib, ssl,csv

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "abc@gmail.com"  # Enter your address
#receiver_email = "xyz@gmail.com"  # Enter receiver address if 1-to-1 communication
password = input("Type your password and press enter: ")
message = """\
Subject: Enter your subject here!

Hi {name},
	This mail is sent using Python.
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	server.login(sender_email, password)
	with open("qwerty.csv") as mail_list: #This example is for CSV received from Google Form
		reader = csv.reader(mail_list)
		next(reader)  # Skip header row
		for L in reader:
			print(f"Sending email to {L[2]}, email: {L[1]}")
			server.sendmail(sender_email, L[1], message.format(name=L[2]))
	
