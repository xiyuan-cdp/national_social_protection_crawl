import requests
from DrissionPage._pages.session_page import SessionPage

cookies = {
    'TS0117ea39': '015400267628e829f995a0e746f279d8e3ed1e0c808961af38276734560bd7d6a993a37f899b3bd142ab603865d508a69d32462ae7',
    'JSESSIONID': 'A00205FCFE2DE22AEB989AC9F4182124',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://zwfw.nx.gov.cn/grztsx.jsp?wbtreeid=6259&searchtext=&ptypeId=2c9c80875cc848aa015cd2d455d903cd&ptypeCode=SB&mentype=0&wsbslistCURURI=71708B1A8CF4AF520C36BDC28827E310&wsbslistKEYTYPES=12%2C12&actiontype=PrevPage&wsbslistORDER=ASC&wsbslistORDERKEY=baseprocode&wsbslistCountNo=20&wsbslistNOWPAGE=&wsbslistPAGE=20&wsbslistrowCount=44',
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
    ('wbtreeid', '6259'),
    ('searchtext', ''),
    ('ptypeId', '2c9c80875cc848aa015cd2d455d903cd'),
    ('ptypeCode', 'SB'),
    ('mentype', '0'),
    ('wsbslistCURURI', '71708B1A8CF4AF520C36BDC28827E310'),
    ('wsbslistKEYTYPES', '12,12'),
    ('actiontype', 'NextPage'),
    ('wsbslistORDER', 'ASC'),
    ('wsbslistORDERKEY', 'baseprocode'),
    ('wsbslistCountNo', '1000'),
    ('wsbslistNOWPAGE', ''),
    ('wsbslistPAGE', '0'),
    ('wsbslistrowCount', '44'),
)
page = SessionPage()
page.get('https://zwfw.nx.gov.cn/grztsx.jsp', headers=headers, params=params, cookies=cookies)
result = []
for item in page.eles('办事指南'):
    url = item.link
    result.append(url)
    print(url)
print(result)