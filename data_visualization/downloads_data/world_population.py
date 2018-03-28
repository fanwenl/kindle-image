""" 处理json格式的数据 """
import json
import pygal.maps.world
from pygal.maps.world import COUNTRIES
from pygal.style import RotateStyle, LightColorizedStyle

filename = ".\\downloads_data\\population_data.json"

def get_country_code(country_names):
    """ 根据指定的国家，返回pygal使用的两个字母的国别码 """
    for code, name in COUNTRIES.items():
        if name == country_names:
            return code
    # 没有找到返回None
    return None

with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口的空字典
cc_populations = {}

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict["Value"]))
        codes = get_country_code(country_name)
        if codes:
            cc_populations[codes] = population
        else:
            print("REEOR-:" + country_name)
            
# 根据人口数量将所有的国家分为三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = "World Population in 2010, by Country"
wm.add('0-10m', cc_pops_1)
wm.add('10-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('.\\downloads_data\\maps.svg')
