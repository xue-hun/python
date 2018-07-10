#coding:utf-8
import os
import urllib
import sys
import requests
import re

def zhuanhuan(bianma):
    url = "http://developer.baidu.com/vcast/getVcastInfo"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://developer.baidu.com/vcast',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'BAIDUID=74CFC8F48E180941202037D6536FB59C:FG=1; BIDUPSID=8708AA0A3DD49BB5614E2D68EEBA6E57; PSTM=1529819432; BDUSS=DlTYm5iS3p6Y01vY0dKQ0NidEJnS1VZWm1jSjJXY1FPUFdQTTJRckQ3UkhYMlpiQVFBQUFBJCQAAAAAAAAAAAEAAADrg559eHVlaHVud2ViAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEfSPltH0j5bV; H_PS_PSSID=1431_25810_21116_18559_22073; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=tAksJeC62uDeXSO78ZEcDCbY0elmRfTTH6ao72snT2RbszaVTLETEG0PDx8g0Kubah6ZogKK5mOTH65P; H_BDCLCKID_SF=tJAD_C-MtI-3HJIk2tnhb-_eqxby26nJ0C3eaJ5nJDohsb5y0UPbehIk-POm5qFj5CJLbJQmQpP-HJA6DRb_35Dw-lbE5l5nBgTnKl0MLpbWbb0xynoD-tvBWxnMBMPtamOnaILaLIcjqR8ZDj85jUK; Hm_lvt_3abe3fb0969d25e335f1fe7559defcc6=1531101309; Hm_lpvt_3abe3fb0969d25e335f1fe7559defcc6=1531101316; PSINO=7; cflag=15%3A3; __cfduid=d22b22d3c817df308badb7b7dcfd644181531103495'
    }
    data = "title=1&content="+bianma+"&sex=4&speed=3&volumn=7&pit=5&method=TRADIONAL"
    r = requests.post(url=url,headers=headers,data=data)
    xiazai = r.text
    xiazaiurl = re.findall(':"(.*)",',xiazai)
    #正则匹配生成mp3的url
    # print xiazaiurl[0]
    return xiazaiurl[0]
    
jishu = 165
while (jishu < 518):
    mingz = str(jishu)
    mingz = mingz.zfill(5)
    wenben = mingz+'-.txt'
    txt = open(wenben)
    wenzi = txt.read()
    bianma = urllib.quote(wenzi.decode(sys.stdin.encoding).encode('utf8'))
    #提取文本内容转换为utf8编码
    xiazaiurl = zhuanhuan(bianma)
    b = requests.get(xiazaiurl)
    wenjianm = '1/'+mingz+'.mp3'
    with open(wenjianm, "wb") as code:
         code.write(b.content)
    print wenjianm+u'下载完成'
    jishu = jishu+1
