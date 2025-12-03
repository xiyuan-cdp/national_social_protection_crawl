import requests

cookies = {
    'yitihua20220424': '42557677',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ru;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Origin': 'https://wssp.hainan.gov.cn',
    'Referer': 'https://wssp.hainan.gov.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
    'sec-ch-ua': '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'xzqhCode': '460000-000-000-000-000',
}

data = {
    'qrys': '{"serverType":"1","serviceSubType":"theme","theme":"085","dept":"","regionId":"HZ2881f4424539dd0142453c856b0025","taskType":"","isOnLine":"","taskName":"","pageNumber":1,"pageSize":1000,"mltaskname":""}'
}
result = []
response = requests.post('https://wssp.hainan.gov.cn/wssp3/matter/exempt/info', headers=headers, cookies=cookies,
                         data=data)
data = response.json()
for item in data['data']['shixiangList']:
    subdatas = item['subdatas']
    for subdata in subdatas:
        id = subdata['id']
        sourcekey = subdata['sourcekey']
        rowguid = subdata['rowguid']
        url = f'https://wssp.hainan.gov.cn/hnwt/handlingGuideline?id={id}&sourcekey={sourcekey}&rowguid={rowguid}&taskhandleitem=&deptId=&deptName=%E6%B5%B7%E5%8D%97%E7%9C%81'
        title = subdata['taskname']
        result.append({'title': title, 'url': url})
print(result)
