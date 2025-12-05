import requests

cookies = {
    'aisteUv': '17520527456831856282610',
    'aisiteJsSessionId': '1753434139966855123433',
    'SESSION': 'YTZjNjk3NGUtZTNiMC00NmVkLTlmOTUtMDFiN2I5MTE3Mjc4',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://zwfw.gxzf.gov.cn',
    'Referer': 'https://zwfw.gxzf.gov.cn/eportal/ui?pageId=162204b6fb7a443999213a8d31d7290e',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'request-by': 'ajax-request-tag',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = (
    ('pageId', '162204b6fb7a443999213a8d31d7290e'),
    ('moduleId', '8fed0735e1c14a47a68e7d12b9143831'),
    ('portal.url', '/portlet/officeServicePortlet/queryMainItemList'),
)


def get_list() -> list:
    current = 1
    urls = []
    while True:
        data = {
            'current': str(current),
            'categoryId': 'd7e4a549e616455b9245af439e0d67f0',
            'itemType': '',
            'regionCode': '3',
            'onlineHandle': '',
            'onlineSubscribe': ''
        }
        current += 1
        response = requests.post('https://zwfw.gxzf.gov.cn/eportal/ui', headers=headers, params=params, cookies=cookies,
                                 data=data)
        json = response.json()
        result = []
        if 'itemTreeNode' not in json['data']:
            break
        for item in json['data']['itemTreeNode']:
            if item['children']:
                for child in item['children']:
                    if child['children']:
                        for sub_child in child['children']:
                            obj_ = sub_child['obj']
                            if obj_['isExternalLink'] == 0:
                                url = f'https://zwfw.gxzf.gov.cn/eportal/ui?pageId=d0349fe94d1c4d139b006db643fb9e52&itemDetailId={obj_["id"]}'
                                result.append({"url": url, "title": obj_['itemName']})
                            if obj_['isExternalLink'] == 1:
                                url = obj_['externalLinkUrl']
                                result.append({"url": url, "title": obj_['itemName']})
                    else:
                        obj_ = child['obj']
                        if obj_['isExternalLink'] == 0:
                            url = f'https://zwfw.gxzf.gov.cn/eportal/ui?pageId=d0349fe94d1c4d139b006db643fb9e52&itemDetailId={obj_["id"]}'
                            result.append({"url": url, "title": obj_['itemName']})
                        if obj_['isExternalLink'] == 1:
                            url = obj_['externalLinkUrl']
                            result.append({"url": url, "title": obj_['itemName']})
            else:
                obj_ = item['obj']
                if obj_['isExternalLink'] == 0:
                    url = f'https://zwfw.gxzf.gov.cn/eportal/ui?pageId=d0349fe94d1c4d139b006db643fb9e52&itemDetailId={obj_["id"]}'
                    result.append({"url": url, "title": obj_['itemName']})
                if obj_['isExternalLink'] == 1:
                    url = obj_['externalLinkUrl']
                    result.append({"url": url, "title": obj_['itemName']})
        # print(result)
        urls.extend(result)
    return urls


result = get_list()
print(result)
print(len(result))
