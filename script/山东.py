import requests
from DrissionPage._elements.session_element import make_session_ele
from DrissionPage._pages.session_page import SessionPage

import requests

cookies = {
    'wondersLog_sdywtb_sdk': '%7B%22persistedTime%22%3A1763089754782%2C%22updatedTime%22%3A1763089755173%2C%22sessionStartTime%22%3A1763089755172%2C%22sessionReferrer%22%3A%22%22%2C%22deviceId%22%3A%22bc484e9499ad67d9788b81f949fe36a2-5347%22%2C%22LASTEVENT%22%3A%7B%22eventId%22%3A%22wondersLog_pv%22%2C%22time%22%3A1763089755173%7D%2C%22sessionUuid%22%3A5257746321061587%2C%22costTime%22%3A%7B%7D%7D',
    'zh_choose_undefined': 's',
    'Hm_lvt_3147c565b4637bb1f8c07a562a3c6cb7': '1763089756,1764730477',
    'HMACCOUNT': 'A89E656BF367E71C',
    'arialoadData': 'true',
    'ariauseGraymode': 'false',
    'Hm_lpvt_3147c565b4637bb1f8c07a562a3c6cb7': '1764730480',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ru;q=0.5',
    'Connection': 'keep-alive',
    'Referer': 'http://www.shandong.gov.cn/api-gateway/jpaas-jiq-web-sdywtb/front/item/gr_index',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
}


def get_data(pageNo):
    params = (
        ('pageNo', str(pageNo)),
        ('regionCode', '370000000000'),
        ('theme', '085'),
        ('taskType', 'ALL'),
        ('orginCode', ''),
        ('isonline', ''),
        ('keyword', ''),
    )

    response = requests.get(
        'http://www.shandong.gov.cn/api-gateway/jpaas-jiq-web-sdywtb/front/TagController/pThemeItem', headers=headers,
        params=params, cookies=cookies, verify=False)
    page = make_session_ele(response.text)
    for item in page.eles('.r2_tit iom2'):
        item = item.ele('t:a')
        url = item.attr('href')
        title = item.attr('title')
        result.append({'url': url, 'title': title})


if __name__ == '__main__':
    result = []
    for pageNo in range(1, 9):
        get_data(pageNo)
    print(result)