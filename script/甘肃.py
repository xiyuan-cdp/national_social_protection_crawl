import re

import requests
from DrissionPage._pages.session_page import SessionPage

cookies = {
    'CUSSESSIONID': 'NTAyMmI3NTgtODEyYi00OTdkLWI0OTItZTgzMjAwNzc2M2Vl',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://zwfw.gansu.gov.cn/szgs/sxcx/personal/theme/showIndex.do',
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
    ('gerenthemeId', '085'),
    ('deptCode', ''),
    ('isonline', ''),
    ('keyword', ''),
    ('number', '1'),
    ('numOfOnePage', '1000'),
    ('typeId', ''),
    ('areaCode', '620000000000'),
    ('_', '1753426958366'),
)
page = SessionPage()
page.get('https://zwfw.gansu.gov.cn/szgs/sxcx/personal/item/showdown.do', headers=headers, params=params,
         cookies=cookies)
result = []
for item in page.eles('办事指南'):
    onclick = item.attr('onclick')
    if onclick:
        taskCode = re.search("showBanshizhinan\('(.*?)','", onclick).group(1)
        taskHandleItem = re.search("','(.*?)'\)", onclick).group(1)
        url = f'https://zwfw.gansu.gov.cn/szgs/bszn/index.do?taskCode={taskCode}&taskHandleItem={taskHandleItem}'
        result.append(url)
print(result)