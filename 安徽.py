import requests
from DrissionPage._pages.session_page import SessionPage

cookies = {
    'JSESSIONID': '430EFBF42F2B82C7129B15F4293F0409RiVaLE',
    '__jsluid_s': 'd1095cf57d67595f51c8bfd325771d81',
    '_gscu_826589485': '53257786w00tsp87',
    '_gscbrs_826589485': '1',
    '_gscs_826589485': 't53264139orxjuh13|pv:5',
}

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Origin': 'https://www.ahzwfw.gov.cn',
    'Referer': 'https://www.ahzwfw.gov.cn/bog-bsdt/static/workProcess.html?subjecttype=P',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
  'currentPageNo': '1',
  'pageSize': '100',
  'ssqdZoneCode': '340000000000',
  'ztmb': '46',
  'ssqdTypeCode': '',
  'ssqdName': '',
  'isOnline': '',
  'allOnline': '',
  'iscsjtb': '',
  'serviceObject': 'P',
  'xzqhZj': '0',
  'isPage': '1'
}
page = SessionPage()
page.post('https://www.ahzwfw.gov.cn/bog-bsdt/implement/queryImplements.do', headers=headers, cookies=cookies, data=data)
data = page.response.json()
result = []
for item in data['data']['rows']:
    url = f'https://www.ahzwfw.gov.cn/bog-bsdt/static/workProcess/components/applicationMaterial.html?ssqdId={item['id']}&ssqdCode={item['ssqdCode']}&typeSipe=nameSkip'
    result.append(url)
print(result)

