import pandas as pd
import requests
import json
import pickle as pk
import datetime as dt

def saveData():
    # 获取当前时间
    now_time = dt.datetime.now().strftime('%F')   # %F为只显示年月日

    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    area = requests.get(url).json()
    data = json.loads(area['data'])
    with open('dataSource/' + now_time + '.pkl', 'wb') as f:  # dataSource为当前工作区间下的文件夹
        pk.dump(data, f)

    #with open('dataSource/'+ now_time + '.pkl', 'rb') as f:  #打开文件
        #test = pk.load(f)
