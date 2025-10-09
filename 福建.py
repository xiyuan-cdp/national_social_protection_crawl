import json

import requests

cookies = {
    'JSESSIONID': 'B59A55F704036184E4A2FF297A09B020',
    '__51cke__': '',
    '__tins__21889365': '%7B%22sid%22%3A%201753265920845%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201753267768814%7D',
    '__51laig__': '16',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Origin': 'https://zwfw.fujian.gov.cn',
    'Referer': 'https://zwfw.fujian.gov.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = (
    ('userType', '1'),
    ('areaCode', '350000'),
    ('bigType', '01'),
    ('smallType', '085'),
    ('pageNum', '1'),
    ('pageSize', '100'),
    ('isOnline', '0'),
    ('serviceName', ''),
)

response = requests.get('https://zwfw.fujian.gov.cn:732/cms-business/apasService/getThemeApasServiceByParams',
                        headers=headers, params=params, cookies=cookies)
data = json.loads(response.text)
result = []
for item in data['data']:
    if item['apasServiceSimpleList']:
        for i in item['apasServiceSimpleList']:
            url = f'https://zwfw.fujian.gov.cn/person-todo/todo-fingerpost?unid={i['unid']}&infoType=1'
            result.append(url)
            print(url)
    if item['rspDirectoryApasService']:
        for a in item['rspDirectoryApasService']:
            for i in a['apasServiceSimpleList']:
                url = f'https://zwfw.fujian.gov.cn/person-todo/todo-fingerpost?unid={i['unid']}&infoType=1'
                result.append(url)
                print(url)
print(result)