import json

import requests
from DrissionPage._pages.session_page import SessionPage

cookies = {
    'JSESSIONID': 'A800AD51B46A07FCE89E117D79A98664',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'C-App-Id': 'GSP_APP_001',
    'C-Business-Id': '2025072511251988820001026232PC43',
    'C-Dynamic-Password-Foruser': 'false',
    'C-Tenancy-Id': '530000000000',
    'C-Timestamp': '20250725112519888',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://zwfw.yn.gov.cn',
    'Referer': 'https://zwfw.yn.gov.cn/portal/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def get_list():
    data = {
        "txnCommCom": {"txnIttChnlId": "C0071234567890987654321", "txnIttChnlCgyCode": "BC01C101", "tStsTraceId": "123",
                       "tRecInPage": 100, "tPageJump": 1},
        "txnBodyCom": {"name": "", "type": "FBM", "orgCode": "", "serviceObject": "0",
                       "typeId": "31a0fec90df8432a8471205e1188e2a5", "matterId": "", "strLevel": "1", "exeLevel": "",
                       "isAppoint": "", "isOnlinepay": "", "isLogistics": "", "regnCode": "530000000000",
                       "addrLvlCd": "1", "handleWay": "0"}}
    page = SessionPage()
    page.post('https://zwfw.yn.gov.cn/portal/gml/web10011', headers=headers, cookies=cookies, data=json.dumps(data))
    data = page.response.json()['C-Response-Body']
    data = json.loads(data)
    result = []
    for item in data['lIST2']:
        title = item['name']
        id_ = item['id']
        url: list = get_urls(id_)
        result.extend(url)
    return result


def get_urls(id) -> list:
    data = {
        "txnCommCom": {"txnIttChnlId": "C0071234567890987654321", "txnIttChnlCgyCode": "BC01C101", "tStsTraceId": "123",
                       "tRecInPage": 100, "tPageJump": 1},
        "txnBodyCom": {
            "regnCode": "530000000000",
            "orgCode": "",
            "typeId": "",
            "id": id,
            "strLevel": "2",
            "handleWay": "0",
            "serviceObject": "0",
            "tbrange": ""
        }}
    page = SessionPage()
    page.post('https://zwfw.yn.gov.cn/portal/gml/web10011', headers=headers, cookies=cookies, data=json.dumps(data))
    data = page.response.json()['C-Response-Body']
    data = json.loads(data)
    urls = []
    for item in data['lIST2']:
        url = f'https://zwfw.yn.gov.cn/portal/#/work-service/guide-detail?id={item['id']}&matterId={item['matterId']}'
        urls.append({"url": url, "title": item['name']})
    # print(urls)
    return urls


result = get_list()
print(result)
