## Put together by @nickpersico, Sales Ops at Krossover.com
## Closetronic - Close.io to Leftronic Python Script Examples

import requests
import json
from leftronic import Leftronic
import datetime

#Your Close.io & Leftronic API Credentials
closeio_key = 'YOUR_API_KEY'
update = Leftronic("YOUR_LEFTRONIC_ACCESS_KEY")

#Use the datetime library to retrieve the current day's report
today = datetime.date.today()
tomorrow = datetime.date.today() + datetime.timedelta(days=1)

## SAMPLE CLOSE.IO REPORTING URLS ##

#Today's activity report URL & JSON response, using strings to always display the current day's report
today_report = 'https://app.close.io/api/v1/report/{YOUR_ORGANIZATION_ID}?user_id=all&date_start=%sT04:00:00.000Z&date_end=%sT06:59:59.999Z' % (today, tomorrow)
response = requests.get(today_report, auth=(closeio_key, ''), headers={'Content-Type': 'application/json'})

## PICK YOUR VARIABLE FROM THE CLOSE.IO JSON RESPONSE ##

#Calls for today using the today_report URL
calls_today = response.json['calls']

#The amount of won deals today using the same today_report URL
won_today = response.json['opportunities_won']

#The amount of revenue won today, the output is in cents, must divide by 100.0
revenue_today/100.0 = response.json['revenue_won_one_time']

#The amount of opportunities/pipeline created today, the output is in cents, must divide by 100.0
opportunities_today/100.0 = response.json['revenue_created_one_time']


## PUSH THE RESPONSE VARIABLE TO THE APPROPRIATE LEFTRONIC WIDGET ##

#Pushes the number of calls to your Leftronic widget
update.pushNumber("LEFTRONIC_WIDGET_STREAM_NAME", calls_today)

#Pushing currency values to a Leftronic pushNumber widget
update.pushNumber("LEFTRONIC_WIDGET_STREAM_NAME", {"prefix": "$", "number": revenue_today/100.0})