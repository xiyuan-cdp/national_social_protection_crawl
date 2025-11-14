import requests
from DrissionPage._pages.session_page import SessionPage

cookies = {
    'Ytian_CK': 'browse_guid=C867459A0A94C38D22F6A5945098866A10D4470C9FC830E105EB376413F0A45F0A2CD2D664319D29&browse_guid_login=EA4C12357EB2F4F5AE4AFDFA8009BF980F05F91A9C04FFB0A89FBA30D14687111E8ED13165ED1F72E0AD14F3ED1F583CDEFD4BF74628FB982AD7EF67350F9380E0D461685FA1E3C021DC41EBFDB92F938D0EEE742401E6C12E143D083BD742ECC98F69083CF223F0&oauth_info=FA66808D506CDEFEAA8D6DEE09B53E9EC46B34FDAC39B280FBEDA378F61331E49B80E3FBD899A13E30C74A09FF65D34934395D52DF356F983AC54705FB021795A6E9434949CC639E4316CEC0588E48ABFFEE8B24F62B3D38B63EF2C90FAA39EDD64EC925F1973B54FB6BF292199AAF06F874DEBCF03ABDC95D8F3110BA29428245709FBB02B8586E8B74565201B0FA346F8A4F6E0082D89A4062D2918E23ED723B7A2448012C1A42DB20947BA8C47E9E49D9B8AE5E211D120CF61CF783128103A318019CA8B25D9776DD9BCE9417489ED0A4AF083EF5A898B29916985197C73583A1CE166971F98F',
    'MM_mq4qQammP3BA4': 'ZDAzMTIwY2ZjOWJjMmUzMetM8lH1k9CzMFe-nUFxJuevlVJJBzh1HSpeG1Qjo55CiBQkfbl41h9UuC3ET_BwUg',
    'ASP.NET_SessionId': '5fwsa055s4xjcq55inec4055',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'priority': 'u=1, i',
    'referer': 'https://zwfw.guizhou.gov.cn/nv/grbs/520000/index.html?areacode=520000',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
}

params = (
    ('yt_out_lay', '1'),
    ('ClassName', 'ZnzwSvr.page.QltAction.GetQltFolderList'),
    ('DB_Conn', 'ZWBSDB'),
    ('area_code', '520000'),
    ('item_name', ''),
    ('PageSize', '1000'),
    ('page', '1'),
    ('service_object', '0'),
    ('org_code', ''),
    ('apply_times', ''),
    ('item_zt_code', '001001010'),
    ('item_rssj_code', ''),
    ('item_tddx_code', ''),
    ('hycode', ''),
    ('item_zzfl_code', ''),
    ('item_jyhd_code', ''),
    ('type', ''),
    ('isqueryxz', '1'),
    ('ISselfHelp', ''),
)
page = SessionPage()

page.get('https://zwfw.guizhou.gov.cn/ytbase/system/default.aspx', headers=headers, params=params, cookies=cookies)
data = page.response.json()
result = []
for item in data['data']['Data']:
    if 'QltList' in item and item['QltList']:
        for i in item['QltList']:
            url = f"https://zwfw.guizhou.gov.cn/bsznindex.do?otheritemcode={i['ITEM_CODE']}&orgcode={i['Org_code']}&areacode={i['Region_code']}"
            result.append({"url": url, "title": i['NAME']})
    if 'ChiltList' in item and item['ChiltList']:
        for j in item['ChiltList']:
            for i in j['QltList']:
                url = f"https://zwfw.guizhou.gov.cn/bsznindex.do?otheritemcode={i['ITEM_CODE']}&orgcode={i['Org_code']}&areacode={i['Region_code']}"
                result.append({"url": url, "title": i['NAME']})

print(result)
