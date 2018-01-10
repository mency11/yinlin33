import urllib
import urllib2
import re
for i in range(0,10):
    url = "http://www.meilishuo.com/search/goods/?ptp=1.PvGO8.0.0.QKQ9lJQ&searchKey=%E8%96%84%E5%8D%AB%E8%A1%A3&page="+str(i)+"&cpc_offset=0"
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    data = urllib2.urlopen(request).read().decode("utf-8","ignore")
    pat = re.compile('<a class="img-link".*?href="(.*?)"',re.S)
    rst = re.findall(pat,data)
    for j in range(0,len(rst)):
        try:
            url2 = rst[j]
            data2 = urllib2.urlopen(url2).read().decode("utf-8","ignore")
            name_pat = re.compile('<span itemprop="name">(.*?)<',re.S)
            price_pat = re.compile('<span id="J_NowPrice" class="price" >(.*?)<',re.S)
            evaluate_pat = re.compile('<span class="num">(.*?)<',re.S)
            sales_volume_pat = re.compile('<span class="num J_SaleNum">(.*?)<',re.S)
            rst2 = re.findall(name_pat,data2)
            rst3 = re.findall(price_pat,data2)
            name_rst = rst2[0].encode("utf-8")
            price_rst = rst3[0].encode("utf-8")
            evaluate_rst = re.findall(evaluate_pat,data2)
            sales_volume_rst = re.findall(sales_volume_pat,data2)
            evaluate_rst[0] = evaluate_rst[0][10:]
            sales_volume_rst[0] = sales_volume_rst[0][10:]
            print "name:",name_rst
            print "price:",price_rst
            print "evaluate:",evaluate_rst[0]
            print "sales volume:",sales_volume_rst[0]
            print "----------------------------------------------"
            if (j + 1) % 5 == 0:
                input = raw_input()
                if input == '':
                    continue
                else:
                    break
        except Exception as err:
            print err