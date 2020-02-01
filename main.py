#2020/1/31
import json
from urllib.request import Request, urlopen
import time
import requests
import sys
import random
import re
url = "https://app.tonystark.io/helper/api"
#包装头部
firefox_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
#构建请求
pre_time = ""
i = 0
while(1):
    if (i+1)%5 == 0:
        print("已为成功您监控" + str(i+1) +"次")
    try:
        request = Request(url, headers=firefox_headers)
        html = urlopen(request)
        data = html.read()
        strs = str(data ,'UTF-8')
        #path json
        strs_for_json = strs[9:]
        strs_for_json= strs_for_json[:-3]
        data = strs_for_json
        datas = json.dumps(data)
        data_json = json.loads(data) #dict
        if pre_time != data_json["time"]:
            print(data_json)
            if (re.search('北京',data_json["amount"])) != None:
                pre_time = data_json["time"]
                api = "{you_api_addition}"
                title = "口罩抢购通知  " + data_json["desc"]
                content = "地点" + data_json["amount"] + "\n 链接" + data_json["url"]
                data = {
                    "text": title,
                    "desp": content
                }
                req = requests.post(api, data=data)
                print("推送成功")
    except Exception:
        print("第"+ str(i+1) +"次推送挂掉了")
        i = i - 1
    sleep_time = 10 + int(random.random() * 10)
    time.sleep(sleep_time)
    i = i + 1
