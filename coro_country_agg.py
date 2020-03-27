import csv
import matplotlib.pyplot as plt
import pandas as pd

url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
coroHeaderNames = ("Date","Country","Confirmed","Deaths")  # as of 3/26, removed "Recovered" data from dataset...

#popURL = 'https://gist.githubusercontent.com/tmcw/4179511/raw/e640b042b4074663a37cd9258db79ac5dbad3e92/pop.csv'
#popHeaderNames=("Country","Ranking","blank1","name","pop","blank2","blank3","blank4","blank5","blank6","blank7")

#making data frame from csv file  Source: https://github.com/datasets/covid-19/tree/master/data
coroDf = pd.read_csv(url, error_bad_lines=False, names=coroHeaderNames, header=0)
#popDf  = pd.read_csv(popURL, error_bad_lines=False, names=popHeaderNames, header=0)
#selCHN = coroDf.loc[coroDf['Country'] == 'China', ["Date"], ["Confirmed"]]

yIntercept = 10

xUSA=[]
xCHN=[]
xITA=[]
xSPN=[]
xDEU=[]

USAPlot=[]
CHNPlot=[]
ITAPlot=[]
SPNPlot=[]
DEUPlot=[]

CHN = coroDf.loc[coroDf["Country"]=="China"]
ITA = coroDf.loc[coroDf["Country"]=="Italy"]
SPN = coroDf.loc[coroDf["Country"]=="Spain"]
USA = coroDf.loc[coroDf["Country"]=="US"]
DEU = coroDf.loc[coroDf["Country"]=="Germany"]
#print(USA)

type="Deaths"
USADate=USA["Date"]
USAData=USA[type]
CHNDate=CHN["Date"]
CHNData=CHN[type]
ITADate=ITA["Date"]
ITAData=ITA[type]
SPNDate=SPN["Date"]
SPNData=SPN[type]
DEUDate=DEU["Date"]
DEUData=DEU[type]

for row in USAData:
    if (row > yIntercept):
        USAPlot.append(row)

for row in CHNData:
    if (row > yIntercept):
        CHNPlot.append(row)

for row in ITAData:
    if (row > yIntercept):
        ITAPlot.append(row)

for row in SPNData:
    if (row > yIntercept):
        SPNPlot.append(row)

for row in DEUData:
    if (row > yIntercept):
        DEUPlot.append(row)

for x in range(0, len(USAPlot)):
    xUSA.append(x)
for x in range(0, len(CHNPlot)):
    xCHN.append(x)
for x in range(0, len(ITAPlot)):
    xITA.append(x)
for x in range(0, len(SPNPlot)):
    xSPN.append(x)
for x in range(0, len(DEUPlot)):
    xDEU.append(x)

plt.plot(xCHN,CHNPlot,label="CHN")
plt.plot(xITA,ITAPlot,label="ITA")
plt.plot(xSPN,SPNPlot,label="SPN")
plt.plot(xUSA,USAPlot,label="USA")
plt.plot(xDEU,DEUPlot,Label="DEU")
plt.title("Number of days since Reported "+type+" passed "+str(yIntercept))
#plt.yscale("log")
plt.legend()
plt.show()
