import csv
import matplotlib.pyplot as plt
import pandas as pd

url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
coroHeaderNames = ("Date","Country","Confirmed","Recovered","Deaths")  # as of 3/26, removed "Recovered" data from dataset...

#making data frame from csv file  Source: https://github.com/datasets/covid-19/tree/master/data
coroDf = pd.read_csv(url, error_bad_lines=False, names=coroHeaderNames, header=0)

type="Deaths"
yIntercept = 100

USAPop=1# 311592000
CHNPop=1#1344130000
ITAPop=1#  60770000
SPNPop=1#  46235000
DEUPop=1#  81726000
KORPop=1

xUSA=[]
xCHN=[]
xITA=[]
xSPN=[]
xDEU=[]
xKOR=[]

USAPlot=[]
CHNPlot=[]
ITAPlot=[]
SPNPlot=[]
DEUPlot=[]
KORPlot=[]

USA = coroDf.loc[coroDf["Country"]=="US"]
CHN = coroDf.loc[coroDf["Country"]=="China"]
ITA = coroDf.loc[coroDf["Country"]=="Italy"]
SPN = coroDf.loc[coroDf["Country"]=="Spain"]
DEU = coroDf.loc[coroDf["Country"]=="Germany"]
KOR = coroDf.loc[coroDf["Country"]=="Korea, South"]

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
KORDate=KOR["Date"]
KORData=KOR[type]
print(KORData)

for row in USAData:
    if (row > yIntercept):
        USAPlot.append(row/USAPop)

for row in CHNData:
    if (row > yIntercept):
        CHNPlot.append(row/CHNPop)

for row in ITAData:
    if (row > yIntercept):
        ITAPlot.append(row/ITAPop)

for row in SPNData:
    if (row > yIntercept):
        SPNPlot.append(row/SPNPop)

for row in DEUData:
    if (row > yIntercept):
        DEUPlot.append(row/DEUPop)

for row in KORData:
    if (row > yIntercept):
        KORPlot.append(row/KORPop)

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
for x in range(0, len(KORPlot)):
    xKOR.append(x)

plt.plot(xCHN,CHNPlot,label="CHN")
plt.plot(xITA,ITAPlot,label="ITA")
plt.plot(xSPN,SPNPlot,label="SPN")
plt.plot(xUSA,USAPlot,label="USA")
plt.plot(xDEU,DEUPlot,Label="DEU")
plt.plot(xKOR,KORPlot,Label="KOR")
plt.title("Number of days since Reported "+type+" passed "+str(yIntercept))
#plt.yscale("log")
plt.legend()
plt.show()
