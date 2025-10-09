import json

import requests
from DrissionPage._pages.session_page import SessionPage

cookies = {
    'SESSIONID': 'YWRkYWI0NGQtOGQ0YS00YTY0LWJmNGQtNjc1ZjFjMWEyMDZh',
    'Hm_lvt_2e78e4e6592603c96de5e3ada929877c': '1752051655,1753353743',
    'Hm_lpvt_2e78e4e6592603c96de5e3ada929877c': '1753353743',
    'HMACCOUNT': 'A89E656BF367E71C',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://zwfw.hubei.gov.cn',
    'Referer': 'http://zwfw.hubei.gov.cn/webview/fw/grfw.html?v=20211029',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'requestURL': 'http://zwfw.hubei.gov.cn/webview/fw/grfw.html?v=20211029',
}


def get_list():
    data = {
        'grade': '',
        'orgCode': '',
        'isOnline': '',
        'serviceGr': '1',
        'serviceFr': '',
        'subjectIdsGr': '085',
        'subjectIdsFr': '',
        'taskType': '',
        'regionCode': '420000000000',
        'areaGrade': '2',
        'currentPage': '1',
        'pageSize': '1000',
        'onlyLocalLevel': '1',
        'onlyGrfRSearch': '1'
    }

    page = SessionPage()
    page.post('http://zwfw.hubei.gov.cn/web/bszn/item_project', headers=headers, cookies=cookies, data=data,
              verify=False)
    data = page.response.json()
    urls = []
    for record in data['data']['records']:
        taskCode = record['TASKCODE']
        url: list = get_detail(taskCode)
        urls.extend(url)
        # print(url)
    return urls


def get_detail(taskCode):
    page = SessionPage()
    cookies = {
        'SESSIONID': 'YWRkYWI0NGQtOGQ0YS00YTY0LWJmNGQtNjc1ZjFjMWEyMDZh',
        'Hm_lvt_2e78e4e6592603c96de5e3ada929877c': '1752051655,1753353743',
        'HMACCOUNT': 'A89E656BF367E71C',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221983c08e587e87-06578553c9a0a1-4c657b58-2073600-1983c08e58827ed%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%221983c08e587e87-06578553c9a0a1-4c657b58-2073600-1983c08e58827ed%22%7D',
        'sajssdk_2015_cross_new_user': '1',
        'Hm_lpvt_2e78e4e6592603c96de5e3ada929877c': '1753353873',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://zwfw.hubei.gov.cn',
        'Referer': 'http://zwfw.hubei.gov.cn/webview/fw/grfw.html?v=20211029',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
        'requestURL': 'http://zwfw.hubei.gov.cn/webview/fw/grfw.html?v=20211029',
    }
    data = {
        'taskCode': taskCode
    }

    page.post('http://zwfw.hubei.gov.cn/web/tysl/ykypt/standard/transact/project/getActionByTaskCode',
              headers=headers, cookies=cookies, data=data, verify=False)
    actionCode = page.response.json()
    actionCode = actionCode['data']

    actionCodeList = json.loads(actionCode)
    actionCodeList = [item['actionCode'] for item in actionCodeList]
    codes = []
    for actionCode in actionCodeList:
        data = {
            'limit': '',
            'taskCode': taskCode,
            'transactName': '',
            'actionCode': actionCode
        }

        page.post('http://zwfw.hubei.gov.cn/web/tysl/ykypt/standard/item/transact/selectPageList',
                  headers=headers, cookies=cookies, data=data, verify=False)
        data = page.response.json()['data']
        data = json.loads(data)['data']
        code = ['http://zwfw.hubei.gov.cn/webview/bszn/bsznpage.html?transactCode=' + i['TaskCode'] for i in data]
        codes.extend(code)
    return codes



result = get_list()
print(result)
