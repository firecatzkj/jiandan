from  bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import re
import os
# he = {'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3','User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.151 Safari/534.16'}
# req = urllib.request.Request("http://jandan.net/ooxx/page-2033")
# h = urllib.request.urlopen(req)
# bsobj = BeautifulSoup(h,"html.parser")
# print(bsobj.title)
def get_web_bsobj(target_url):
    req = urllib.request.Request(target_url)
    h = urllib.request.urlopen(req)
    bsobj = BeautifulSoup(h, "html5lib")
    print(bsobj.title)
    return  bsobj

def get_file_bsobj():
    h = urlopen("file:c:/mzt.html")
    bsobj = BeautifulSoup(h,'html5lib')
    return bsobj


def download_img(target_url,file_path):
    bsobj = get_web_bsobj(target_url)
    print(str(bsobj.title.text)+"解析就绪")
    content = bsobj.findAll('li',{"id":re.compile("comment-[0-9]+")},recursive=True);
    my_img_url=[]
    for i in content:
        temp = i.find_all('a',{'class':'view_img_link'})
        for j in temp:
            print(j['href'])
            my_img_url.append(j['href'])
        print("###########")
    print("^^^^^^^^^^^the next^^^^^^^^^^^^^")
    j=1
    for i in my_img_url:
        print(i)
        fn = file_path+str(j)+".jpg"
        urllib.request.urlretrieve(i,fn)
        j=j+1
        print("saved %s" %j)


def run():
    print("""
    #########################################
    #       煎蛋网妹子图片下载器        #####
    #########################################
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    运行之前请先在D盘下面新建mzt文件夹 摸摸蛋
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """)
    start_page_num = int(input("输入页码:"))
    total_page_num = int(input("输入要获取的页数"))

    s_url = "http://jandan.net/ooxx/page-"
    file_path = "d:/mzt/"

    for i in range(total_page_num):
        temp_dir = file_path + str(start_page_num) + "/"
        print(temp_dir)
        os.mkdir(temp_dir)
        url = s_url + str(start_page_num)
        start_page_num += 1
        print(url)
        download_img(url, temp_dir)
        print("##################" + url + "下载完毕" + "################")


if __name__ == '__main__':
    run()