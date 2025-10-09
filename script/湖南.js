function to_approve_page(approve_id, type, org_id) {
    var areacode = $("#areacode").val();
    var dghy = "";
    var webroot = $("#webroot").val();
    var cscjwt = "";
    window.open(webroot + "/onething/service/serviceguideck.jsp?approve_id=" + approve_id + "&type=" + type + "&dghy=" + dghy + "&cscjwt=" + cscjwt + "&org_id=" + org_id + "&areacode=" + areacode + "&org_id=" + org_id);
}