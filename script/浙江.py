import json

from DrissionPage._base.chromium import Chromium
from DrissionPage._configs.chromium_options import ChromiumOptions

chromium_options = ChromiumOptions()
chromium_options.set_local_port(9221).headless()
page = Chromium(addr_or_opts=chromium_options)
tab = page.new_tab()
tab.listen.start("/interface/gateway.do")
tab.get(
    "https://www.zjzwfw.gov.cn/zjservice-fe/#/serviceChild?id=11&tabOption=THEME&personType=1&siteCode=330000000000")
packets = tab.listen.wait(count=10)
result = []
for packet in packets:
    data = json.loads(packet.response.body['data'])
    try:
        for i in data['data']['data']['data']:
            if i['name'] == '社保':
                for category in i['categoryTwoList']:
                    for affair in category['handlingAffairsVOS']:
                        if 'id' in affair:
                            url = 'https://www.zjzwfw.gov.cn/zjservice-fe/#/workguide?localInnerCode=' + affair['id']
                            title = affair['name']
                            result.append({'url': url, 'title': title})
    except KeyError:
        pass
print(result)
