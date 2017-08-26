import csv
from datetime import datetime
from matplotlib import pyplot as plt


def get_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    return (dates, highs, lows)

death_valley = 'death_valley_2014.csv'
sitka =  'sitka_weather_2014.csv'
ddates, dhighs, dlows = get_data(death_valley)
sdates, shighs, slows = get_data(sitka)

fig, axes = plt.subplots(nrows=1, ncols=2, dpi=128, figsize=(12, 6))
axes[0].plot(ddates, dhighs, c='red', alpha=0.5)
axes[0].plot(ddates, dlows, c='blue', alpha=0.5)
axes[0].fill_between(ddates, dhighs, dlows, facecolor='blue', alpha=0.1)
title1 = "Daily high and low temperatures - 2014\nDeath Valley, CA"
axes[0].set_title(title1, fontsize=14)
axes[0].set_xlabel('', fontsize=12)
axes[0].set_ylabel("Temperature (F)", fontsize=12)
axes[0].tick_params(axis="both", which="major", labelsize=12)
axes[0].set_yticks(range(0, 121, 20))

axes[1].plot(sdates, shighs, c='red', alpha=0.5)
axes[1].plot(sdates, slows, c='blue', alpha=0.5)
axes[1].fill_between(sdates, shighs, slows, facecolor='blue', alpha=0.1)
title = "Daily high and low temperatures - 2014\nSitka, AL"
axes[1].set_title(title, fontsize=14)
axes[1].set_xlabel('', fontsize=12)
axes[1].set_ylabel("Temperature (F)", fontsize=12)
axes[1].set_yticks(range(0, 121, 20))

fig.autofmt_xdate()
plt.show()
