import requests
from DrissionPage._pages.session_page import SessionPage

cookies = {
    'yitihua20220424': '35130651',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://wssp.hainan.gov.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'xzqhCode': '460000-000-000-000-000',
}


def get_list() -> list:
    params = (
        ('topicCode', '1599182508237'),
    )
    page = SessionPage()
    page.get('https://wssp.hainan.gov.cn/wssp3/heatTheme/getHeatThemeList', headers=headers, params=params,
             cookies=cookies)
    data = page.response.json()
    resultList = data['data']['resultList']
    urls = []
    for result in resultList:
        if result['topicname'] == '社保卡':
            for sub in result['resultSubList']:
                id = sub['id']
                url: list = get_data(id)
                urls.extend(url)
    return urls


def get_data(topicid) -> list:
    params = (
        ('topicid', topicid),
    )
    page = SessionPage()
    page.get('https://wssp.hainan.gov.cn/wssp3/heatTheme/getHighlightArea', headers=headers,
             params=params, cookies=cookies)
    data = page.response.json()
    urls = []
    for result in data['data']['resultList']:
        if result['ishighlight'] == '1':
            deptid = result['deptid']
            url: list = get_url(topicid, deptid)
            urls.extend(url)
    return urls


def get_url(topicid, deptid) -> list:
    data = {
        'topicid': topicid,
        'xzqhid': deptid,
        'pageNum': '1',
        'pageSize': '100',
        'issub': '1'
    }
    page = SessionPage()
    page.post('https://wssp.hainan.gov.cn/wssp3/heatTheme/getMatterByIdAndCode', headers=headers,
              cookies=cookies, data=data)
    urls = []
    for item in page.response.json()['data']['resultList']:
        url = f'https://wssp.hainan.gov.cn/hnwt/handlingGuideline?id={item["id"]}&sourcekey={item["sourcekey"]}&rowguid={item["rowguid"]}'
        title = item['taskname']
        urls.append({"url": url, "title": title})
    return urls


result = get_list()
print(result)
