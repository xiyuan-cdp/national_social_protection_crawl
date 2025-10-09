/**
 * 移除出tag以外的全部标签，该方法只试过jq中测试，没有测试过vue，react等响应式框架（尚未知是否可用，未知会不会触发什么奇怪bug）
 * @param tag
 */


function clickElements(tag) {
    let elements = document.querySelectorAll(tag)
    for (let i = 0; i < elements.length; i++) {
        elements[i].click()
    }
}

function removeTag(tag) {
    let elements = document.querySelectorAll(tag)
    for (let i = 0; i < elements.length; i++) {
        elements[i].remove()
    }
}
function keepSpecifiedTag(tag, selector = true) {
    if (selector) {
        tag = document.querySelector(tag)
    }
    let children = tag.parentNode.children;
    for (let i = 0; i < children.length; i++) {
        if (children[i] === tag) continue
        children[i].remove()
    }

    if (tag.tagName !== "BODY")
        keepSpecifiedTag(tag.parentNode, false)
    else {
        let children = tag.children;
        debugger
        for (let i = 0; i < children.length; i++) {
            if (children[i] === tag) continue
            children[i].remove()
        }
    }
}
keepSpecifiedTag("#mainWrap")

clickElements(".matters-truncate-toggle")
