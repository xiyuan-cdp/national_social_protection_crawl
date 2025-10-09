import requests

cookies = {
    'SESSION': '6946159d-eed8-4d5a-aa7a-624c2896878c',
    'WT-group10-1': 'ac12dc688a73c90e0050',
    'wondersLog_zwdt_G_D_I': '04fd44b43f759f84097b6211fb2589d6-9781',
    'WT-group10': 'AF/OEwjgEqz86+9TzMYvNw$$',
    'wondersLog_zwdt_sdk': '%7B%22persistedTime%22%3A1752053272401%2C%22updatedTime%22%3A1753674170590%2C%22sessionStartTime%22%3A1753674170589%2C%22sessionReferrer%22%3A%22https%3A%2F%2Fzwdt.sh.gov.cn%2FgovPortals%2FlegalPerson%2Fgroup%3Fcode%3D217%22%2C%22deviceId%22%3A%2204fd44b43f759f84097b6211fb2589d6-9781%22%2C%22LASTEVENT%22%3A%7B%22eventId%22%3A%22wondersLog_pv%22%2C%22time%22%3A1753674170590%7D%2C%22sessionUuid%22%3A5994632004900344%2C%22costTime%22%3A%7B%22wondersLog_unload%22%3A1753674170590%7D%7D',
    'ariauseGraymode': 'false',
    'WT-virt10': 'ac12dc6b7fee218a1b63',
    'arialoadData': 'true',
    'ariaappid': 'be30ca125d0f542b56e3f2cd45359459',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://zwdt.sh.gov.cn',
    'Referer': 'https://zwdt.sh.gov.cn/govPortals/legalPerson/group?code=217',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def get_list():
    data = {
        'pageNumber': '1',
        'pageSize': '1000',
        'itemType': '',
        'orgCode': '',
        'stRegion': 'SH00SH',
        'category': '217',
        'gfType': '\u6CD5\u4EBA',
        'stNet': '',
        'nmErrand': '',
        'sort': '',
        'feature': '',
        'stKeyword': '',
        'stIsShow': 'Y'
    }

    response = requests.post('https://zwdt.sh.gov.cn/govPortals/person.do', headers=headers, cookies=cookies, data=data)
    data = response.json()
    urls = []
    for data in data['itemList'].values():
        for item in data:
            print(item['stId'])
            url = get_detail(item['stId'])
            urls.append(url)
    return urls


def get_detail(stId):
    import requests

    data = {
        'stId': stId
    }

    response = requests.post('https://zwdt.sh.gov.cn/govPortals/item/getFwznWithByItemId.do', headers=headers,
                             cookies=cookies, data=data)
    ST_ID = response.json()[0]['item']['ST_ID']
    return 'https://zwdt.sh.gov.cn/govPortals/bsfw/item/' + ST_ID


result = get_list()
print(result)
