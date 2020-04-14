import json
import urllib.request
from datetime import datetime
import re
import folium

resourceURL = "https://opendata.hullcc.gov.uk/dataset/30fd3969-556d-4eae-ae4c-f3f9d2cfa9e3/resource/90e1cce0-295e-4fa7-aa21-ebc4f3e8e8d4/download/scoot_loop_resources_full.json"
data = urllib.request.urlopen(resourceURL)
jsonData = json.loads(data.read())

map = folium.Map(
		location=[53.767771, -0.327524],
		zoom_start=13
		)

for e in jsonData:
	desc = re.sub("(- https.*$)", "\1", e["description"])
	html ="""
	<html>
	<a href="%(resource)s.html" target="_blank">%(description)s</a>
	</html>""" %{'resource' : e['resource_id'],'description' : desc}
	popup = folium.Popup(html, max_width=2650)
	folium.Marker([e["longtitude"],e["latitude"]],popup=popup).add_to(map)
map.save('map.html')
