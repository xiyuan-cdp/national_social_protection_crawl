import requests

cookies = {
    '3460F95863F1803830E36F029BFD21EC': '96f86386-ef67-4451-8f46-549876369023',
    'area_code': '439900000000',
    'JSESSIONID': '88FCBBE350646DD9A9D194F79F540077',
    'area_name': '%u7701%u672C%u7EA7',
    'tjcookie': '',
    'redirect_urldl': '',
    'areaid': '1',
}

headers = {
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Origin': 'https://zwfw-new.hunan.gov.cn',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ru;q=0.5',
    'sec-ch-ua': '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = (
    ('action', 'toCatalogHttpPost'),
    ('url', '/unifyTaskToWt/getUnifyTaskByPage?page=1&rows=1000'),
    ('data', '{"type":"1","unifyName":"","ztfl":"085","areaCode":"430000000000"}'),
)

result = []
response = requests.post('https://zwfw-new.hunan.gov.cn/hnywtb/anony', headers=headers, params=params, cookies=cookies)
data = response.json()
for content in data['data']['contents']:
    rightsCode = content['rightsCode']
    ywCode = content['ywCode']
    unifyId = content['unifyId']
    title = content['unifyName']
    url = f'https://zwfw-new.hunan.gov.cn/hnywtb/service/guide.html?id={unifyId}&type=gr&rightsCode={rightsCode}&ywCode={ywCode}'
    result.append({'title': title, 'url': url})
print(result)
