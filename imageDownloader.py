import urllib
import urllib.request
import re
import os
from os import listdir
from os.path import expanduser

userHome = expanduser("~")
zenDir = userHome + "/Documents/zenWorks/img/"
print("saving images at "+zenDir)
localImgs = os.listdir(zenDir)
#print(localImgs)
req = urllib.request.Request("http://zenpencils.com", headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36'})
page = urllib.request.urlopen(req)
print("connected")
webpage = page.read()
webpageStr = webpage.decode(encoding = 'UTF-8')
links = re.findall('(<option value=")(.*)"',webpageStr)
for link in links:
    actualLink = link[1]
    if(actualLink != ''):
        print("parsing " + actualLink + "\n")
        imgPageReq = urllib.request.Request(actualLink, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36'})
        imgPage = urllib.request.urlopen(imgPageReq).read()
        imgPageStr = imgPage.decode(encoding = 'UTF-8')
        imgLinks = re.findall('(<div id="comic">[\s\n]*<img src=")(.*?)"',imgPageStr)
        for imgLink in imgLinks:
                        actualImgLink = imgLink[1]
                        explodedPgLink = actualLink.split('/')
                        name = explodedPgLink[4] + '.' +actualImgLink[-3:]
                        if (name in localImgs):
                                print(name + " exists\n")
                        else:
                                print("\tsaving " + name + "\n")
                                imgReq = urllib.request.Request(actualImgLink, headers={'User-Agent':'Mozilla/5.0'})
                                local_file = open(zenDir + name, "wb")
                                local_file.write(urllib.request.urlopen(imgReq).read())
                                local_file.close()
