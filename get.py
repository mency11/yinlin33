Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib2
>>> values={}
>>> values['username'] = "1016903103@qq.com"
>>> values['password']="XXXX"
>>> data = urllib.urlencode(values)
>>> url = "http://passport.csdn.net/account/login"
>>> geturl = url + "?"+data
>>> request = urllib2.Request(geturl)
>>> response = urllib2.urlopen(request)
>>> print response.geturl()
http://passport.csdn.net/account/login?username=1016903103%40qq.com&password=XXXX
>>> 
