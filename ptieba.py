# -*-coding:utf-8 -*-
import re
import requests
import random
from bs4 import BeautifulSoup
import os
from urllib.request import urlopen

class Tool():
    """docstring for Tool"""
    removeImg = re.compile('<img.*?>| {7} | ')
    removeA = re.compile('<a.*?> | </a>')


class Spyder():
    """docstring for Spyder"""
    # 初始化
    def __init__(self):
        self.tool = Tool()

    # 获取源码
    def GetSource(self,url):
        UserAgents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \(KHTML, like Gecko) Element Browser 5.0','IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)','Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14','Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \Version/6.0 Mobile/10A5355d Safari/8536.25','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \Chrome/28.0.1468.0 Safari/537.36','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)' ]
        RandIndex = random.randint(0,9)
        UserAgent = UserAgents[RandIndex]
        Headers = {'User_Agent':UserAgent}
        R = requests.get(url=url,params=Headers)
        result = R.text
        # print(result)
        return result

    # 获取帖子信息，如标题、页数、图片链接
    # 将两个方法合并是因为，一需要发送一次请求，优化程序速度
    def GetInformation(self,url):
        HtmlSource = self.GetSource(url=url)
        # 获取标题
        Pattern = re.compile('<h3 class="core_title_txt.*?title=.*?>(.*?)</h3>',re.S)
        Items = re.search(pattern=Pattern,string=HtmlSource)
        Title = Items.group(1)
        print(u'\n帖子标题为:',Title)
        # 获取帖子的页数
        Pattern = re.compile('<div class="p_thread.*?<ul class="l_posts_num.*?共<span.*?>(.*?)</span>页',re.S)
        Items = re.search(pattern=Pattern,string=HtmlSource)
        PageNumber = Items.group(1)
        print(u'\n帖子页数为:',PageNumber)
        return Title, PageNumber

        # 获取图片的链接
    def GetImageLinks(self,url):
        HtmlSource = self.GetSource(url=url)
        Soup = BeautifulSoup(HtmlSource,'lxml')
        Items = Soup.find_all('img',class_='BDE_Image')
        Images = []
        number = 0
        for Item in Items:
            Images.append(Item['src'])
            number += 1
        if number >= 1:
            print(u'共找到',number,u'张图片')
        else:
            print(u'没找到图片')
        return Images

    # 创建目录
    def MakeDir(self,path):
        self.path = path.strip()
        IsExist = os.path.exists(path=path)
        if not IsExist:
            print(u'正在创建名为:',self.path,u'的文件夹')
            os.mkdir(self.path)
            return self.path
        else:
            print(u'名为:',self.path,u'的文件夹已经存在')
            return False

    # 下载一张图片
    def DownloadImage(self,ImageLink,Name):
        data = urlopen(ImageLink).read()
        fileName = Name + '.jpg'
        with open('%s\%s' %(self.path,fileName),'wb') as f:
            f.write(data)
        print(u'下载成功:',fileName)

    # 下载帖子中所有的图片
    def DownloadAllImage(self,Num):
        self.siteURL = 'https://tieba.baidu.com/p/' + str(Num)
        Title, PageNumber = self.GetInformation(url=self.siteURL)
        for Page in range(1,int(PageNumber)+1):
            self.url = self.siteURL + '?pn=' + str(Page)
            Images = self.GetImageLinks(url=self.url )
            print(u'正在获取第',Page,'页的图片')
            Path = self.MakeDir('Page'+str(Page))
            number = 1
            for ImageLink in Images:
                self.DownloadImage(ImageLink=ImageLink,Name=Path+'Num'+str(number))
                number += 1
            print(u'完成第',Page,'页的下载')
        print(u'全部完成！')

Spyder = Spyder()
Num = int(input('输入帖子号:'))
Spyder.DownloadAllImage(Num=Num)
