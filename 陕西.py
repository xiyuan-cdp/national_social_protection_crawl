import json
from time import sleep
import random
import string
from DrissionPage._base.chromium import Chromium
from DrissionPage._configs.chromium_options import ChromiumOptions


def get_data() -> list:
    chromium_options = ChromiumOptions()
    chromium_options.set_local_port(9221).headless()
    page = Chromium(addr_or_opts=chromium_options)
    tab = page.new_tab()
    tab.get("https://zwfwzx.baoji.gov.cn/icity/icity/project/index?type=person")
    try:
        import requests

        cookies = {
            '_gscu_2044799855': '52051953wuvqws39',
            'ICITYSession': 'bfae75576c4f4395bab68006fa2e5879',
            '_gscbrs_2044799855': '1',
            '_gscs_2044799855': '53423754ginidw39|pv:2',
        }

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://zwfwzx.baoji.gov.cn',
            'Referer': 'https://zwfwzx.baoji.gov.cn/icity/icity/project/index?type=person',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {"cat": "theme", "ID": "16", "pagemodel": "person", "start": 1, "page": 1, "limit": 1000,
                "ITEM_TYPE": "",
                "out_type": "ZJJG", "SUIT_ONLINE": "", "SearchName": ""}
        data = tab.run_js(f"return encrypt_a('{json.dumps(data)}')+''")
        url = tab.run_js("""
            function addUrlAuth (url) {
                var curUrl = url;
                var sig = __signature;
                var chars = "0123456789abcdef";
                var key = "";
                var keyIndex = -1;
                for (var i = 0; i < 6; i++) {
                    var c = sig.charAt(keyIndex + 1);
                    key += c;
                    keyIndex = chars.indexOf(c);
                    if (keyIndex < 0 || keyIndex >= sig.length) {
                        keyIndex = i;
                    }
                }
        
                var timestamp = parseInt(Math.random() * (9999 - 1000 + 1) + 1000) + "_" + key + "_" + Date.parse(new Date());
                var t = timestamp.replace(/\+/g, "_");
                var tkey = toMD5Str(t);
        
                curUrl += "?s=" + sig;
                curUrl += "&t=" + t;
                curUrl += "&o=" + tkey;
                return curUrl;
            }
            return addUrlAuth("https://zwfwzx.baoji.gov.cn/icity/api-v2/shanxi.app.icity.govservice.GovProjectCmd/getInitList")
        """)
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies, data=json.dumps({'data': data}))
        urls = []
        for item in response.json()['data']:
            code = item['CODE']

            url = f'https://zwfwzx.baoji.gov.cn/icity/icity/proinfo/index?code={code}'
            urls.append(url)
        return urls
    finally:
        page.quit()


result = get_data()
print(result)
