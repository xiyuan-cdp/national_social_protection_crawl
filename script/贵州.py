import requests
import tls_client

url = "https://zwfw.guizhou.gov.cn/ytbase/system/?yt_out_lay=1&ClassName=ZnzwSvr.page.QltAction.GetQltFolderList&ispages=1&isqueryxz=1&item_name=&org_code=1170934890500804468&type=&page=1&PageSize=1000"

payload = {}
headers = {
    'priority': 'u=1, i',
    'x-requested-with': 'XMLHttpRequest',
    'Cookie': 'ASP.NET_SessionId=hghwlaqqlanmhl55metcba45; Ytian_CK=browse_guid=C867459A0A94C38D22F6A5945098866A10D4470C9FC830E105EB376413F0A45F0A2CD2D664319D29&browse_guid_login=EA4C12357EB2F4F5AE4AFDFA8009BF980F05F91A9C04FFB0A89FBA30D14687111E8ED13165ED1F72E0AD14F3ED1F583CDEFD4BF74628FB982AD7EF67350F9380E0D461685FA1E3C021DC41EBFDB92F938D0EEE742401E6C12E143D083BD742ECC98F69083CF223F0&oauth_info=27145B50B21BD935C2BEF7193EC329D0289E1A69593D6475D4A42F586B7A5B33BA5FDB028E2CBD51E3BB43A68DF0756477890CA29E816F6D9A414C850B654958AA4D97ECC6134D1A19BF229A171786CF5E9508B343F32AE38551CF6A14AA73187120E26FFB4BD9F2313DA321273550FCA06C6E514534AD91F30BC0E5A89D6135E827A00A794F81713BFC6E031B97D465F3B8D0C62CEFC7E3F4E4C55F9D2DF88CB1529793F47BE44400A2790116D8BEA823C8D45B5A5EDA1FE21208A80084F0F6E676B6EEB4A2FB81C613C7D2E3CCDDA4DC4A423182D472746956ECDC0A2AA4E89095B8BDFD0507E6D49142CF44CF1D35D4FA1876789F15DD563A573A21D7DE3EF5D7D51E625DA843B7C744317553DA5365C2B716A6A4E3815577BCD7FA2634307084EB09E78E197AA3C84299BC7DAB361ABE90DD809F4CD4548719795F65A785F04386BF06F7592022FBE6A0E23CE6518305E2C884C33F680DF3EFCE4A1D19DAC3C3FB48CE451B3D',
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleToiOiI5MGY2YWE4ZS02NGJiLTQwODctYTA5YS1iMDExOTg3ZTZkNjcifQ.0-xTK88iermPRuQKScuFtz25fQ7F91-ir29LLdU5puiJHHAM-Zut511SYlsOxsqN6JDl8M9eJyW6sloV_IoEEQ'
}
session = tls_client.Session(client_identifier="chrome_110", random_tls_extension_order=True)

response = session.get(url, headers=headers, data=payload)
data = response.json()
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
print(len(result))
