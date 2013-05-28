## Put together by @nickpersico, Sales Ops at Krossover.com
## Closetronic - Close.io to Leftronic Python Script Example - Going through a list of leads via search query

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

#Sample URL for all new "active" opportunities created today
url = 'https://app.close.io/api/v1/lead/?query=opportunity_status%3Aactive%20opportunity_created%3Atoday%20'
response = requests.get(url, auth=(closeio_key, ''), headers={'Content-Type': 'application/json'})

#Loop to go through the list of opportunities to retrieve all values, and then add them up
opportunities = []
for lead in response.json['data']:
    opportunities.extend(lead['opportunities'])

total_value = 0

for opportunity in opportunities:
    if opportunity['value']:
        total_value += opportunity['value']
    if opportunity['value'] is None :
      print 0

#Close.io outputs currency in cents, must divide by 100.0
today_opp_value = total_value / 100.0

#Push value to Leftronic widget
update.pushNumber("LEFTRONIC_WIDGET_STREAM_NAME", {"prefix": "$", "number": today_opp_value})