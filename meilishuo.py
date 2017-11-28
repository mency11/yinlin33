'''
本程序实现的功能是将美丽说中的上衣标签中分类的前30页的图片保存到本地。
'''
#导入模块
import urllib.request
import re

#定义一个列表，用于存放个分类的url链接。
urls = []
#打开这个网页，并使用正则表达式爬取分类的url链接。
url = "http://www.meilishuo.com/search/catalog/10057049"
data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
pat = '<a href="(.*?)"'
rst = re.compile(pat,re.S).findall(data)
#将爬取下来的东西统一存放在刚刚定义的列表中。
for i in range(14, 48):
    urls.append(rst[i])

#根据上面抓取的url链接来获得图片链接，并控制页数是它自动翻页。
print("正在加载图片到本地目录，请稍后...")
for i in range(0, len(urls)):
    for j in range(1,31):       #控制页数。
        url2 = "http://www.meilishuo.com" + urls[i] + "&page=" + str(j)
        data2 = urllib.request.urlopen(url2).read().decode("utf-8", "ignore")
        pat2 = 'data-src="(.*?)"'
        rst2 = re.compile(pat2,re.S).findall(data2)
        #依次将刚刚获取到的图片链接，以图片的形式保存在本地的文件夹中。
        for k in range(0,len(rst2)):
            imgurl = rst2[k]
            localfile = "D:/test/test2/"+str(i)+str(j)+str(k)+".jpg"
            urllib.request.urlretrieve(imgurl,filename=localfile)
print("加载成功！！！")