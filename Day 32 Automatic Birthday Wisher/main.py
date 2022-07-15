##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import os
import smtplib, random, pandas
import datetime as dt

MY_EMAIL = os.environ.get('TEST_GMAIL')
MY_PASSWORD = os.environ.get('TEST_GMAIL_PASSWORD')

today = dt.datetime.now()
today_tuple = (today.month, today.day)

dataframe = pandas.read_csv('birthdays.csv')
birthday_list = dataframe.to_dict(orient='records')

for dict in birthday_list:
    birthday_tuple = (dict['month'], dict['day'])
    name = dict['name']
    target_email = dict['email']
    if today_tuple == birthday_tuple:
        letter_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
        with open(letter_path, "r") as mail_file:
            mail_content = mail_file.read()
            new_content = mail_content.replace("[NAME]", name.title())
            print(new_content)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=target_email,
                msg=f"Subject:Happy Birthday!!! 🥳🎉\n\n{new_content}"
            )
