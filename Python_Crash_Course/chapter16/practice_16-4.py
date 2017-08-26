import pandas as pd
import matplotlib.pyplot as plt

df0 = pd.read_csv('sitka_weather_2014.csv', keep_default_na=False, usecols=['AKST', 'Max Humidity', ' Min Humidity'])
df0.index = pd.to_datetime(df0.AKST)
df = df0.drop('AKST', axis=1)

fig = plt.figure()
plt.subplot(111)
plt.plot(df.index, df.iloc[:, 0], color='blue', linestyle='-', alpha=0.5)
plt.plot(df.index, df.iloc[:, 1], color='blue', linestyle='-', alpha=0.5)
plt.fill_between(df.index, df.iloc[:, 1], df.iloc[:, 0], facecolor='blue', alpha=0.5)
#plt.xlim(df.iloc[:, 1].min(), df.iloc[:, 0].max())
plt.show()
