import json

import requests
from DrissionPage._pages.session_page import SessionPage

cookies = {
    'Hm_lvt_6b2608499cef887517c1febcba5a6259': '1753353220',
    'HMACCOUNT': 'A89E656BF367E71C',
    'oldMode': '1',
    'JSESSIONID': '68233FCD6C585390448D3C6F21DF47F0',
    'Hm_lpvt_6b2608499cef887517c1febcba5a6259': '1753353230',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://www.hnzwfw.gov.cn',
    'Referer': 'https://www.hnzwfw.gov.cn/portal/personal/index',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {"personZt": "16", "countPerPage": 1000, "currentPageNum": 1, "catalogName": "", "onlineFlag": "",
        "areaCode": "410000000000", "forUser": "01", "sortField": "serviceType", "sortOrder": "DESC"}

page = SessionPage()
page.post('https://www.hnzwfw.gov.cn/hnzwfw/matter/catalogListByParams', headers=headers,
                         cookies=cookies, data=json.dumps(data))
data = page.response.json()
result = []
for i in data['result']['data']:
    for service in i['serviceList']:
        url = f'https://www.hnzwfw.gov.cn/portal/guide/{service['unid']}'
        result.append(url)
print(result)