import requests

cookies = {
    'SESSION': 'ZmVhOWJlN2EtZTA2MS00MDRiLWJkOTktNzVjNjk4ZjYzZGM3',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://zwfw.tj.gov.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = (
    ('area_code', '120000'),
    ('current', '1'),
    ('dept_code', ''),
    ('size', '1000'),
    ('type', 'P'),
    ('user_topic_type', '085'),
)

response = requests.get('https://zwfw.tj.gov.cn/Gov/hall/task/page-user-task-list', headers=headers, params=params, cookies=cookies)
data = response.json()
result = []
for item in data['result']:
    for i in item['list']:
        url = f'https://zwfw.tj.gov.cn/#/operatingInstruction?taskCode={i['itemId']}'
        result.append(url)
print(result)