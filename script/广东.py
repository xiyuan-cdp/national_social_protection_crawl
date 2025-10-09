import json

from DrissionPage._pages.session_page import SessionPage

cookies = {
    '_horizon_uid': 'd3adb2ef-91c3-413a-8173-dc98eae3acb2',
    '_horizon_sid': 'ab422db6-3e6f-4020-a8bf-c8992c6187a3',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://www.gdzwfw.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.gdzwfw.gov.cn/portal/v2/personal/theme?region=440000',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def get_list(city, urls):
    city_dict = get_city()
    code = city_dict.get(city)
    if code is None:
        raise Exception("city {} not exist".format(city))
    get_data(1, code, code, urls)


def get_data(PAGENO, city, area_code, urls=None):
    req = {
        "PAGENO": str(PAGENO),
        "PAGESIZE": 500,
        "TASK_TYPE": "",
        "DEPT_CODE": "",
        "AREA_CODE": area_code,
        "ISLOCALLEVEL": 0,
        "KEY_WORD": "",
        "TYPE": "001001010",
        "IS_ONLINE": "",
        "TASKTAG": 1,
        "LIMIT_SCENE_SUM": 0,
        "IS_ZERO_SECNE": ""
    }

    page = SessionPage()
    page.post('https://www.gdzwfw.gov.cn/portal/api/v2/solr/getCommonAuditItem', headers=headers, cookies=cookies,
              data=json.dumps(req))
    data = page.response.json()
    print(data)
    data = data['CUSTOM']
    for tab in data['AUDIT_ITEMLIST']:
        url = "https://www.gdzwfw.gov.cn/portal/v2/guide/" + tab['TASK_CODE']
        urls += [{"url": url, "title": tab['TASK_NAME']}]
        # print(data)
    page_info = data['PAGEINFO']
    if page_info['CURRENTPAGEINDEX'] * page_info['PAGESIZE'] < page_info['TOTALNUM']:
        get_data(PAGENO + 1, city, area_code, urls)


def get_city():
    cookies = {
        '_horizon_uid': 'd3adb2ef-91c3-413a-8173-dc98eae3acb2',
        '_horizon_sid': 'a694fd5f-c0c6-41ec-98c9-474d0856fd84',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.gdzwfw.gov.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://www.gdzwfw.gov.cn/portal/v2/personal/theme?region=440000',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'regCode': '440000'
    }
    page = SessionPage()

    page.post('https://www.gdzwfw.gov.cn/portal/api/v2/node/gdbsNav/current', headers=headers,
              cookies=cookies, data=data)
    data = page.response.json()
    citys = []
    for hall in data['hall']:
        city = {"city": hall['ORGNAME'],
                "code": hall['ORGAREACODE']}
        citys.append(city)
    city_dict = {}
    for hall in data['hall']:
        city_dict[hall['ORGNAME']] = hall['ORGAREACODE']

    return city_dict


result = []
get_list("东莞市", result)
print(result)
