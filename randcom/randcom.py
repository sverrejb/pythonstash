from bs4 import BeautifulSoup
import urllib, random
page =     BeautifulSoup(urllib.urlopen('http://www.youporn.com/random/video/'))
comments = page.findAll('p','message')
print random.choice(comments).text