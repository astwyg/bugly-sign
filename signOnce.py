# -*- coding: utf-8 -*-
import urllib2,urllib
import cookielib
import json, datetime
import time, random

import sys
reload(sys)
sys. setdefaultencoding('utf8')


import logging
LOG_FILENAME="log.txt"
logging.basicConfig(filename=LOG_FILENAME,level=logging.WARNING)

def signOnce(iccid, phone, password):
    if iccid=="1" and phone=="1" and password=="1":
        iccid = "89860315840104315205"
        phone= "17710432234"
        password = "yun123456"
    else:
        logging.warning("%s-%s-%s-%s" %(str(datetime.datetime.now()),phone, password, iccid))
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

    # 登陆客户端
    loginInfo = json.dumps({"iccid":iccid,"loginName":phone,"password":password})
    req = urllib2.Request('http://www.yijitongoa.com:9090/yjtoa/s/clientlogin')
    req.add_header('User-Agent','yjt-oa')
    req.add_header('clientVersion','android_10409')
    req.add_header('Cookie2','$Version=1')
    req.add_header('apiVer','1')
    req.add_header('Content-Type','application/json; charset=utf-8')
    req.add_data(loginInfo)
    response = urllib2.urlopen(req)

    response = json.loads(response.read())
    if not response.get("payload"):
        return "签到失败!"+str(response)
    userId = response["payload"][0]["userId"]
    print "客户端已登录成功, 用户id %s" %userId


    # 登陆系统
    loginInfo = response["payload"][0]
    loginInfo["password"] = password
    loginInfo["iccid"] = iccid
    req = urllib2.Request('http://www.yijitongoa.com:9090/yjtoa/s/reallogin')
    req.add_header('User-Agent','yjt-oa')
    req.add_header('clientVersion','android_10409')
    req.add_header('Cookie2','$Version=1')
    req.add_header('apiVer','1')
    req.add_header('Content-Type','application/json; charset=utf-8')
    req.add_data(json.dumps(loginInfo))
    response = urllib2.urlopen(req)

    response = json.loads(response.read())
    if response["code"] == 0:
        print "系统已登录成功"
    else:
        print "系统登录失败"
        return "系统登陆失败!"+ str(response)


    #签到
    signInfo = {"descColor":0,"iccId":iccid,"id":0,"positionData":"39.962446,116.229728","positionDescription":"中国北京市海淀区杏石口路99号","resultColor":0,"signResult":0,"type":"VISIT","userId":userId}
    req = urllib2.Request('http://www.yijitongoa.com:9090/yjtoa/s/signins/attendances')
    req.add_header('User-Agent','yjt-oa')
    req.add_header('clientVersion','android_10409')
    req.add_header('Cookie2','$Version=1')
    req.add_header('apiVer','1')
    req.add_header('Content-Type','application/json; charset=utf-8')
    req.add_data(json.dumps(signInfo))
    response = urllib2.urlopen(req)
    response = response.read()
    print "签到完毕, 结果如下"
    print response
    return str(response)

if __name__ == '__main__':
    time.sleep(random.randint(0,30*60))
    signOnce(sys.argv[1], sys.argv[2], sys.argv[3])
