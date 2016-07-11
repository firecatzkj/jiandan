from  bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import re



# he = {'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3','User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.151 Safari/534.16'}
# req = urllib.request.Request("http://jandan.net/ooxx/page-2033")
# h = urllib.request.urlopen(req)
# bsobj = BeautifulSoup(h,"html.parser")
# print(bsobj.title)


def get_web_bsobj():
    req = urllib.request.Request("http://jandan.net/ooxx/page-2043")
    h = urllib.request.urlopen(req)
    bsobj = BeautifulSoup(h, "html5lib")
    print(bsobj.title)

    return  bsobj

def get_file_bsobj():
    h = urlopen("file:c:/mzt.html")
    bsobj = BeautifulSoup(h,'html5lib')
    return bsobj


bsobj = get_web_bsobj()
print(str(bsobj.title.text)+"解析就绪")

#content = bsobj.findAll('li',{"id":re.compile("comment-[0-9]+")},recursive=True);
#print(len(content))


#content = bsobj.findAll('li',{"id":re.compile("comment-box-comment-[0-9]+")},recursive=True);
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
    fn = "d:/mzt/"+str(j)+".jpg"
    urllib.request.urlretrieve(i,fn)
    j=j+1
    print("saved %s" %j)