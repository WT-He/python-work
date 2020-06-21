import pandas as pd
import requests
import json
import datetime as dt

def getHubei():
# 获取当前时间
    now_time = dt.datetime.now().strftime('%F')   # %F为只显示年月日

    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    area = requests.get(url).json()
    data = json.loads(area['data'])
    update_time = data['lastUpdateTime']
    all_counties = data['areaTree']
    all_list = []
    for country_data in all_counties:
        if country_data['name'] != '中国':
            continue
        else:
            all_provinces = country_data['children']
            for province in all_provinces:
                if province['name'] != '湖北':
                    continue
                else:
                    all_cites = province['children']
                    for city_data in all_cites:
                        city_name = city_data['name']
                        city_today = city_data['today']
                        city_total = city_data['total']
                        city_result = {'省份':province['name'],'城市': city_name, '更新日期': update_time, '现有确诊': city_total['nowConfirm'],
                                           '累计确诊': city_total['confirm'],'累计治愈': city_total['heal'],'累计死亡': city_total['dead'],
                                           '今日新增确诊': city_today['confirm'],'今日新增治愈': city_today['confirmCuts']}
                        all_list.append(city_result)#将当前省份的数据添加到数据列表里面

    df = pd.DataFrame(all_list)
    df.to_csv('Hubei/' + now_time + '.csv', index=False, encoding="utf_8_sig")


