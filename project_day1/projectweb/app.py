import urllib,urllib2
link="https://merojob.com/search/"

request=urllib2.Request(link)
response=urllib2.urlopen(link)
print response.read()
