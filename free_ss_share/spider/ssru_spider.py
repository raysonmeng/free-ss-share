# coding=utf-8
# https://shadowsocksr.ru/
import re
from selenium import webdriver
from lxml import etree

# reChinese = re.compile('[\x80-\xff]+').findall(teststr)

host = 'http://captianbreak.com/'
driver = webdriver.PhantomJS(executable_path='/Users/Rayson/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get(host)
with open('png.png', 'w') as f:
    f.write(driver.get_screenshot_as_png())

# print driver.page_source
# url_list = etree.HTML(driver.page_source).xpath('/html/body/div[3]/div/div/div/img/@src')
# location_list = etree.HTML(driver.page_source).xpath('/html/body/div[3]/div/div/div/span/text()')
#
# for i in xrange(len(url_list)):
#     print location_list[i], url_list[i].encode('utf-8').split('url=')[1]  # , re.compile('[\u4e00-\u9fa5]+').findall(url_list[i].encode('utf-8').split('url=')[1])