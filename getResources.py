import json
import urllib.request
import dateutil.parser
import re

resourceURL = "https://opendata.hullcc.gov.uk/dataset/30fd3969-556d-4eae-ae4c-f3f9d2cfa9e3/resource/90e1cce0-295e-4fa7-aa21-ebc4f3e8e8d4/download/scoot_loop_resources_full.json"
data = urllib.request.urlopen(resourceURL)
jsonData = json.loads(data.read())

strTable = "<html><table border = \"1\"><tr><th>Hull Scoot Loop Vehicle Flow Data</th></tr>"
for e in jsonData:
    desc = re.sub("(- https.*$)", "\1", e["description"])
    strRow = "<tr><td><a href=\"" + e["resource_id"] + ".html\">" + desc + "</a></td></tr>"
    strTable = strTable + strRow

strTable = strTable + "</table></html>"

html = open("index.html", 'w')
html.write(strTable)

print(strTable)
