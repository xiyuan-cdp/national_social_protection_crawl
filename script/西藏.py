from time import sleep

from DrissionPage._base.chromium import Chromium
from DrissionPage._configs.chromium_options import ChromiumOptions


def get_query_data(currentpage: int):
    replace = """
             return window.sm2Util.encrypt(JSON.stringify({
                "token": "Epoint_WebSerivce_**##0601",
    			"params": {
                    usertype : "20",
                    currentpage : {currentpage},
                    pagesize : 15,
                    ouguid : "7c08b4d2-90e6-45e0-86c1-4efea9f3fa22",
                    dictid : "",
                    areacode : "540101"
                }
            }));
            """.replace('{currentpage}', str(currentpage))

    return tab.run_js(replace)


def get_data() -> list:
    # sleep(1)
    # tab.ele('主题分类').click()
    # tab.ele('社会保障').click()
    import requests

    cookies = {
        'sid': 'E7AAE73978EA4FB18B40A6DB8D922F57',
        'vname': 'lasa',
        'areacode': '540101',
        'isnormal': '1',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://smfw.lasa.gov.cn',
        'Referer': 'https://smfw.lasa.gov.cn/lszwdt/epointzwmhwz/pages/eventdetail/wanttodo',
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
            'https://smfw.lasa.gov.cn/lszwdt/rest/zwdtTask/getTaskList?foreSessionClusterIntercept=true',
            headers=headers,
            cookies=cookies, data=data)
        text = response.text
        data = tab.run_js(f"""
                 return  JSON.parse(window.sm2Util.aesDecrypt('{text}'));
                """)
        # print(data)
        if not data['custom']['tasklist']:
            break
        for task in data['custom']['tasklist']:
            taskcode = task['taskguid']
            title = task['taskname']
            url = f'https://smfw.lasa.gov.cn/lszwdt/epointzwmhwz/pages/eventdetail/personaleventdetail?taskguid={taskcode}'
            urls.append({"url": url, "title": title})
            print(url)
    return urls


chromium_options = ChromiumOptions()
chromium_options.set_local_port(9221).headless()
page = Chromium(addr_or_opts=chromium_options)
try:
    tab = page.new_tab()
    tab.get("https://smfw.lasa.gov.cn/lszwdt/epointzwmhwz/pages/eventdetail/wanttodo")
    result = get_data()
    print(result)
finally:
    page.quit()
