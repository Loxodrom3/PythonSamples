from urllib.request import urlopen
import pandas as pd
import re

# Read station list from inputList.txt
with open("inputList.txt", "r") as file:
   stationList = file.read().splitlines()

# Get output file
outputDS_file_name = "outputCORSDS.txt"
outDS_file = open(outputDS_file_name, "w")
outputCoord_file_name = "outputCoordinates.txt"
outCoord_file = open(outputCoord_file_name, "w")

for station in stationList:
    print(station)
    url = 'https://www.ngs.noaa.gov/cgi-cors/CorsSidebarSelect.prl?site=' + station + '&option=Coordinates14'
    dataSheet = urlopen(url).read()
    data = dataSheet.decode('utf-8')

    if dataSheet:   # need a different check for "bad station"
        # Write DataSheet to outDS_file
        outDS_file.write(data)
        outDS_file.write('\n')
        outDS_file.write('\n')
        outDS_file.write('---------------------------------------------------------------')
        outDS_file.write('\n')
        # Write ITRF ccoordinates to outCoord_file
        outCoord_file.write('\n')
        outCoord_file.write(station)
        outCoord_file.write('\n')
        # Parse data to what we need for ITRF
        x = data.find("ITRF2014 POSITION")
        outCoord_file.write(data[x:x+35])
        outCoord_file.write('\n')
        outCoord_file.write(data[x+160:x+185])
        outCoord_file.write('\n')
        outCoord_file.write(data[x+240:x+265])
        outCoord_file.write('\n')
        outCoord_file.write(data[x+320:x+345])
        outCoord_file.write('\n')
        outCoord_file.write('\n')
        outCoord_file.write('\n')
        outCoord_file.write('---------------------------------------------------------------')
        # Write NAD83 ccoordinates to outCoord_file
        # Homework for Jonathon
    else:
        print("Failed to fetch data for station:", station)

outDS_file.close()
outCoord_file.close()
