import csv
import matplotlib.pyplot as plt
import pandas as pd

url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/worldwide-aggregated.csv'
headerNames = ("Date","Confirmed","Recovered","Deaths")

#making data frame from csv file
df = pd.read_csv(url, error_bad_lines=False, names=headerNames, header=0)
#print(df)
#print(df[['Timestamp', 'MBTemp4']])
print(df.iloc[3])   #index or integer location
x= df["Date"]
y1=df["Confirmed"]
y2=df["Recovered"]
y3=df["Deaths"]
#plt.plot(x,y1, label="Confirmed")
#plt.plot(x,y2, label="Recovered")
#plt.plot(x,y3, Label="Deaths")
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.show()
