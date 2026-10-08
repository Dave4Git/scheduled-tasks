# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

import random
import datetime as dt
import smtplib
import pandas as pd
from email.mime.text import MIMEText

PORT = 587
HOST = "smtp.gmail.com"

##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

num = random.randint(1,3)
#print(num)
birthday_letter = f"letter_templates/letter_{num}.txt"

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
day = now.day

with open("birthdays.csv") as file:
	birthdays = pd.read_csv("birthdays.csv")

for index, row in birthdays.iterrows():
	if month == row["month"] and day == row["day"]:
		birthday_name = row["name"]
		to_email = row["email"]
		with open(birthday_letter) as email_template:
			email_body = email_template.read()
			## create new doc in here, replacing [name] with name
			new_letter = email_body.replace("[NAME]", birthday_name)
			print(new_letter)
		with smtplib.SMTP(host=HOST, port=PORT) as connection:
			connection.starttls()
			connection.login(user=MYEMAIL, password=PASSWORD)
			connection.sendmail(
							from_addr=MYEMAIL,
							to_addrs=to_email,
							msg=f"Subject:Happy Birthday!\n\n{new_letter}")




