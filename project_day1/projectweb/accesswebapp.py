import urllib
import urllib2  
import re

link="http://www.jobsnepal.com/simple-job-search"
caches=[]
def request(url,param):
    data=urllib.urlencode({'Keywords':param})
    req=urllib2.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")   
    req.add_data(data)
    response=urllib2.urlopen(req)
    result=response.read()
    caches.append({"key":param,'value':result})
    return result


    #return response.read()
def match_result(regex,content):
    pattern=re.compile(regex)
    return pattern.findall(content)
def print_result(matches):
    for r in matches:
        print "Link: %s" % r[1]
        print "job title: %s" % r[2].strip()
        print "Company: %s" % r[7].strip()
        print "Company URL: %s" % r[5]
        print "-----------------------"
param=raw_input("Enter Search Keyword: ")
result=request(link,param)
#print result
result=result.replace("\n"," ")

#print results
#print result
#filename=raw_input("Enter File Name: ")
#file=open(filename+".html","w+")
#file.write(response.read())
#file.close()
#print response.read()
regex='<a class="job-item" (.*?) href="(.*?)" >(.*?)</a>(.*?)<td >(.*?)<a href="(.*?)"(.*?)class="joblist">(.*?)</a>(.*?)<!-- Company Type'
matches=match_result(regex,result)
#pattern=re.compile(regex)
#matches=pattern.findall(result)

#print matches