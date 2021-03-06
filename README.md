# Scoot Loop Graphs

The code in this repo grabs data from the HCC CKAN respository and creates a graph for each Scoot Loop on the computer running the script. You can then take these graphs and host them on a web server.

See output of this script in action at https://hullscootloops.netlify.com. 

## To setup your environment
1. apt-get install python3
2. apt-get install python3-pip
3. pip3 install plotly
4. pip3 install statsmodels
5. pip3 install requests
6. pip3 install folium

## Build the graphs

**getResources.py** builds a rubbishy html table index. Modify it so that it puts the index with the graphs (or change the href so it points where you want it to). You can use map.py instead if you'd like a map of scoop loops rather than a list. 

**map.py** builds a map of scoot loops using folium and leaflet. Popups for each marker link to graphs in the same directory.

**scootLoopGrab.py** grabs the last 3000 readings (edit the SQL to increase/reduce this) for each Scoot Loop published to the HCC CKAN respository and creates a graph for each Scoot Loop.

Create a cron job to run the code at regular intervals and copy the resultant html files into your public web directory. Be aware. Grabbing all scoot loop data from the CKAN server places considerable load on it. Grabbing should take around half an hour or so.

## The software in this repository is released under the following licence

> This program is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, either version 3 of the License, or
> (at your option) any later version.
> 
> This program is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
> GNU General Public License for more details.
> 
> You should have received a copy of the GNU General Public License
> along with this program.  If not, see <https://www.gnu.org/licenses/>.
