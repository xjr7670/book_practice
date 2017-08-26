import pandas as pd

from pygal.style import *
from pygal_maps_world.maps import World
from country_codes import get_country_code

csv = pd.read_csv("co2_emissions.csv", keep_default_na=False, skiprows=4)
csv['code'] = csv['Country Name'].apply(get_country_code)
# 需要把CO2排放量转换为数字格式
csv['digit_2013'] = pd.to_numeric(csv['2013'])

# 把CO2排放量分3个层次
# 并把国家码和对应的2013年CO2排放量取出来放在字典中
co2_1, co2_2, co2_3 = {}, {}, {}
for code, co2 in zip(csv['code'], csv['digit_2013']):
    if co2 <= 5:
        co2_1[code] = co2
    elif co2 <=10:
        co2_2[code] = co2
    else:
        co2_3[code] = co2

wm = World(fill=True, style=RedBlueStyle)
wm.title = "World's CO2 emissions at 2013"
wm.add("CO2 <= 5", co2_1)
wm.add("CO2 <= 10", co2_2)
wm.add("CO2 > 10", co2_3)
wm.render_to_file("practice_16-7.svg")
