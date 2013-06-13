import urllib2
response = urllib2.urlopen('http://feeds.twit.tv/twit_video_hd')
html = response.read()
print html
