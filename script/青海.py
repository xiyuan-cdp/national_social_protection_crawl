from DrissionPage._base.chromium import Chromium
from DrissionPage._configs.chromium_options import ChromiumOptions


def get_query_data(currentpage: int):
    replace = """
             return window.sm2Util.encrypt(JSON.stringify({
                "token": "Epoint_WebSerivce_**##0601",
    			"params": {
                    "keyword": '',
    				"shenpilb": "",
    				"if_jz_hall": "1",
    				"usertype": usertype,
    				"webapplytype": canonline,
    				"areacode": areacode,
    				"dictguid": dictguid,
    				"currentpage": {currentpage},
    				"pagesize": 10
    			}
    		}));
            """.replace('{currentpage}', str(currentpage))

    return tab.run_js(replace)


def get_data() -> list:
    tab.ele('@title=社会保障').click()
    import requests

    cookies = {
        '_gscu_762245679': '52052137uz419z12',
        'fontZoomState': '0',
        '__51uvsct__3K0Ea7J1KxW9zpnb': '1',
        '__51vcke__3K0Ea7J1KxW9zpnb': '7a115d9c-bf75-5bf2-92e3-727ac575a05c',
        '__51vuft__3K0Ea7J1KxW9zpnb': '1752052177244',
        '_gscbrs_762245679': '1',
        '_gscs_762245679': '53428031dhptfl12|pv:3',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://www.qhzwfw.gov.cn',
        'Referer': 'https://www.qhzwfw.gov.cn/personal_services.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'encrypt': '1',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    pageno = 0
    urls = []
    while True:
        data = get_query_data(pageno)
        pageno = pageno + 1
        response = requests.post(
            'https://www.qhzwfw.gov.cn/epoint-web-qhzwdt/rest/qhzwdtaskandprojectbyou/getThemeCategoryTaskList',
            headers=headers, cookies=cookies, data=data)
        text = response.text
        data = tab.run_js(f"""
                 return  JSON.parse(window.sm2Util.aesDecrypt('{text}'));
                """)
        if not data['custom']['tasklist']:
            break
        for task in data['custom']['tasklist']:
            for item in task['categoryLittleTask']:
                taskcode = item['taskcode']
                url = f'https://www.qhzwfw.gov.cn/matterbszndetail.html?taskcode={taskcode}'
                urls.append(url)
                print(url)
    return urls



chromium_options = ChromiumOptions()
chromium_options.set_local_port(9221).headless()
page = Chromium(addr_or_opts=chromium_options)
try:
    tab = page.new_tab()
    tab.get("https://www.qhzwfw.gov.cn/personal_services.html")
    result = get_data()
    print(result)
finally:
    page.quit()
