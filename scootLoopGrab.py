import json
import urllib.request
import plotly.express as px
import dateutil.parser
import re
from http.client import IncompleteRead
import requests

def grab_resources():
	resourceURL = "https://opendata.hullcc.gov.uk/dataset/30fd3969-556d-4eae-ae4c-f3f9d2cfa9e3/resource/90e1cce0-295e-4fa7-aa21-ebc4f3e8e8d4/download/scoot_loop_resources_full.json"
	data = urllib.request.urlopen(resourceURL)
	jsonData = json.loads(data.read())
	return jsonData

for e in grab_resources():
	sqlurl = "https://opendata.hullcc.gov.uk/api/3/action/datastore_search_sql?sql="
	currentResource = e["resource_id"]
	title = re.sub("(- https.*$)", "\1", e["description"])
	print("Grabbing " + title)
	sql = "SELECT * from \"" + e["resource_id"] + "\" ORDER BY _id desc LIMIT 3000"
	url = sqlurl + urllib.parse.quote(sql)
	try:
		data = requests.get(url, timeout = 5)
	except:
		print("Server didn't respond in a timely manner or sent less bytes than expected. Trying request again.")
		data = requests.get(url, timeout = 5)
	jsonData = json.loads(data.text)

	result = jsonData.get('result')
	records = result.get('records')

	timeArray = []
	flowArray = []

	for e in records:
    		timeArray.append(dateutil.parser.parse(e["MeasurementTime"]))
    		flowArray.append(e["VehicleFlow"])

	fig = px.scatter(x=timeArray, y=flowArray, labels={'x':'Time','y':'Vehicle Flow'}, trendline="lowess", title=title)
	fig.write_html("graphs/" + currentResource + ".html", auto_open=True)
