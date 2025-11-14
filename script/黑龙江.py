import json

import tls_client

cookies = {
    '_ud_': '259badc67e4945ada2fa6d411fde5391',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Origin': 'https://www.zwfw.hlj.gov.cn',
    'Referer': 'https://www.zwfw.hlj.gov.cn/zhcx/service/personal/subject?areaCode=230000000000',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

session = tls_client.Session(client_identifier="chrome_110", random_tls_extension_order=True)


def get_data(pageNo):
    params = {"districtcode": "230000000000", "groupId": "", "taskServiceObj": "01", "pageNo": pageNo, "pageSize": "10",
              "themeIds": "085", "applicableGroupIds": "", "itemUserType": "", "itemTypeIds": "", "pcIsonline": "",
              "creditpromisetype": "", "appIsonline": "", "itemName": "", "limitSceneNum": "", "handleArea": "",
              "projectType": "", "isFee": "", "ggfwOrXzxk": ""}
    data = {
        'header': '{}',
        'version': '1.0',
        'charset': 'UTF-8',
        'origin': '1',
        'timestamp': '1753177575734',
        'interface_id': 'hljzhcxsxlbnew',
        'app_id': 'hljzhcx',
        'biz_content': json.dumps(params),
    }
    response = session.post('https://www.zwfw.hlj.gov.cn/jpaas-jags-server/interface/createsign', headers=headers,
                            cookies=cookies, data=data)
    response = json.loads(response.text)
    sign = response['data']['sign']

    data['sign'] = sign
    response = session.post('https://www.zwfw.hlj.gov.cn/jpaas-jags-server/interface/gateway', headers=headers,
                            cookies=cookies, data=data)
    data = json.loads(response.text)
    data = json.loads(data['data'])
    try:
        matterList = data['data']['matterList']
    except KeyError:
        return []
    urls = []
    for matter in matterList:
        url = f'https://www.zwfw.hlj.gov.cn/zhcx/bszn?syncItemId={matter['syncItemId']}&areaCode=230000000000'
        title = matter['itemName']
        urls.append({"url": url, "title": title})
        print(url)
    return urls


def get_list():
    urls = []
    for i in range(1, 100):
        url: list = get_data(i)
        urls.extend(url)
        if not url:
            break
    print(urls)
    return urls


result = get_list()
print(result)
