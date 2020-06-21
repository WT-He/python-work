import pandas as pd
import requests
import json
import datetime as dt
import wordcloud
import jieba


def getChinaallpro():
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
            for province_data in all_provinces:
                province_name = province_data['name']
                province_today = province_data['today']
                province_total = province_data['total']
                province_result = {'省份': province_name, '更新日期': update_time, '现有确诊': province_total['nowConfirm'],
                                   '累计确诊': province_total['confirm'],'累计治愈': province_total['heal'],'累计死亡': province_total['dead'],
                                   '今日新增确诊': province_today['confirm'],'今日治愈': province_today['confirmCuts']}
                all_list.append(province_result)#将当前省份的数据添加到数据列表里面
    def yxhcreater(city1,city2,city3):
        yxhtxt1=" {0}{1}是怎么回事呢？{0}相信大家都很熟悉，但是{0}{1}是怎么回事呢，\n下面就让小编带大家一起了解吧。".format(city1,city2)
        yxhtxt2="{0}{1}，其实就是{2}，大家可能会很惊讶{0}怎么会{1}呢？\n但事实就是这样，小编也感到非常惊讶。".format(city1,city2,city3)
        yxhtxt3="这就是关于{0}{1}的事情了，\n大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！".format(city1,city2)
        print(yxhtxt1+yxhtxt2+yxhtxt3)
    list00 = []
    namestr =""
    namelist=[]
    for list in all_list:
        num = list["今日新增确诊"]
        # address = list["省份"]
        list00.append(num)
    list00.sort(reverse = True)
    tem = []
    for i in range(0,5):
        tem.append(list00[i])
    try_num = 0
    for province in all_list:
        if(province["今日新增确诊"] in tem) and try_num<=4:
            namelist.append(province["省份"])
            namestr = namestr + str(province["省份"])
            try_num=try_num+1

    print("")
    print("新增最多的五个城市:")
    print(namestr)   #新增最多的五个城市
    print("")

    w = wordcloud.WordCloud()
    txt = " ".join(jieba.lcut(namestr))
    print("txt:",end="")
    print(txt)

    # 此段为汉字转拼音 因为我的电脑无端出现无法完成汉字词云的bug
    from xpinyin import Pinyin
    p = Pinyin()
    ret = p.get_pinyin(txt, '')
    print(ret)

    w.generate(ret)
    w.to_file("result.png")
    print("词云已生成至本文件夹下result文件\n")
    print("营销号生成文章：")
    yxhcreater(str(namelist[0]),str(namelist[1]),str(namelist[2]))

    df = pd.DataFrame(all_list)
    df.to_csv('China/' + now_time + '.csv', index=False, encoding="utf_8_sig")

