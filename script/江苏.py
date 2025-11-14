import requests
from DrissionPage._elements.session_element import make_session_ele
from DrissionPage._pages.session_page import SessionPage

headers = {
    'Referer': 'https://www.jszwfw.gov.cn/col/col172800/index.html',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def get_data(urls):
    response = requests.get('https://www.jszwfw.gov.cn/col/col172800/index.html', headers=headers)
    page = make_session_ele(response.text)
    for tab in page.eles('@mlbm'):
        catalog = tab.attr('mlbm')
        print(catalog)
        get_detail(catalog, '1', urls)
        # print(tab.text)


def get_detail(catalog, webId, urls: list):
    cookies = {
        'JSESSIONID': '8649B6479FAFD21FE275DAD151E5A75F',
        'jisCUSSESSIONID': '44a1f463-09a2-4638-be99-fcf2c4be40f1',
        'SERVERID': '8839d5867daad807ccbd8af3921c49d2|1753235547|1753235547',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Referer': 'https://www.jszwfw.gov.cn/col/col172800/index.html',
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
        ('catalog', catalog),
        ('webId', webId),
    )
    page = SessionPage()
    page.get('https://www.jszwfw.gov.cn/jszwfw/rmfw/getArea.do', headers=headers, params=params,
             cookies=cookies)
    data = page.response.json()
    if 'sonArray' not in data['params'] or not data['params']['sonArray']:
        return

    for son in data['params']['sonArray']:
        webid_ = son['webid']
        temp: list = get_url(catalog, webid_)
        urls.extend(temp)
        return get_detail(catalog, webid_, urls)
        # print(webid_)
    # print(data)


def get_url(catalog, webId):
    cookies = {
        'JSESSIONID': '8649B6479FAFD21FE275DAD151E5A75F',
        'jisCUSSESSIONID': '44a1f463-09a2-4638-be99-fcf2c4be40f1',
        'SERVERID': 'ed5c37cd37e9a84849acc7836050b7f7|1753239418|1753239394',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Referer': 'https://www.jszwfw.gov.cn/col/col172800/index.html',
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
        ('catalog', catalog),
        ('webId', webId),
    )
    page = SessionPage()
    page.get('https://www.jszwfw.gov.cn/jszwfw/rmfw/getYwInfo.do', headers=headers, params=params,
             cookies=cookies)
    data = page.response.json()
    urls = []

    for key, value in data['params'].items():
        urls.append({"url": key, "title": value})

    # print(urls)
    return urls


result = []
get_data(result)
print(result)
