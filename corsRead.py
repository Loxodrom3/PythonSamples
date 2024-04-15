from urllib.request import urlopen

# replace stationList with a read of inputList.txt
# get output file
# open file
stationList = ["neal", "negi", "neho", "neor", "nerc", "neyk"]


for i in range(0, len(stationList)): #
    print(stationList[i])
    url = 'https://www.ngs.noaa.gov/cgi-cors/CorsSidebarSelect.prl?site=' + stationList[i] + '&option=Coordinates14'
    dataSheet = urlopen(url).read()
    # error check for URL return
    print(dataSheet.decode('utf-8'))
    # write to outputfile
    # Parse data to what we need
