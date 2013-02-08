import urllib2
from BeautifulSoup import BeautifulSoup
import os
import time

comicStart = 0
comicEnd = 1170

titles = []
comicImages = []
hiddenFunnies = []

realDatabase = True
getImages = False

for i in range(comicStart,comicEnd):
	try:
		url = "http://xkcd.com/" + str(i) + "/" # write the url here

		usock = urllib2.urlopen(url)
		data = usock.read()
		soup = BeautifulSoup(data)
		usock.close()
		mid = soup.find(id="middleContainer")
		title = mid.find(id="ctitle").contents
		titles.append(title)
		comic = mid.find(id="comic").img.get('src')
		comicImages.append(comic)
		hiddenComic = mid.find(id="comic").img.get('title')
		hiddenFunnies.append(hiddenComic)
		print str(title)[3:-2]
		print comic
		print hiddenComic
		print "------------------------"
		time.sleep(0)
		
		if getImages:
			lastImage = urllib2.urlopen(str(comic))
			image = lastImage.read()
			filename = "comic" + str(i) + str(comic)[-4:]
			print filename
			fout = open(filename,"wb")
			fout.write(image)
			fout.close()
			time.sleep(0)
	except urllib2.HTTPError, e:
		print 'We failed with error code - %s.' % e.code
if realDatabase:
	fout = open("xkcd.txt",'wb')
	for i in range(0,len(titles)):
		fout.write(str(i) + "\t" + str(titles[i])[3:-2]+"\t"+str(comicImages[i])+'\t' + str(hiddenFunnies[i])+'\n')
	fout.close()
