import urllib
import urllib.request
import re

req = urllib.request.Request("http://zenpencils.com", headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:17.0) Gecko/20100101 Firefox/17.0'})
page = urllib.request.urlopen(req)
webpage = page.read()
webpageStr = webpage.decode(encoding = 'UTF-8')
links = re.findall('(<option value=")(.*)"',webpageStr)
for link in links:
  actualLink = link[1]
	if(actualLink != ''):
		print("parsing " + actualLink + "\n")
		imgPageReq = urllib.request.Request(actualLink, headers={'User-Agent':'Mozilla/5.0'})
		imgPage = urllib.request.urlopen(imgPageReq).read()
		imgPageStr = imgPage.decode(encoding = 'UTF-8')
		imgLinks = re.findall('(<div id="comic-1" class="comicpane"><img src=")(.*?)"',imgPageStr)
		for imgLink in imgLinks:
			actualImgLink = imgLink[1]
			explodedPgLink = actualLink.split('/')
			name = explodedPgLink[4] + '.' +actualImgLink[-3:]
			print("\tsaving " + name + "\n")
			path = r"d:\zenWorks"
			imgReq = urllib.request.Request(actualImgLink, headers={'User-Agent':'Mozilla/5.0'})
			local_file = open(path + "\\" + name, "wb")
			local_file.write(urllib.request.urlopen(imgReq).read())
			local_file.close()
