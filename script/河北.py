import json

import requests


def get_list(pageNum: int):
    cookies = {
        'JSESSIONID': 'D3474B895DC279F0DCE7AB2B715CE562',
        'SF_cookie_14': '11383299',
        'SF_cookie_28': '37132023',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://www.hbzwfw.gov.cn',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://www.hbzwfw.gov.cn/hbzw/foursxcx/itemList/gr_index.do?webId=1&zt=16&deptid=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'webId': '1',
        'zt': '16',
        'isonline': '',
        'isBasis': '0',
        'pageNum': str(pageNum),
        'word': ''
    }
    response = requests.post('http://www.hbzwfw.gov.cn/hbzw/foursxcx/itemList/getZtGrShowList.do', headers=headers,
                             cookies=cookies, data=data, verify=False)
    data = json.loads(response.text)
    data = json.loads(data['params']['data'])
    for item in data['subList']:
        if 'itemList' not in item:
            continue
        for i in item['itemList']:
            url = "http://www.hbzwfw.gov.cn/hbzw/bszn/info/simple.do?itemId=" + i['itemId']
            title = i['taskName']
            # print(url)
            result.append({"url": url, "title": title})
    total = data['pages']['pageSum']
    if pageNum < total:
        get_list(pageNum + 1)


result = []
get_list(1)
print(result)
