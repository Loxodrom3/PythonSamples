import csv
import matplotlib.pyplot as plt
import pandas as pd

url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
coroHeaderNames = ("Date","Country","Confirmed","Recovered","Deaths")

#popURL = 'https://gist.githubusercontent.com/tmcw/4179511/raw/e640b042b4074663a37cd9258db79ac5dbad3e92/pop.csv'
#popHeaderNames=("Country","Ranking","blank1","name","pop","blank2","blank3","blank4","blank5","blank6","blank7")

#making data frame from csv file  Source: https://github.com/datasets/covid-19/tree/master/data
coroDf = pd.read_csv(url, error_bad_lines=False, names=coroHeaderNames, header=0)
#popDf  = pd.read_csv(popURL, error_bad_lines=False, names=popHeaderNames, header=0)
#selCHN = coroDf.loc[coroDf['Country'] == 'China', ["Date"], ["Confirmed"]]

AFG = coroDf.loc[coroDf["Country"]=="Afghanistan"]
CHN = coroDf.loc[coroDf["Country"]=="China"]
USA = coroDf.loc[coroDf["Country"]=="US"]
ITA = coroDf.loc[coroDf["Country"]=="Italy"]
SPN = coroDf.loc[coroDf["Country"]=="Spain"]
print(USA)

type="Confirmed"
USADate=USA["Date"]
USADeaths=USA[type]
CHNDate=CHN["Date"]
CHNDeaths=CHN[type]
ITADate= ITA["Date"]
ITADeaths=ITA[type]
SPNDate= SPN["Date"]
SPNDeaths=SPN[type]
plt.plot(CHNDate,CHNDeaths)
plt.plot(USADate,USADeaths)
plt.plot(ITADate,ITADeaths)
plt.plot(SPNDate,SPNDeaths)
plt.show()
