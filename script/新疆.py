import requests
from DrissionPage._pages.session_page import SessionPage

import requests

url = "https://zwfw.xinjiang.gov.cn/api-gateway/jpaas-jiop-web-server/front/matter/new-find-mightr-list"

payload = 'itemName=&districtId=650000000000&itemTypeIds=&taskServiceObj=personal&pageNo=1&pageSize=100&themeIds=EFV85TxUu8nnVvRTkTBSm'
headers = {
    'access-token': '0',
    'gray-version': '2.5.0-beta',
    'Cookie': 'areacode11=650000000000',
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleToiOiI5MGY2YWE4ZS02NGJiLTQwODctYTA5YS1iMDExOTg3ZTZkNjcifQ.0-xTK88iermPRuQKScuFtz25fQ7F91-ir29LLdU5puiJHHAM-Zut511SYlsOxsqN6JDl8M9eJyW6sloV_IoEEQ',
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

data = response.json()
result = []
for matter in data['data']['matterList']:
    for child in matter['childItemList']:
        iid = child['iid']
        districtId = child['districtId']
        title = child['itemName']
        url = f'https://zwfw.xinjiang.gov.cn/jiopweb/guideSimple?itemId={iid}&bannerType=personal&areaCode={districtId}'
        result.append({"url": url, "title": title})
print(result)

# print(data)
