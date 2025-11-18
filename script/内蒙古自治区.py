import requests
import tls_client

cookies = {
    'UM_distinctid': '197ee78b61a581-0ddee9603b691f-4c657b58-1fa400-197ee78b61b1a4e',
    'egueayg': 'HD_10.12.24.201_4430',
    'CNZZDATA1278634450': '2107205610-1752052578-%7C1753428547',
    '_yfx_session_10000002': '%7B%22_yfx_firsttime%22%3A%221752052579049%22%2C%22_yfx_lasttime%22%3A%221753428547542%22%2C%22_yfx_visittime%22%3A%221753428547542%22%2C%22_yfx_domidgroup%22%3A%221753428547542%22%2C%22_yfx_domallsize%22%3A%22100%22%2C%22_yfx_cookie%22%3A%2220250709171619051367524048593888%22%2C%22_yfx_returncount%22%3A%221%22%7D',
    'guidesStatus': 'off',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://zwfw.nmg.gov.cn/handle_affairs?regionCode=150000&workType=personal&record=istrue',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = (
    ('CurrentPage', '1'),
    ('PageSize', '1000'),
    ('workType', 'personal'),
    ('RegionCode', '150000'),
    ('OrgCode', ''),
    ('SubjectClassify', '0085'),
    ('ItemClassify', ''),
    ('ItemNameLike', ''),
    ('IsOnline', ''),
    ('ItemType', ''),
    ('PeopleClasssify', ''),
    ('LifeClasssify', ''),
    ('IsIntoHall', ''),
)
session = tls_client.Session(client_identifier="chrome_110", random_tls_extension_order=True)

response = session.get('https://zwfw.nmg.gov.cn/handle_affairs_serch_new', headers=headers, params=params,
                       cookies=cookies)
datas = response.json()
result = []
for data in datas['itemJsonDataList']:
    if data['SubFolder']:
        for sub_data in data['SubFolder']:
            if sub_data['ItemList']:
                for item in sub_data['ItemList']:
                    title = item['ItemName']
                    url = f"https://zwfw.nmg.gov.cn/handle_affairs_detail_simple?item_detail_id={item['ItemID']}&regionCode=150000&record=istrue"
                    result.append({"url": url, "title": title})
    if data['ItemList']:
        for item in data['ItemList']:
            title = item['ItemName']
            url = f"https://zwfw.nmg.gov.cn/handle_affairs_detail_simple?item_detail_id={item['ItemID']}&regionCode=150000&record=istrue"
            result.append({"url": url, "title": title})

print(len(result))
print(result)
