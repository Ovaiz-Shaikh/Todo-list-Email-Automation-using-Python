import os
import smtplib
import ssl
from email.message import EmailMessage
import schedule
import time

# Define email sender and receiver
email_sender = 'your email'
email_password = 'your password'
email_receiver = 'receivers email'

# Set the subject of the email
subject = 'Daily To-Do List'

# Define the student to-do list
todo_list = [
    "1. Review lecture notes from yesterday's classes.",
    "2. Complete assignments.",
    "3. Prepare for the upcoming quiz.",
    "4. Revise key concepts from the last week's lessons.",
    "5. Study Verbal reasoning and practice Quant.",
    "6. Work on the group project for Major project.",
    "7. Take a short break and refresh yourself!",
]

# Format the to-do list as a string with bullet points
body = "Hello,\n\nHere's your to-do list for today:\n\n"
for task in todo_list:
    body += f"- {task}\n"

body += "\nStay focused and have a productive day!\n\nBest regards,\nYour Personal Assistant"

def send_email():
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

schedule.every().day.at("09:00").do(send_email)

print("Email scheduling started. Type 'STOP' to quit.")

# Run the scheduler until the user decides to stop
while True:
    schedule.run_pending()
    time.sleep(1)
    user_input = input("Enter 'STOP' to end scheduling: ").strip().upper()
    if user_input == 'STOP':
        print("Stopping email scheduling...")
        break
