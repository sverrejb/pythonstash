import random, re, urllib
def getComment():
	socket = urllib.urlopen("http://www.youporn.com/random/video/")
	htmlSource = socket.read()
	socket.close()
	result = re.findall('<p class="message">((?:.|\\n)*?)</p>', htmlSource)
	link = re.findall('<link rel="canonical" href="((?:.|\\n)*?)" />', htmlSource)
	if result:
		print '"' + random.choice(result) + '"'
		print link[0]
	else:
		getComment()
getComment()