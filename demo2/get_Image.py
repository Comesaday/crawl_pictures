#encoding:UTF-8
import urllib.request
import re
import os

def get_Html(url):
        #直接打开网页，不经请求
    html=urllib.request.urlopen(url)
    html=html.read()
    html=html.decode("utf-8")
    return html

def get_Image(html):
    reg=r'src="(.+?\.jpg)" pic_ext'
    image=re.compile(reg)
    imglist=image.findall(html)
    x=1
    path='E:\\test'
    if not os.path.isdir(path):
        print("文件夹不存在！")
        os.makedirs(path)
        print("创建文件夹成功!")
    paths=path+'\\'
    for imgurl in imglist:
        print("第%d张图片"%(x))
        print("图片地址："+imgurl)
        urllib.request.urlretrieve(imgurl,'{}{}.jpg'.format(paths,x+1))
        x=x+1
        print("下载成功")
    print("全部下载完成！")
    return imglist

url="http://tieba.baidu.com/p/2460150866"
html=get_Html(url)
print(get_Image(html))
