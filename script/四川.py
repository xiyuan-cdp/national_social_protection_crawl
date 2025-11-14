import re

import requests
from DrissionPage._pages.session_page import SessionPage

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://www.sczwfw.gov.cn/jiq/front/item/gr_index?areaCode=510000000000',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def get_list():
    pageno = 1
    urls = []
    while True:
        params = (
            ('dxType', '1002'),
            ('areaCode', '510000000000'),
            ('theme', '085'),
            ('deptCode', ''),
            ('isonline', ''),
            ('searchtext', ''),
            ('pageno', pageno),
            ('type', '1'),
            ('limitSceneNum', ''),
            ('taskType', ''),
        )
        pageno += 1
        page = SessionPage()

        page.get('https://www.sczwfw.gov.cn/jiq/interface/item/tags', headers=headers, params=params)
        for item in page.eles('办事指南'):
            title = item.parent().parent().ele(".sx_title").text
            url = re.search("ywblurl\('(.*?)'\)", item.attr('onclick')).group(1)
            # print(url)
            urls.append({"url": url, "title": title})
        # 程序出口，终止死循环条件
        if not page.ele('办事指南'):
            break
    return urls


result = get_list()
print(result)
