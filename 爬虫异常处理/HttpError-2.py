
import urllib2
 
req = urllib2.Request('http://blogx.csdn.net/cqcre1')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"
