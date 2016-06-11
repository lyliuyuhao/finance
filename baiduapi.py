import sys, urllib.request, json

def get_stock_cn(list_location, stock_id):
    """
    查询中国股票的函数。
    list_location:上市地点， sh和sz
    stock_id:股票代码
    返回值：最近一个交易日的股票信息，包括买卖价格，买卖份额，当天的大盘信息以及K线图---json数据
    """
    url_cn = "http://apis.baidu.com/apistore/stockservice/stock?stockid=" + list_location + stock_id + "&list=1"

    req_cn = urllib.request.Request(url_cn)
    req_cn.add_header("apikey", "420ed7c48c24b39d35c142f524b29e84")

    resp_cn = urllib.request.urlopen(req_cn)
    content_cn = resp_cn.read()

    return content_cn

def main():
    a = get_stock_cn("sz", "002230")
    b = json.dump(a)
    print(b)

if __name__ == '__main__':
    sys.exit(int(main() or 0))
