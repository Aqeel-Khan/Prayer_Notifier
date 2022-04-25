import requests
from twilio.rest import Client
import datetime
import os

#Twilio keys and client
account_sid = os.environ["ACC_SID"]
auth_token = os.environ["AUTH_TOKEN"]
client = Client(account_sid, auth_token)

#MuslimSalat api details
MS_API_KEY = "9d7fef2e488b01d637fd51b43b0de7b6"
MS_ENDPOINT = "http://muslimsalat.com/location/date.json"

#Current location latitude and longitude
params = {
    "latitude": 1.426562474853169,
    "longitude": 103.77268195152284,
}

#DateTime module to allow MuslimSalat API timing to match current time
today = datetime.datetime.today()
today_date = today.strftime("%d/%m/%Y")
#Replacement of current time to allow testing of current time to prayer time for program testing.
today_time = today.replace(hour=6, minute=6).strftime("%I:%M %p").lower().strip("0")
print(today_date)
print(today_time)

#Getting api info in json format
response = requests.get(url=f"http://muslimsalat.com/singapore/{today_date}.json", params=params)
result = (response.json()["items"][0])
print(result)

#running current time against list of prayer time to identify the specific prayer.
for key in result:
    if today_time in result[key]:
        message = client.messages \
            .create(
            body=f"It is {key} time!",
            from_='+19704009862',
            to='+6591390085'
        )
