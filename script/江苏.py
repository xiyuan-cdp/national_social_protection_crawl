import requests

cookies = {
    'JSESSIONID': 'DF3630C4DB2555B597E7ABEA409A17FA',
    'jisCUSSESSIONID': '3d67907d-32d3-4754-b79a-cd86b18c83f9',
    'SERVERID': '8839d5867daad807ccbd8af3921c49d2|1764728457|1764728319',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ru;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.jszwfw.gov.cn',
    'Referer': 'https://www.jszwfw.gov.cn/jszwfw/bscx/itemlist/gr_index.do?webId=1&themid=allzt&deptid=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}



def get_data(pageNo):
    data = {
        'webId': '1',
        'themid': '085',
        'deptid': '',
        'word': '',
        'pageno': str(pageNo),
        'handlearea': '',
        'isOnline': '',
        'qlKind': '',
        'fwdx': '0'
    }

    response = requests.post('https://www.jszwfw.gov.cn/jszwfw/bscx/itemlist/grshowtype.do', headers=headers,
                             cookies=cookies, data=data)
    data = response.json()
    pageSize = data['params']['pagenum']
    for item in data['params']['list']:
        sonList = item['sonList']
        for son in sonList:
            ywcode = son['ywcode']
            task_type = son['task_type']
            task_code = son['task_code']
            title = son['task_name']
            url = f'https://www.jszwfw.gov.cn/jszwfw/bscx/itemlist/bszn.do?webId=1&iddept_yw_inf={ywcode}&ql_kind={task_type}&iddept_ql_inf={task_code}'
            result.append({"url": url, "title": title})
            if 'sonList' in son and son['sonList']:
                for son1 in son['sonList']:
                    ywcode = son1['ywcode']
                    task_type = son1['task_type']
                    task_code = son1['task_code']
                    title = son1['task_name']
                    url = f'https://www.jszwfw.gov.cn/jszwfw/bscx/itemlist/bszn.do?webId=1&iddept_yw_inf={ywcode}&ql_kind={task_type}&iddept_ql_inf={task_code}'
                    result.append({"url": url, "title": title})
    if pageNo < pageSize:
        get_data(pageNo + 1)



result = []
get_data(1)
print(result)
