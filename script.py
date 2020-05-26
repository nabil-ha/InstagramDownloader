from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.downloadvideosfrom.com/Instagram.php#')

while True:
    try:
        thewantedurl = str(input('url: '))
        urlplace = browser.find_element_by_id('url')
        urlplace.send_keys(thewantedurl)
        buttondown = browser.find_element_by_id('DownloadMP4')
        buttondown.click()
    except Exception as err:
        print(err)
        browser.close()

