import csv
import matplotlib.pyplot as plt
import pandas as pd

url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv'
coroHeaderNames = ("Date","Region","Province-State","Lat","Long","Confirmed","Recovered","Deaths")

popURL = 'https://gist.githubusercontent.com/tmcw/4179511/raw/e640b042b4074663a37cd9258db79ac5dbad3e92/pop.csv'
popHeaderNames=("Country","Ranking","blank1","name","pop","blank2","blank3","blank4","blank5","blank6","blank7")

#making data frame from csv file
coroDf = pd.read_csv(url, error_bad_lines=False, names=coroHeaderNames, header=0)
popDf  = pd.read_csv(popURL, error_bad_lines=False, names=popHeaderNames, header=0)

#print(df[['Timestamp', 'MBTemp4']])
#print(df.iloc[3])   #index or integer location
x= coroDf["Date"]
y1=coroDf["Confirmed"]
selCHN = coroDf.loc[coroDf['Region'] == 'China']
print(coroDf)
print(selCHN["Confirmed"])
#print(selCHN["Confirmed"])
#plt.plot(x,selCHN["Confirmed"])
#plt.show()
