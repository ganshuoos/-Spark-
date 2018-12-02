import urllib.request
import urllib.error
import urllib.parse
import urllib.robotparser
import http

# Cookie Use
LOGIN_URL = "https://osu.ppy.sh/home#"
get_url = 'https://osu.ppy.sh/home#'
values = {'username': 'WangLikethis', 'password': 'trghajj1'}
postdata = urllib.parse.urlencode(values).encode()
user_agent = r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36'\
             r' (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'

headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
# Store cookie locally, and call it cookie.txt
cookie_filename = 'cookie.txt'
cookie_aff = http.HTTPStatus.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie_aff)
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(LOGIN_URL, postdata, headers)

try:
    response = opener.open(request)

except urllib.error.URLError as e:
    print(e.reason)

cookie_aff.save(ignore_discard=True, ignore_expires=True)

for item in cookie_aff:
    print('Name =' + item.name)
    print('Value =' + item.value)

get_request = urllib.request.Request(get_url, headers=headers)
get_response = opener.open(get_request)
print(get_response.read().decode())