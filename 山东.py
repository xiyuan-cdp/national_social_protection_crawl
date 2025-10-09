import requests
from DrissionPage._pages.session_page import SessionPage

cookies = {
    'zh_choose_undefined': 's',
    'Hm_lvt_3147c565b4637bb1f8c07a562a3c6cb7': '1752051423,1753352234',
    'HMACCOUNT': 'A89E656BF367E71C',
    'arialoadData': 'true',
    'Hm_lpvt_3147c565b4637bb1f8c07a562a3c6cb7': '1753352649',
    'ariauseGraymode': 'false',
    'ariaappid': 'f25ef833fd7360958941e3b86774b2ba',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
}
page = SessionPage()
page.get('http://www.shandong.gov.cn/api-gateway/jpaas-jiq-web-sdywtb/front/item/gr_index', headers=headers,
         cookies=cookies, verify=False)
result = []
for tab in page.ele('.grfw_detail grfw_detail1').eles('t:a'):
    url = tab.link
    if url:
        result.append(url)
print(result)
