# Covid-notifier
A notifier which could keep you updated about the covid cases in the states of your interest.

There are three steps you need to do:
* Create a function to push notifications
* Extract data from the source to display
* Call the notifier function to get notifications

### Create a function to push notifications
For getting notifications on windows notify function from python library plyer.notification is used.

### Get data from the source
The website used here as the source is "https://www.mohfw.gov.in"

Data is extracted from the website in json format and then converted into a DataFrame.

### Call the notifier function to get notifications
All the work is almost done now we only need to call the notifier and pass the data we need to get in the notification.
