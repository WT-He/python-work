#主函数
import besideH
import chinaAllprovince
import dataSource
import Hubei

print('正在链接目标网站……')
dataSource.saveData()   # 保存源数据
print('正在保存源数据……')
Hubei.getHubei()    # 保存湖北数据
print('正在保存湖北省各市数据……')
besideH.getBesideHu()   # 保存非湖北数据
print('正在保存非湖北省的各市数据……')
print('正在保存全国省份数据……')
chinaAllprovince.getChinaallpro()   # 保存全国省数据



