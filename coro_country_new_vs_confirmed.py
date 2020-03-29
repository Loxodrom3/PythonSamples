import csv
import matplotlib.pyplot as plt
import pandas as pd

url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
coroHeaderNames = ("Date","Country","Confirmed","recovered","Deaths")  # as of 3/26, removed "Recovered" data from dataset...

#making data frame from csv file  Source: https://github.com/datasets/covid-19/tree/master/data
coroDf = pd.read_csv(url, error_bad_lines=False, names=coroHeaderNames, header=0)

type="Confirmed"
yStart = 100  # start conisdering data when the type has reaced this amount
winSize = 7 # window size for moving average

#define x range for the countries
#xUSA=[] xCHN=[] #xITA=[] xSPN=[] xDEU=[]
USAConf=[]
USAConfAvg=[]
CHNConf=[]
CHNConfAvg=[]
ITAConf=[]
ITAConfAvg=[]
SPNConf=[]
SPNConfAvg=[]
DEUConf=[]
DEUConfAvg=[]
KORConf=[]
KORConfAvg=[]

#USAPlot=[] CHNPlot=[] ITAPlot=[] SPNPlot=[] DEUPlot=[]
USANew=[]
USANewAvg=[]
CHNNew=[]
CHNNewAvg=[]
ITANew=[]
ITANewAvg=[]
SPNNew=[]
SPNNewAvg=[]
DEUNew=[]
DEUNewAvg=[]
KORNew=[]
KORNewAvg=[]

USA = coroDf.loc[coroDf["Country"]=="US"]
CHN = coroDf.loc[coroDf["Country"]=="China"]
ITA = coroDf.loc[coroDf["Country"]=="Italy"]
SPN = coroDf.loc[coroDf["Country"]=="Spain"]
DEU = coroDf.loc[coroDf["Country"]=="Germany"]
KOR = coroDf.loc[coroDf["Country"]=="Korea, South"]


for x in range(0, len(USA)):
    if (USA.iloc[x,2] > yStart):
        USAConf.append(USA.iloc[x,2])
        USANew.append(USA.iloc[x,2]-USA.iloc[x-1,2])
i=0
while i < len(USAConf)-winSize+1:
    USAConfAvg.append(sum(USAConf[i:i+winSize])/winSize)
    USANewAvg.append(sum(USANew[i:i+winSize])/winSize)
    i += 1

for x in range(0, len(CHN)):
    if (CHN.iloc[x,2] > yStart):
        CHNConf.append(CHN.iloc[x,2])
        if x==0:
            CHNNew.append(0)
        else:
            CHNNew.append(CHN.iloc[x,2]-CHN.iloc[x-1,2])
i=0
while i < len(CHNConf)-winSize+1:
    CHNConfAvg.append(sum(CHNConf[i:i+winSize])/winSize)
    CHNNewAvg.append(sum(CHNNew[i:i+winSize])/winSize)
    i += 1

for x in range(0, len(ITA)):
    if (ITA.iloc[x,2] > yStart):
        ITAConf.append(ITA.iloc[x,2])
        ITANew.append(ITA.iloc[x,2]-ITA.iloc[x-1,2])
i=0
while i < len(ITAConf)-winSize+1:
    ITAConfAvg.append(sum(ITAConf[i:i+winSize])/winSize)
    ITANewAvg.append(sum(ITANew[i:i+winSize])/winSize)
    i += 1

for x in range(0, len(SPN)):
    if (SPN.iloc[x,2] > yStart):
        SPNConf.append(SPN.iloc[x,2])
        SPNNew.append(SPN.iloc[x,2]-SPN.iloc[x-1,2])
i=0
while i < len(SPNConf)-winSize+1:
    SPNConfAvg.append(sum(SPNConf[i:i+winSize])/winSize)
    SPNNewAvg.append(sum(SPNNew[i:i+winSize])/winSize)
    i += 1

for x in range(0, len(DEU)):
    if (DEU.iloc[x,2] > yStart):
        DEUConf.append(DEU.iloc[x,2])
        DEUNew.append(DEU.iloc[x,2]-DEU.iloc[x-1,2])
i=0
while i < len(DEUConf)-winSize+1:
    DEUConfAvg.append(sum(DEUConf[i:i+winSize])/winSize)
    DEUNewAvg.append(sum(DEUNew[i:i+winSize])/winSize)
    i += 1

for x in range(0, len(KOR)):
    if (KOR.iloc[x,2] > yStart):
        KORConf.append(KOR.iloc[x,2])
        KORNew.append(KOR.iloc[x,2]-KOR.iloc[x-1,2])
i=0
while i < len(KORConf)-winSize+1:
    KORConfAvg.append(sum(KORConf[i:i+winSize])/winSize)
    KORNewAvg.append(sum(KORNew[i:i+winSize])/winSize)
    i += 1

plt.plot(CHNConfAvg,CHNNewAvg,label="CHN")
plt.plot(ITAConfAvg,ITANewAvg,label="ITA")
plt.plot(SPNConfAvg,SPNNewAvg,label="SPN")
plt.plot(USAConfAvg,USANewAvg,label="USA")
plt.plot(DEUConfAvg,DEUNewAvg,Label="DEU")
plt.plot(KORConfAvg,KORNewAvg,Label="KOR")
plt.title("New vs Confirmed cases")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Confirmed cases")
plt.ylabel("New Cases")
plt.legend()
plt.show()
