Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib2
>>> url = 'http://python.jobbole.com/81334/'
>>> user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36)'
>>> values = {'username' : 'wx',  'password' : '123456' }
>>> headers = { 'User-Agent' : user_agent }
>>> data = urllib.urlencode(values)
>>> request = urllib2.Request(url, data, headers)
>>> response = urllib2.urlopen(request)
>>> page = response.read()
>>> print page


