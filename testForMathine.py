import sys, urllib.request, json
url = 'http://apis.baidu.com/apistore/stockservice/stock?stockid=sz002230&list=1'
req = urllib.request.Request(url)
req.add_header("apikey", "420ed7c48c24b39d35c142f524b29e84")
resp = urllib.request.urlopen(req)
content = resp.read()
if (content):
    print(content)