import json

from pygal.style import LightColorizedStyle, RotateStyle
from country_codes import get_country_code
from pygal_maps_world.maps import World

f = open("gdp.json")
gdp = json.load(f)

gdps = {}
# 把所有国家的名称通过get_country_code函数以得到其国别码
# 并把其GDP存入字典
for item in gdp:
    if item["Year"] == "2016":
        code = get_country_code(item["Country Name"])
        if code:
            gdps[code] = int(float(item["Value"])) / 100000000

# 根据GDP数量级别不同把国家分成三组
gdp_1, gdp_2, gdp_3 = {}, {}, {}
for c, g in gdps.items():
    if g < 1000:
        gdp_1[c] = g
    elif g < 10000:
        gdp_2[c] = g
    else:
        gdp_3[c] = g

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = "GDP of the Whold World - 2016"
wm.add("0-100bn", gdp_1)
wm.add("100-1000bn", gdp_2)
wm.add("1000-10000bn", gdp_3)

wm.render_to_file("gdps.svg")
