import requests
from DrissionPage._pages.session_page import SessionPage

cookies = {
    'JSESSIONID': 'A76266393F184F5A28C2B64C6FD544E9',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://www.jxzwfww.gov.cn/jxzw/grbs/gotoRight.do?webId=360000000000&orgId=&name=&themeId=6EE82C5B514845FEB9025601CD56E877&pageno=2&wid=1',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def get_data(pageno: str, urls: list):
    params = (
        ('webId', '360000000000'),
        ('orgId', ''),
        ('name', ''),
        ('themeId', '6EE82C5B514845FEB9025601CD56E877'),
        ('pageno', pageno),
        ('wid', '1'),
    )
    page = SessionPage()
    page.get('https://www.jxzwfww.gov.cn/jxzw/grbs/gotoRight.do', headers=headers, params=params,
             cookies=cookies)
    for tab in page.eles('.bsznbut'):
        id = tab.attr('onclick')[9:30]
        url = f'https://www.jxzwfww.gov.cn/jxzw/bszn/index.do?itemCode={id}&webId=1'
        urls.append(url)
        print(url)



result = []
for i in range(1, 10):
    get_data(str(i), result)
print(result)
