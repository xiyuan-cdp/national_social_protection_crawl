import json
import time

import requests

cookies = {
    'ICITYSession': '8a21b5cdcf534cbea1cb0bb034247ba1',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://ty.sxzwfw.gov.cn',
    'Referer': 'https://ty.sxzwfw.gov.cn/icity/govservice/project?i=1&type=gr',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def get_data():
    urls = []
    data = {
        "page": 1,
        "limit": 10000,
        "type": "all",
        "title": "",
        "serviceObject": "1",
        "name": "",
        "SearchName": "",
        "isOnlineProcessed": ""
    }
    # 获取当前时间戳
    timestamp = int(time.time() * 1000)
    # print(timestamp)
    params = (
        ('s', 'c777561751967131003'),
        ('t', '7079_c17517_' + str(timestamp)),
        ('k', '38ea516d5cd9b88a90268cd6f1f1642c'),
    )

    response = requests.post(
        'https://ty.sxzwfw.gov.cn/icity/api-v2/app.icity.govservice.ShanxiItemServiceCmd/getItemByPage',
        headers=headers, params=params, cookies=cookies, data=json.dumps(data))
    data = json.loads(response.text)
    for item in data['data']:
        for i in item['taskList']:
            url = "https://ty.sxzwfw.gov.cn/icity/icity/proinfo_new?url=https://zwfwpt.sxzwfw.gov.cn:10002/aaa/person/" + \
                  i['rowGuid']
            urls.append(url)
    # print(data)
    return urls

result = get_data()
print(result)