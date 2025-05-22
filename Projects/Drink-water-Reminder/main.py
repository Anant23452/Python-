import time
from desktop_notifier import DesktopNotifier

while True:
    print ("please sip some water !")

DesktopNotifier.notify("Drink Water Reminder", "Please sip some water!")
time.sleep(3600)  # Wait for 1 hour before showing the next notification