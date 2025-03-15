// "DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING": true in %appdata%/discord/settings.json. 
xpath = '/html/body/div[1]/div[3]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div[3]/main/div[1]/div/div/ol';
xpath2 = '/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div[3]/main/div[1]/div/div/ol';
function loop() {
    verify = ""
    image = document.evaluate(xpath + '/li[last()]//div/div[3]/div/div/div/div/button[1]/div/div/img', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue
    image2 = document.evaluate(xpath + '/li[last()-1]//div/div[3]/div/div/div/div/button[1]/div/div/img', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue
    if (image) {
        image.closest('button').click();
    } else if (image2) {
        image2.closest('button').click();
    } else if (true) {
        if (image) {
            image = document.evaluate(xpath2 + '/li[last()]//div/div[3]/div/div/div/div/button[1]/div/div/img', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue
            image2 = document.evaluate(xpath2 + '/li[last()-1]//div/div[3]/div/div/div/div/button[1]/div/div/img', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue
            image.closest('button').click();
        } else if (image2) {
            image2.closest('button').click();
        } else {
            console.log("FISH: Not found")
        }
    }
}
setInterval(loop, 4000);