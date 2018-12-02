import urllib.request
import urllib.error
import urllib.parse
import urllib.robotparser
import http

# 构造Request
# Get Method
LOGIN_URL = "http://网址"
values = {'username': '', 'password': ''}
data = urllib.parse.urlencode(values).encode()
geturl = LOGIN_URL + "?" + str(data)
get_method_request = urllib.request.Request(geturl)

# Post Method
LOGIN_URL = "http://网址"
values = {'username': '', 'password': ''}
data = urllib.parse.urlencode(values).encode()
post_method_request = urllib.request.Request(LOGIN_URL, data)


