import tls_client

cookies = {
    'ZWFWW-group-443': '36169.55913.7938.0000',
    '_trs_uv': 'mcv9lquh_2312_84nw',
    '_trs_ua_s_1': 'mcvmutml_2312_4r3a',
}

session = tls_client.Session(client_identifier="chrome_120", random_tls_extension_order=False)
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://www.lnzwfw.gov.cn/wsbs/zrr/',
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
    params = (
        ('pageNum', '1'),
        ('pageSize', '500'),
        ('rightclassGerenzt', '085'),
    )

    response = session.get('https://www.lnzwfw.gov.cn/matter/Dept/findByRightclassGerenzt', headers=headers,
                           params=params, cookies=cookies)
    urls = []
    for data in response.json()['result']['list']:
        print(data)
        ql_kind = data['ql_kind']
        taskcode = data['taskcode']
        url = get_detail(ql_kind, taskcode)
        urls.extend(url)
    return urls


#

def get_detail(ql_kind, catalogCode):
    params = (
        ('qlObject', ql_kind),
        ('catalogCode', catalogCode),
    )

    response = session.get('https://www.lnzwfw.gov.cn/matter/Dept/findByCatalogCode', headers=headers, params=params,
                           cookies=cookies)
    return ['https://center.lnzwfw.gov.cn/api/web/matter/getContent?id=' + data['item_id'] for data in
            response.json()['result']]


result = get_list()
print(result)
