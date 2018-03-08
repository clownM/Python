# -*- coding:gbk -*-
import urllib.request
import json
from city import city

cityname = input('你想查哪个城市的天气？\n')
citycode = city.get(cityname)
if citycode:
    try:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' %citycode)
        web = urllib.request.urlopen(url)
        content = json.loads(web.read())
        weatherinfo = content["weatherinfo"]
        min_temperature = weatherinfo["temp1"]
        max_temperature = weatherinfo["temp2"]
        weather = weatherinfo["weather"]
        print("最低气温为%s"%min_temperature)
        print("最高气温为%s"%max_temperature)
        print("天气情况为%s"%weather)
    except:
        print("查询失败")
else:
    print("没有找到该城市")


