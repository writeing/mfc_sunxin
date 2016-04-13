# -^- coding:utf-8 -*-
import urllib2
import urllib
import requests
import Cookie
import cookielib
import time
#url = 'http://v.youku.com/v_show/id_XMjcxNjEyMDQ4.html'
Ftime = time.time
def downYK(url):    
    c = cookielib.LWPCookieJar()

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(c))

    request = urllib2.Request(url)
    html = opener.open(request).read()    


    ykss = c.as_lwp_str().split(':')[1].split(';')[0][6:]
    secTime = str(int(Ftime()*1000))
    downUrl = 'http://127.0.0.1:61078/?command=iku://|video|'+url+'|quality=flv|ykss='+ykss+'|ywebplayerbottom||'+secTime
    urllib2.urlopen(downUrl)
    #vodio =requests.get(downUrl)
    print ykss
#    f = open("mfc",'w')
#    f.write(html)
#    f.close()
