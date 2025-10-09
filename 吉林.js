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
    const result = await asyncSend();debugger
    console.log(result); // 确保在此处能获取到值
    return result;
})();


