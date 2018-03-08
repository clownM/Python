# -*- coding:gbk -*-
import urllib.request
import json
from city import city

cityname = input('������ĸ����е�������\n')
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
        print("�������Ϊ%s"%min_temperature)
        print("�������Ϊ%s"%max_temperature)
        print("�������Ϊ%s"%weather)
    except:
        print("��ѯʧ��")
else:
    print("û���ҵ��ó���")


