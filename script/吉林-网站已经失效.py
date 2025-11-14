from time import sleep

from DrissionPage._base.chromium import Chromium
from DrissionPage._configs.chromium_options import ChromiumOptions

chromium_options = ChromiumOptions()
chromium_options.set_local_port(9221)
page = Chromium(addr_or_opts=chromium_options)
tab = page.new_tab()
tab.get("https://zwfw.jl.gov.cn/jlszwfw/")
tab.run_js("""
function asyncSend() {
    return new Promise((resolve) => {
        httpUtils.send("matter", "paged", {
            "current": "1",
            "pageSize": "100",
            "areaId": "220000",
            "taskName": "",
            "usertopictype": "085",
            "corptopictype": "",
            "serverType": "1",
            "deptCode": "",
            "taskType": "",
            "projectType": "",
            "operaType": "",
            "materialFormat": "",
            "onlinehandledepth": "1"
        }, (result) => {
            resolve(result);
        });
    });
}
(async () => {
    const result = await asyncSend();
    window.result = result;
})();
""")
sleep(3)
data = tab.run_js("""
const result = window.result;
return result
""")
result = []
for tab in data['data']['basic']:
    for info in tab['infoList']:
        for matt in info['mattList']:
            url = f"https://zwfw.jl.gov.cn/jlszwfw/bsznxq/?taskCode={matt['taskHandleItem']}&type=1&area={matt['areaCode']}"
            result.append(url)
print(result)
page.quit()
