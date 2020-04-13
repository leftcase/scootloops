import json
import urllib.request
import dateutil.parser
import re

resourceURL = "https://opendata.hullcc.gov.uk/dataset/30fd3969-556d-4eae-ae4c-f3f9d2cfa9e3/resource/90e1cce0-295e-4fa7-aa21-ebc4f3e8e8d4/download/scoot_loop_resources_full.json"
data = urllib.request.urlopen(resourceURL)
jsonData = json.loads(data.read())

strTable = """<style type=\"text/css\">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:5px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:5px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-xkfo{background-color:#000000;border-color:inherit;text-align:left;vertical-align:top;font-weight:bold;color:FFFFFF}
</style><html>
<table class =\"tg\" border = \"1\"><tr><th class=\"tg-xkfo\">Hull Scoot Loop Vehicle Flow Data</th></tr>"""
for e in jsonData:
    desc = re.sub("(- https.*$)", "\1", e["description"])
    strRow = "<tr><td class=\"tg-0pky\"><a href=\"" + e["resource_id"] + ".html\">" + desc + "</a></td></tr>"
    strTable = strTable + strRow

strTable = strTable + "</table></html>"

html = open("index.html", 'w')
html.write(strTable)

print(strTable)
