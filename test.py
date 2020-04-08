import json
import urllib
import urllib.request
import plotly.express as px
import dateutil.parser

sqlurl = "https://opendata.hullcc.gov.uk/api/3/action/datastore_search_sql?sql="
sql = "SELECT * from \"2aeb1f0d-5daf-4304-9b50-d3436c72a52a\" ORDER BY _id desc LIMIT 3000"
url = sqlurl + urllib.parse.quote(sql)
data = urllib.request.urlopen(url)

jsonData = json.loads(data.read())

result = jsonData.get('result')
records = result.get('records')

timeArray = []
flowArray = []

for e in records:
    timeArray.append(dateutil.parser.parse(e["MeasurementTime"]))
    flowArray.append(e["VehicleFlow"])

#print timeArray
#print flowArray
fig = px.scatter(x=timeArray, y=flowArray, labels={'x':'Time','y':'Vehicle Flow'}, trendline="lowess")
fig.write_html('test.html', auto_open=True)
