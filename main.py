# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import os
import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
   "lat": 20.662902,
   "lon": 85.597903,
   "appid": api_key,
    "cnt" : 4,

}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
weather_data = response.json()
# print(weather_data["list"][0]["weather"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <= 700:
        will_rain = True
if will_rain:
    client= Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body="Its going to rain today . Remember to bring an umbrella",
        from_="+19379091519",
        to = "+917978730018"
    )
    print(message.status)
