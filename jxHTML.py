import urllib2
import urllib
import requests
import downMFC
import time
from lxml import etree
mfcbase = 'http://v.dxsbb.com'
mfcUrl = 'http://v.dxsbb.com/jisuanji/555/'
YKbaseUrl = 'http://v.youku.com/v_show/id_%s.html'
def getHTMl(url):
    html = requests.get(url).content
    return html
def downURL(uu):
    html = getHTMl(uu)
    sou = etree.HTML(html)    
    data = sou.xpath(u'//div[@class="playerleft"]/script')
    ID = data[0].text.split(',')[3].split('\'')[1]
    ykurl = YKbaseUrl %ID
    downMFC.downYK(ykurl)
    time.sleep(5)
    
def main():
    html = getHTMl(mfcUrl)
    sou = etree.HTML(html)    
    Listurl = sou.xpath(u'//div[@id="play_1"]/ul/li/a')
    print Listurl
    for uu in Listurl:
        print uu.attrib['href']
        downURL(mfcbase+uu.attrib['href'])
        
if __name__=='__main__':
    main()