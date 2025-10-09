import requests
from DrissionPage._pages.session_page import SessionPage

cookies = {
    '__jsluid_s': '21ec712f08f70fa2461eb5e535f87060',
    '_abfpc': '6b097318379ff3e83a14ea5e7ec16020419120b1_2.0',
    'insert_cookie': '35926656',
    '_yfx_session_sdzc': '%7B%22_yfx_firsttime%22%3A%221752053218265%22%2C%22_yfx_lasttime%22%3A%221753673445120%22%2C%22_yfx_visittime%22%3A%221753673445120%22%2C%22_yfx_lastvisittime%22%3A%221753673466966%22%2C%22_yfx_domidgroup%22%3A%221753673445120%22%2C%22_yfx_domallsize%22%3A%22100%22%2C%22_yfx_cookie%22%3A%2220250709172658267115924483525016%22%2C%22_yfx_returncount%22%3A%221%22%7D',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://banshi.beijing.gov.cn/pubtask/grfw.html',
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
    ('serverType', '1001'),
    ('locationCode', '110000000000'),
    ('localType', '0'),
    ('businessType', ''),
    ('topicType', '085'),
    ('taskName', ''),
    ('deptCode', ''),
    ('taskType', ''),
    ('pageNum', '1'),
)

result = []
page = SessionPage()
page.get('https://banshi.beijing.gov.cn/guideservice/pubtask/getTaskList', headers=headers, params=params,
         cookies=cookies)
data = page.response.json()
for item in data['data']['list']:
    url = 'https://banshi.beijing.gov.cn'+item['taskUrl']
    result.append(url)
print(result)
