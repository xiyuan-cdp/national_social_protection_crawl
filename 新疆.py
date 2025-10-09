import requests
from DrissionPage._pages.session_page import SessionPage

cookies = {
    'areacode11': '650000000000',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://zwfw.xinjiang.gov.cn',
    'Referer': 'https://zwfw.xinjiang.gov.cn/jiopweb/HotServicesLevel2Page?bannerType=personal&areaCode=650000000000&labelSign=grfwsb',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'access-token': '0',
    'gray-version': '2.5.0-beta',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'districtCode': '650000000000',
    'serviceObj': 'personal'
}
page = SessionPage()
page.post('https://zwfw.xinjiang.gov.cn/api-gateway/jpaas-jiop-web-server/interface/label/findByDistrictCode',
          headers=headers, cookies=cookies, data=data)

data = page.response.json()
result = []
for label in data['data']['labelList']:
    for child in label['children']:
        if child['labelSign'] == 'grfwsb':
            print(child['labelName'])
            for item in child['relatedItemList']:
                # print(item)
                url = f'https://zwfw.xinjiang.gov.cn/jiopweb/guideSimple?itemId={item["iid"]}&bannerType=personal&areaCode={item['districtId']}'
                # print(url)
                result.append(url)
print(result)

# print(data)
