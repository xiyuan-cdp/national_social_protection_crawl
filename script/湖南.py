import re

from DrissionPage._pages.session_page import SessionPage

cookies = {
    '3460F95863F1803830E36F029BFD21EC': '96f86386-ef67-4451-8f46-549876369023',
    'area_code': '439900000000',
    'area_name': '%u7701%u672C%u7EA7',
    'tjcookie': '',
    'redirect_urldl': '',
    'areaid': '1',
    'JSESSIONID': '69BC17BBB4C75459EDDFD9496E3FF8D0',
    'word': '',
    'RUMS_SESSIONID': '2DC73950A0B44A5FC03DA589FF7193CD',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://zwfw-new.hunan.gov.cn/onething/service/index_ywtb.jsp?type=xndtgr&main=&areacode=439900000000',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = (
    ('approve_id', '9A3277DABA664158E053651515AC4C69'),
    ('type', 'xndtgr'),
    ('areacode', '439900000000'),
)
page = SessionPage()
page.get('https://zwfw-new.hunan.gov.cn/onething/service/serviceguidecklist.jsp', headers=headers, params=params,
         cookies=cookies)
areacode = page.ele('#areacode').text
webroot = page.ele('#webroot').text
dghy = ""
cscjwt = ""
type = 'xndtbm'
org_id = ""
result = []
for item in page.ele('.grssqk2-1-ul').eles('t:a'):
    data = item.attr('onclick')
    approve_id = re.search("to_approve_page\('(.*?)','xndtbm'", data).group(1)
    url = 'https://zwfw-new.hunan.gov.cn' + webroot + "/onething/service/serviceguideck.jsp?approve_id=" + approve_id + "&type=" + type + "&dghy=" + dghy + "&cscjwt=" + cscjwt + "&org_id=" + org_id + "&areacode=" + areacode + "&org_id=" + org_id
    result.append({'url': url, 'title': item.text})
print(result)
