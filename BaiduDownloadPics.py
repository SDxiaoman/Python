#-*- coding:utf-8 -*-
import re
import requests
import os

g_download_dir = 'H:/Python/res/' #文件存放路径（根据自己需要存放，但是要确保文件是否有创建权限）
word = input('Input the key value:') #需要搜索的关键字


#----------------------------------------------------------------------
def mdir():
    if not os.path.exists(g_download_dir):
        os.mkdir(g_download_dir)
    if  not os.path.exists(g_download_dir+word):
        os.mkdir(g_download_dir+word)

    os.chdir(g_download_dir+word)    

#----------------------------------------------------------------------
def geturl(page_number):
    #通过关键字搜索相关的图片进行下载
    #url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'    
    url = "http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=" + word + "&cg=girl&rn=60&pn=" + str(page_number)
    html = requests.get(url).text
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    return pic_url


#----------------------------------------------------------------------
def downimage(pic_url, page_number):
    i = 1
    for each in pic_url:
        print (each)
        try:
            pic= requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print ('Error! CAN NOT DOWMLOAD THIS PICTURE!')
            i = i - 1
            continue
        except requests.exceptions.Timeout:
            print ('========REQUEST TIMEOUT !!!========')
            i -= 1
        string = word+ str(page_number) + '-' + str(i) + '.jpg'
        fp = open(string,'wb')
        fp.write(pic.content)
        fp.close()
        i += 1    

#------------------------Start--------------------------------------
if __name__ == '__main__':
    mdir()
    page_number = 1
    page_count = 60
    while 1:
        mPicUrl = geturl(page_count)
        downimage(mPicUrl, page_number)
        page_count += 60
        page_number += 1

