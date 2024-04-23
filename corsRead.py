from urllib.request import urlopen

# Read station list from inputList.txt
with open("inputList.txt", "r") as file:
    stationList = file.read().splitlines()

# Get output file
output_file_path = "CORSoutput.txt"
output_file = open(output_file_path, "w")

for station in stationList:
    print(station)
    url = 'https://www.ngs.noaa.gov/cgi-cors/CorsSidebarSelect.prl?site=' + station + '&option=Coordinates14'
    dataSheet = urlopen(url).read()
    # Error check for URL return
    if dataSheet:   # need a different check for "bad station"
        data = dataSheet.decode('utf-8')
        output_file.write(data)
        output_file.write('\n')  
        output_file.write('\n')  
        output_file.write('\n')  
        # Parse data to what we need
    else:
        print("Failed to fetch data for station:", station)

output_file.close()
