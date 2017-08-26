import pandas as pd
import matplotlib.pyplot as plt

df0 = pd.read_csv('sitka_weather_2014.csv', keep_default_na=False, usecols=['AKST', 'PrecipitationIn'])
df0.index = pd.to_datetime(df0.AKST)
df = df0.drop('AKST', axis=1)

fig = plt.figure()
plt.subplot(111)
plt.fill_between(df.index, [0] * 356, df.PrecipitationIn, facecolor='blue', alpha=0.7)
plt.ylim(df.iloc[:, 0].min(), df.iloc[:, 0].max())
plt.show()
