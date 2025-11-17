import requests

cookies = {
    'cna': 'Nhv1IC4T5QICAf////8r5rvh',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22197ee60f5731d45-03243d8637340b-4c657b58-2073600-197ee60f5742609%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk3ZWU2MGY1NzMxZDQ1LTAzMjQzZDg2MzczNDBiLTRjNjU3YjU4LTIwNzM2MDAtMTk3ZWU2MGY1NzQyNjA5In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22197ee60f5731d45-03243d8637340b-4c657b58-2073600-197ee60f5742609%22%7D',
    'sensorsdata2015jssdksession': '%7B%22session_id%22%3A%2219883537f3e824031df8d6121ec324c657b58207360019883537f3f2686%22%2C%22first_session_time%22%3A1754549944126%2C%22latest_session_time%22%3A1754549944813%7D',
    'aliyungf_tc': '60f8eaf3583cd9b61ec37ee72db71a9dd7274b8ec840d923283fe478103c5b22',
    'acw_tc': 'ac11000117633623717184426e0062d73257c9ccfd166ac139384640751709',
    '_ud_': '557ceb723cb146ffbc8fe3481ba20562',
    'JSESSIONID': 'AF337C9C7961684EFFF79F5BD3367758',
    'session': '532584d450c148559da7ee33a4a10200',
    'arialoadData': 'false',
    'zjzw_siteCode': '330000000000',
    'webId': '1',
    'zwlogBaseinfo': 'eyJsbF91c2VyaWQiOiIiLCJsb2dfc3RhdHVzIjoi5pyq55m75b2VIiwidXNlclR5cGUiOiJndWVzdCIsImJpel9zZXNzaW9uX2lkIjoiNTMyNTg0ZDQ1MGMxNDg1NTlkYTdlZTMzYTRhMTAyMDAiLCJzaXRlX2lkIjoiMzMwMDAwMDAwMDAwIiwicGFnZV9tb2RlIjoi5bi46KeE5qih5byPIn0%3D',
    'ssxmod_itna': '1-eqAx070Qi=dxg7Dh=zGkDphx97zqDODQq0dGM0Deq7tDRDFqAPiDHbAd8o5j9bb9D3hPDBiBYoidzjqDsqFi4GzDidKGhDBeE7eY87yKdKFD10TiF/jMxYqN=lZordG8/0ruyXLBKUl/BTxMzkxeYoxbDB3DbqDybDm0YxGGR4GwDGoD34DiDDPDbRrDAqqD7qDFSCWTNZTDm4GWSeGfDDoDYfudxitoDDtf7eG2FETdb0Di=DDliDx49GYiA=HKMPq_o=hC57Gtx0UaDBLPYsOGdVCqF=yUVF9IUeGyA5GutPqF1m78D6aAbFohD=xeeGeGxeehedBoo7Degx5DYYCqeiop2Dodod7YqO_FDhq75peQDDf17Db/6orGxjxbWNlEN/gNb0iVAeZ0T0QeinhPQ=cQozBqGC0PimY20plGdFvPYoP/DxD',
    'ssxmod_itna2': '1-eqAx070Qi=dxg7Dh=zGkDphx97zqDODQq0dGM0Deq7tDRDFqAPiDHbAd8o5j9bb9D3hPDBiBYoidzi4DWm97OhxboW47pxq/1p0IwdD0Hj5H=C=2G2k=wKnBRvTNIiMxkevB3Ynk4N7xnCdQiYbiL4d6qsL_jKjD5rebgWdm9/gN/_OGxxhu7nqritdISmniirLRDvx6eYmW/Iw6=sj=_FBatNkDqzL0L9mXq4LvG6Srq/C3nQY2GghuMB2_2i=0g8=cPfFX8TBh07pTev2i4Fi8D=0X7bvWDqWAy31qAddk4nCDquKg=qPZ/evjiBBuO0T_9cGRcpzT5C72ipPCa2fqp4uqfwpiWqwRG0uzn58Yi7lbF4bu/T1Dre7BazDsbykb0OQPwGiF09XKbFmPw_EN5erBwFzmES_8bPX9R89vfFqf4pbP4nKnQKBaghadyABfDZKgzaQA7L35fYvb5yadkD5T7c80KFBfpOsql_MyWfztqyKuTxyk6S4luxuRrFgpfKxFYqbessmhmqwtum=Eao4rzF6Y_uflaYbp8q24WVWwZAY_j593EzQpu4e9za1j5InT6cl4ZdvKIvXRtqqTwMFuIZfSOyqgAyKpu7X=WLp7yrXYlnXbWA7XtbF42sSLxRUx9UHDVsBnW4V9q6yywdc4H9_v4vr1GZzNX/hUtwKgt49wrFDKhTBN60V9GCqVfEjBxY_RiYQD20A94Pj4RjL04felkmlejGY/4uddbG=Qe4m57qYxpoI9GgL4QD=TODhAYB0waQTDe1oefK9gDVw8WOSxNkd9DzelnptdB4x1xq=N2dB_G1BeE4fBt9hzB544nhYj4_DPMbIGd=DxD',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ru;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Origin': 'https://www.zjzwfw.gov.cn',
    'Referer': 'https://www.zjzwfw.gov.cn/zjservice-fe/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
    'sec-ch-ua': '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'current': '1',
    'handleType': 'ALL',
    'pageSize': '40',
    'qlKind': '',
    'siteCode': '330000',
    'theme': '085',
    'themeUserType': '1'
}

response = requests.post('https://www.zjzwfw.gov.cn/jpaas-zjservice-server/open-api/item/getMatterListByTheme',
                         headers=headers, cookies=cookies, data=data)
data = response.json()
result = []
for item in data['data']['data']['data']['list']:
    if 'qlInnerCode' in item:
        qlInnerCode = item['qlInnerCode']
        url = 'https://www.zjzwfw.gov.cn/zjservice-fe/#/workguide?localInnerCode=' + qlInnerCode
        title = item['qlName']
        result.append({'url': url, 'title': title})
    elif 'subMatterList' in item:
        for subItem in item['subMatterList']:
            if 'qlInnerCode' in subItem:
                qlInnerCode = subItem['qlInnerCode']
                url = 'https://www.zjzwfw.gov.cn/zjservice-fe/#/workguide?localInnerCode=' + qlInnerCode
                title = subItem['qlName']
                result.append({'url': url, 'title': title})
            else:
                for subItem1 in subItem['subMatterList']:
                    if 'qlInnerCode' in subItem1:
                        qlInnerCode = subItem1['qlInnerCode']
                        url = 'https://www.zjzwfw.gov.cn/zjservice-fe/#/workguide?localInnerCode=' + qlInnerCode
                        title = subItem1['qlName']
                        result.append({'url': url, 'title': title})
print(result)
