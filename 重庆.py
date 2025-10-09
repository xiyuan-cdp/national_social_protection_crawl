import requests
import json
import tls_client

url = "https://cqykb.cq.gov.cn/pc/xindian/handle/getItemList"
params = (
    ('pageNum', '2'),
    ('pageSize', '10'),
    ('areaCode', '500000'),
    ('serviceObject', '1'),
    ('firstLevelCategoryId', '1'),
    ('secondLevelCategoryId', '085'),
    ('handleType', ''),
    ('limitSceneNum', ''),
    ('itemType', ''),
    ('keyWord', ''),
)

payload = ""
headers = {
    'Authorization': '',
    'Content-Type': 'application/json'
}
session = tls_client.Session(client_identifier="chrome_110", random_tls_extension_order=True)

response = session.get(url, headers=headers, data=payload, params=params)
result = []
for row in response.json()['rows']:
    url = f'https://zwykb.cq.gov.cn/v2/grbs/bszn.html?catalogId={row["catalogId"]}&transactCode='
    result.append(url)

print(result)

