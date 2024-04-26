from urllib.request import urlopen
import re

# Read station list from inputList.txt
# with open("inputList.txt", "r") as file:
#   stationList = file.read().splitlines()
stationList = ("NEAL", "CHCM", "HAHD")

# Get output file
output_file_path = "output.txt"
scratchFile = "scratch.txt"
output_file = open(output_file_path, "w")
scratchFile = open(scratchFile, "w")

for station in stationList:
    print(station)
    url = 'https://www.ngs.noaa.gov/cgi-cors/CorsSidebarSelect.prl?site=' + station + '&option=Coordinates14'
    dataSheet = urlopen(url).read()
    # Error check for URL return
    # extract_locations(dataSheet) 
    
    if dataSheet:   # need a different check for "bad station"
        dataSheetStr = dataSheet.decode('utf-8')
        scratchFile.write(dataSheetStr)
        scratchData = open('scratch.txt')
        blah = scratchData.readlines()
        #for line in range(11):
        #    scratchData.readline() 
        blah
        output_file.write(scratchData)
        output_file.write('\n')  
        output_file.write('\n')  
        output_file.write('---------------------------------------------------------------')  
        output_file.write('\n')  
        output_file.write('\n')  
        # Parse data to what we need
    else:
        print("Failed to fetch data for station:", station)

output_file.close()
