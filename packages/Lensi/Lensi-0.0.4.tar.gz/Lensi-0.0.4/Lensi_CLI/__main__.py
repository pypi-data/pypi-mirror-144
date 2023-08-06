#!/usr/bin/env python
# -*- coding:utf-8 _*-
import os
from pprint import pprint
import shutil
from urllib import request
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading
from urllib.parse import quote 
from fuzzywuzzy import fuzz,process
import fire
import configparser
from tqdm import tqdm
import winshell
import zipfile

def web_qq_info(qq_id):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    qq_id_int = int(qq_id)
    # pprint(qq_id)
    qq_info_url = 'https://pc.qq.com/detail/'+ str(qq_id_int%20) + '/detail_' + qq_id + '.html' 
    # pprint(qq_info_url)
    qq_info_html_req = request.Request(url=qq_info_url,headers=headers)
    qq_info_html = urlopen(qq_info_html_req)
    qq_info_soup = BeautifulSoup(qq_info_html.read(),"html.parser")
    try:
        qq_info_data = qq_info_soup.select('body > div.category-wrap > div.container_16 > div > div > div.detail-wrap > div.detail-desc > div.cont-content > p:nth-child(1)')
        for item in qq_info_data:
            qq_info_main = item.get_text()
        qq_info_data_home = qq_info_soup.select('body > div.category-wrap > div.container_16 > div > div > div.detail-wrap > div.detail-desc > div.cont-content > p:nth-child(3) > a')
        for item in qq_info_data_home:
            qq_info_home = item.get('href')
        qq_info = [qq_info_home,qq_info_main,qq_info_url]
        return qq_info
    except:
        qq_info_data = qq_info_soup.select('body > div.category-wrap > div.container_16 > div > div.part1')
        for item in qq_info_data:
            qq_info_image = item.get('style')
        qq_info_image_url = qq_info_image[int(qq_info_image.find('url(')):int(qq_info_image.find(')',qq_info_image.find('{url(')))].strip('url(')
        qq_info_image_url = qq_info_image_url.rstrip(")!important")
        if qq_info_image_url[0] == "/":
            qq_info_image_url = "https:" + qq_info_image_url
        # pprint(qq_info_image_url)
        return qq_info_image_url
    # pprint(qq_info_main,"\n",qq_info_home)

def web_baoku_info(baoku_id):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    # pprint(baoku_id)
    baoku_info_url = 'https://baoku.360.cn/soft/show/appid/' + baoku_id
    pprint(baoku_info_url)
    baoku_info_html_req = request.Request(url=baoku_info_url,headers=headers)
    baoku_info_html = urlopen(baoku_info_html_req)
    baoku_info_soup = BeautifulSoup(baoku_info_html.read(),"html.parser")
    baoku_info_data = baoku_info_soup.select('body > div.app-container > div:nth-child(2) > div.dashboard-container.pic-container > div > img')
    for item in baoku_info_data:
        baoku_info_image_url = item.get('src')
    baoku_info_image_url = "https:" +baoku_info_image_url
    # pprint(baoku_info_image_url)
    baoku_icon_data = baoku_info_soup.select('body > div.app-container > div:nth-child(2) > div:nth-child(2) > h1 > img')
    for item in baoku_icon_data:
        baoku_icon_image_url = item.get('src')
    baoku_icon_image_url = "https:" +baoku_icon_image_url
    pprint(baoku_icon_image_url)
    baoku_info_url = 'https://baoku.360.cn/soft/show/appid/' + baoku_id + 'd'
    # pprint(baoku_info_url)
    baoku_info_html_req = request.Request(url=baoku_info_url,headers=headers)
    baoku_info_html = urlopen(baoku_info_html_req)
    baoku_info_soup = BeautifulSoup(baoku_info_html.read(),"html.parser")
    baoku_detail = baoku_info_soup.select('body > div.wrap.clearfix > div.main-list.fr > div.app-info > div.app-introduce > div.introduce-txt1 > p')
    for item in baoku_detail:
        baoku_detail_text = item.get_text
    # pprint(baoku_detail_text)
    baoku_info = [baoku_detail_text,baoku_info_image_url]
    return baoku_info
    # pprint(baoku_info_main,"\n",baoku_info_home)

def web_hippo_info(app_name):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    hippo_information_html_url = "https://filehippo.com/download_" + app_name + "/"
    hippo_information_html_req = request.Request(url=hippo_information_html_url,headers=headers)
    hippo_information_html = urlopen(hippo_information_html_req)
    hippo_information_soup = BeautifulSoup(hippo_information_html.read(),"html.parser")
    hippo_information_data = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.mb-l > article')
    for item1 in hippo_information_data:
        hippo_information = item1.get_text()
    return hippo_information

def Lensi_info(app_name,app_source):
    if app_source == "qq":
        web_qq_info(app_name)
    elif app_source == "360":
        web_baoku_info(app_name)
    elif app_source == "Hippo":
        web_hippo_info(app_name)

class myThread (threading.Thread):
    def __init__(self, source, app_name,limit_num=3):
        threading.Thread.__init__(self)
        self.source = source
        self.app_name = app_name
        self.limit_num = limit_num
    def run(self):
        # print ("开始线程：" + self.app_name)
        self.result = lensi_search_all(self.source,self.app_name,self.limit_num) #多线程大函数
        # print ("退出线程：" + self.app_name)
    def get_result(self):  #获取return结果
        try:  
            return self.result  
        except Exception:  
            return None  

def web_360_search(app_name,limmit_num):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    # 伪装标头
    app_name_search = quote(app_name)#输入转换成相应格式
    # app_name = "geek"
    baoku_search_url = 'https://bapi.safe.360.cn/soft/search?keyword='+ app_name_search + '&page=1'
    baoku_html_req = request.Request(url=baoku_search_url,headers=headers)
    baoku_html = urlopen(baoku_html_req)#使用标头获取html
    baoku_soup = BeautifulSoup(baoku_html.read(),"html.parser")
    baoku_str = str(baoku_soup)#字符串化 便于查找
    # pprint(baoku_str)
    '''
    TODO 未使用正则表达式 待优化
    '''
    baoku_name_search_1 = 0
    baoku_version_search_1 = 0
    baoku_download_search_1 =0 
    baoku_id_search_1 = 0 
    baoku_detail_search_1 = 0
    baoku_icon_search_1 = 0
    # 定义上一次查找结果
    baoku_search_all_list = []
    limmit_num_search = baoku_str.count('{"softid":')
    limmit_num_real = min(limmit_num,limmit_num_search)
    #防止找不到更多程序
    for i in range(0,limmit_num_real):
        baoku_name_search = baoku_str.find('"softname":"',baoku_name_search_1)
        baoku_name_search_1 = baoku_name_search + 1
        baoku_name = baoku_str[baoku_name_search:int(baoku_str.find(',',baoku_name_search))].strip('"softname":"')
        if baoku_name == '':
            return baoku_search_all_list #判断是否还有软件
        baoku_version_search = baoku_str.find('"version":"',baoku_version_search_1)
        baoku_version_search_1 = baoku_version_search + 1
        baoku_download_search = baoku_str.find('"soft_download":"',baoku_download_search_1)
        baoku_download_search_1 = baoku_download_search + 1
        baoku_id_search = baoku_str.find('[{"softid":',baoku_id_search_1)
        baoku_detail_search = baoku_str.find('"desc":"',baoku_detail_search_1)
        baoku_detail_search_1 = baoku_detail_search + 1
        baoku_id_search_1 = baoku_id_search + 1
        baoku_icon_search = baoku_str.find('"logo":"',baoku_icon_search_1)
        baoku_icon_search_1 = baoku_icon_search + 1
        #从上一次查找结果后开始查找，实现识别多个软件
        baoku_version= baoku_str[baoku_version_search:int(baoku_str.find(',',baoku_version_search))].strip('"version":"')
        baoku_download = baoku_str[baoku_download_search:int(baoku_str.find(',',baoku_download_search))].strip('"soft_download":"')
        baoku_id = baoku_str[baoku_id_search :int(baoku_str.find(',',baoku_id_search ))].strip('[{"softid":')
        baoku_detail_text = baoku_str[baoku_detail_search :int(baoku_str.find(',',baoku_detail_search ))].strip('"desc":"')
        baoku_icon = baoku_str[baoku_icon_search :int(baoku_str.find(',',baoku_icon_search ))].strip('"logo":"')
        #截获字符串
        baoku_download_url = baoku_download.replace('\\',"")
        baoku_icon_url = "https:" + baoku_icon.replace('\\',"") + "g"
        baoku_info_url = 'https://baoku.360.cn/soft/show/appid/' + baoku_id + 'd'
        #网址处理
        baoku_search_all = [baoku_name.strip(",").encode('ascii').decode('unicode_escape'),baoku_version.strip(","),baoku_detail_text.strip(",").encode('ascii').decode('unicode_escape'),baoku_info_url,baoku_id,baoku_download_url.strip(","),baoku_icon_url,fuzz.partial_ratio(app_name,baoku_name.strip(",").encode('ascii').decode('unicode_escape')),"360"]
        #整理格式
        baoku_search_all_list.append(baoku_search_all)
    return baoku_search_all_list

def web_qq_search(app_name,limmit_num):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    # app_name = "geek"
    # app_name = app_name.encode('unicode_escape').decode('utf-8')
    # app_name_search = app_name.replace("\\","%")
    app_name_search = quote(app_name)
    # pprint(app_name_search)
    qq_search_url = 'https://s.pcmgr.qq.com/tapi/web/searchcgi.php?type=search&callback=searchCallback&keyword='+ app_name_search +'&page=1&pernum=' +str(limmit_num)+'&more=0'
    qq_html_req = request.Request(url=qq_search_url,headers=headers)
    qq_html = urlopen(qq_html_req)
    qq_soup = BeautifulSoup(qq_html.read(),"html.parser")
    qq_str = str(qq_soup)
    '''
    TODO 未使用正则表达式 待优化
    '''
    qq_search_all=[]
    qq_search_list=[]
    # pprint(qq_str)
    qq_name_find_1 = 0
    qq_version_find_1 = 0
    qq_download_find_1 = 0
    qq_id_find_1 = 0
    qq_detail_find_1 = 0  
    qq_icon_find_1 = 0
    limmit_num_real = min(limmit_num,qq_str.count('<versionname>'))
    #防止找不到更多程序
    for i in range(0,limmit_num_real):
        if i == 0:
            qq_name_find = qq_str.find('<![CDATA[',qq_name_find_1)
            qq_name_find_1 = qq_name_find + 1
        else:
            for j in range(0,7):
                qq_name_find = qq_str.find('<![CDATA[',qq_name_find_1)
                qq_name_find_1 = qq_name_find + 1
            # pprint(qq_name_find)
            #有7个“<![CDATA[”！！！ 之后才能找到正确软件名称
        qq_version_find = int(qq_str.find('<versionname>',qq_version_find_1))
        qq_version_find_1 = qq_version_find + 1
        # pprint(qq_name_find)
        qq_download_find = qq_str.find('[CDATA[http:',qq_download_find_1)
        qq_download_find_1 = qq_download_find + 1
        # pprint(qq_name_find)
        qq_id_find = qq_str.find('{"SoftID":"',qq_id_find_1)
        qq_id_find_1 = qq_id_find + 1 
        qq_detail_find = qq_str.find(r'<feature>\n                <![CDATA[',qq_detail_find_1) - 15
        qq_detail_find_1 = qq_detail_find + 1 
        qq_icon_find = qq_str.find('<logo48>',qq_icon_find_1) 
        qq_icon_find_1 = qq_icon_find + 1 
        # pprint(qq_name_find)
        #从上一次查找结果后开始查找，实现识别多个软件
        qq_name = qq_str[qq_name_find:int(qq_str.find("]",qq_name_find))].strip("<![CDATA[")
        if qq_name == '':
            return qq_search_list #判断是否还有软件
        qq_version = qq_str[qq_version_find:int(qq_str.find("&lt",qq_version_find))].strip("<versionname>")
        qq_download = qq_str[qq_download_find:int(qq_str.find("]",qq_download_find))].strip("![CDATA[")
        qq_id = qq_str[int(qq_id_find):int(qq_str.find(',',qq_id_find))].strip('{"SoftID":"')
        qq_detail = qq_str[qq_detail_find:int(qq_str.find(']',qq_detail_find))].strip(r"<feature>\n                <![CDATA[")
        qq_icon = qq_str[qq_icon_find:int(qq_str.find('&lt',qq_icon_find))].strip(' <logo48>')
        qq_icon_url = "https://pc3.gtimg.com/softmgr/logo/48/" + qq_icon + "g"
        qq_id_int = int(qq_id)
    # pprint(qq_id)
        qq_info_url = 'https://pc.qq.com/detail/'+ str(qq_id_int%20) + '/detail_' + qq_id + '.html' 
        # pprint(qq_detail)
        #截获字符串
        qq_download_url = qq_download.replace('\\',"")
        #网址处理
        qq_detail_text = qq_detail.encode('ascii').decode('unicode_escape')
        qq_search_all = [qq_name.encode('ascii').decode('unicode_escape'),qq_version,qq_detail_text.strip(";\n            <feature>\n                <![CDATA["),qq_info_url,qq_id,qq_download_url,qq_icon_url,fuzz.partial_ratio(app_name,qq_name.encode('ascii').decode('unicode_escape')),"qq"]
        #整理格式
        qq_search_list.append(qq_search_all)
    return qq_search_list
    # print (qq_name,"\n","Version:",qq_version,"\n",qq_download_url,"\n")

def hippo_search_easy(app_name):
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    hippo_download_html_url = "https://filehippo.com/download_" + app_name + "/post_download/"
    hippo_information_html_url = "https://filehippo.com/download_" + app_name + "/"
    hippo_search_result = []
    try:
        hippo_information_html_req = request.Request(url=hippo_information_html_url,headers=headers)
        hippo_information_html = urlopen(hippo_information_html_req)
    except:
        # pprint("!")
        return None
    else:
        # pprint("From",hippo_download_html_url,"\n","And also from",hippo_information_html_url,"\n")
        hippo_information_soup = BeautifulSoup(hippo_information_html.read(),"html.parser")
        hippo_information_data = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.mb-l > article > p:nth-child(3)')
        hippo_information_data_name = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.program-header-content > div.program-header-content__main > div > div.media__body > h1')
        hippo_icon_url_detail = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.program-header-content > div.program-header-content__main > div > div.media__image > img')
        hippo_version_detail = hippo_information_soup.select('body > div.page > div:nth-child(2) > div > div > div > section.program-header-content > div.program-header-content__main > div > div.media__body > p.program-header__version')
        for item in hippo_information_data_name:
            hippo_information_name = item.get_text()
        # print (hippo_information_name,"\n")
        for item1 in hippo_information_data:
            hippo_information = item1.get_text()
        for item2 in hippo_version_detail:
            hippo_version = item2.get_text()
        for item3 in hippo_icon_url_detail:
            hippo_icon_url = item3.get('src')
        # hippo_information = str(hippo_information)
        # print (hippo_information)
        try:
            hippo_download_html_req = request.Request(url=hippo_download_html_url,headers=headers)
            hippo_download_html = urlopen(hippo_download_html_req)
            hippo_download_soup = BeautifulSoup(hippo_download_html.read(),"html.parser")
            hippo_download_data = hippo_download_soup.select('body > div.page > script:nth-child(2)')
            for item2 in hippo_download_data:
                    hippo_download_url = item2.get('data-qa-download-url')
            # print (hippo_download_url)
        except:
            hippo_search_result_list = [hippo_information_name,hippo_version,hippo_information,hippo_information_html_url,app_name,None,hippo_icon_url,fuzz.partial_ratio(app_name,hippo_information_name),"hippo"]
            hippo_search_result.append(hippo_search_result_list)
            return hippo_search_result
        else:
            hippo_search_result_list = [hippo_information_name,hippo_version,hippo_information,hippo_information_html_url,app_name,hippo_download_url,hippo_icon_url,fuzz.partial_ratio(app_name,hippo_information_name),"hippo"]
            hippo_search_result.append(hippo_search_result_list)
            # pprint(hippo_search_result)
            return hippo_search_result

def lensi_search_all(source,app_name,limmit_num):#搜索大函数
        if source == "360":
            try:
                return web_360_search(app_name,limmit_num)
            except:
                pass
        elif source == "qq":
            try:
                return web_qq_search(app_name,limmit_num)
            except:
                pass
        elif source == "Hippo":
            try:
                return hippo_search_easy(app_name)
            except:
                pass

def app_name_cmp(e):
    return e[7]

def create_shortcut_to_desktop(app_folder,file_name):  
    target = "D:\\Lensi\\APP_Portable\\" +app_folder + "\\" + file_name
    title = file_name
    s = os.path.basename(target)  
    fname = os.path.splitext(s)[0]  
    winshell.CreateShortcut(Path = os.path.join(winshell.desktop(), fname + '.lnk'),Target = target,Icon=(target, 0), Description=title)  

def create_shortcut_to_startup(app_folder,file_name):  
    target = "D:\\Lensi\\APP_Portable\\" +app_folder + "\\" + file_name
    title = file_name
    s = os.path.basename(target)  
    fname = os.path.splitext(s)[0] 
    winshell.CreateShortcut(Path = os.path.join(winshell.startup(),fname + '.lnk'),Target = target,Icon=(target, 0),Description=title) 

def create_shortcut_to_startmenu(app_folder,file_name):  
    target = "D:\\Lensi\\APP_Portable\\" +app_folder + "\\" + file_name
    title = file_name
    s = os.path.basename(target)  
    fname = os.path.splitext(s)[0] 
    Path = os.path.join(winshell.startup().strip("\Startup"),"Lensi Apps",fname + '.lnk')
    winshell.CreateShortcut(Path,Target = target,Icon=(target, 0),Description=title) 

def install(file_name,app_name):
    os.chdir("D:\Lensi\Download")
    file_name_kinds = file_name[file_name.rfind("."):].strip(".")
    if file_name_kinds == "zip":
        zip_file = zipfile.ZipFile(file_name)
        zip_file.extractall("D:\Lensi\APP_Portable\\" + app_name + "\\")
        file_list = zip_file.namelist()
        zip_file.close()
        file_name_exe = app_name + ".exe"
        file_name_real = process.extractOne(file_name_exe,file_list)[0]
        os.chdir("D:\Lensi\APP_Portable\\" + app_name)
        file_list_real = os.listdir()
        if file_list_real[0].find(".exe") == -1:
            app_folder = app_name +"//" + file_list_real[0]
            create_shortcut_to_startmenu(app_folder,file_name_real)
            create_shortcut_to_desktop(app_folder,file_name_real)
        else:
            create_shortcut_to_startmenu(app_name,file_name_real)
            create_shortcut_to_desktop(app_name,file_name_real)
    elif file_name_kinds == "msi":
        cmd = "msiexec /i " + "D:\Lensi\Download\\" + file_name + " /norestart  /passive"
        # print(cmd)
        os.system(cmd)
    elif file_name_kinds == "exe":
        cmd = file_name + "/S /D=D:\Lensi\APP_Installed"
        os.system(cmd)
    else:
        os.system(file_name)

def DownloadandInstallFile(download_url,app_source,DAI,app_name):
    save_url = "D:\Lensi\Download"
    if app_source == "qq" or app_source == "360":
        file_name = download_url[download_url.rfind("/"):]
        file_name = file_name.strip("/")
    elif app_source == "hippo":
        file_name = download_url[download_url.rfind("="):]
        file_name = file_name.strip("=")
    if download_url is None or save_url is None or file_name is None:
        print('参数错误')
        return None
    res = requests.get(download_url,stream=True) 
    total_size = int(int(res.headers["Content-Length"])/1024+0.5)
    # 获取文件地址
    file_path = os.path.join(save_url, file_name)
    # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
    with open(file_path, 'wb') as fd:
        print('开始下载文件：{},当前文件大小：{}KB'.format(file_name,total_size))
        for chunk in tqdm(iterable=res.iter_content(1024),total=total_size,unit='k',desc=None):
            fd.write(chunk)
        print(file_name+' 下载完成！')
    os.chdir("D:\Lensi\Download")
    install(file_name,app_name)
    # os.system(file_name)
    os.chdir("D:\Lensi\Download")
    if DAI == "True":
        os.remove(file_name)

def DownloadFile(download_url,app_source):
    save_url = "D:\Lensi\Download"
    if app_source == "qq" or app_source == "360":
        file_name = download_url[download_url.rfind("/"):]
        file_name = file_name.strip("/")
    elif app_source == "hippo":
        file_name = download_url[download_url.rfind("="):]
        file_name = file_name.strip("=")
    if download_url is None or save_url is None or file_name is None:
        print('参数错误')
        return None
    res = requests.get(download_url,stream=True) 
    total_size = int(int(res.headers["Content-Length"])/1024+0.5)
    # 获取文件地址
    file_path = os.path.join(save_url, file_name)
    # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
    with open(file_path, 'wb') as fd:
        print('开始下载文件：{},当前文件大小：{}KB'.format(file_name,total_size))
        for chunk in tqdm(iterable=res.iter_content(1024),total=total_size,unit='k',desc=None):
            fd.write(chunk)
        print(file_name+' 下载完成！')
    os.system("start D:\Lensi\Download")

class Lensi(object):
    def __init__(self) -> None:
        try:
            if os.path.exists("D:\Lensi") == False:
                os.mkdir("D:\Lensi")
            if os.path.exists("D:\Lensi\Download") == False:
                os.mkdir("D:\Lensi\Download")
            if os.path.exists("D:\Lensi\APP_Portable") == False:
                os.mkdir("D:\Lensi\APP_Portable")
            if os.path.exists("D:\Lensi\APP_Installed") == False:
                os.mkdir("D:\Lensi\APP_Installed")
            start_menu = winshell.startup().replace("Startup","Lensi Apps")
            # print(start_menu)
            if os.path.exists(start_menu) == False:
                os.mkdir(start_menu)
            os.chdir("D:\Lensi")
            Lensi_config = configparser.ConfigParser()
            Lensi_config.read("config.ini", encoding="utf-8")
            global qq_num 
            qq_num = Lensi_config.getint("Lensi","qq_num")
            # print(qq_num)
            global baoku_num 
            baoku_num = Lensi_config.getint("Lensi","360_num")
            global DAI
            DAI = Lensi_config.get("Lensi","DAI(DeletedAfterInstalled)")
        except:
            print("Initing the config.ini")
            os.chdir("D:\Lensi")
            f = open("config.ini","w",encoding="utf-8")
            init_text = "[Lensi]\nqq_num = 1\n360_num = 1\nDAI(DeletedAfterInstalled) = True"
            f.write(init_text)
            f.close()
            Lensi_config = configparser.ConfigParser()
            os.chdir("D:\Lensi")
            Lensi_config.read("config.ini", encoding="utf-8")
            qq_num = Lensi_config.getint("Lensi", "qq_num")
            baoku_num = Lensi_config.getint("Lensi", "360_num")
            DAI = Lensi_config.getboolean("Lensi","DAI(DeletedAfterInstalled)") 
    def info_s(self,app_name,app_source):
        if app_source == "qq":
            pprint(web_qq_info(lensi_search_all("qq",app_name,1)[0][4]))
        elif app_source == "360":
            pprint(web_baoku_info(lensi_search_all("360",app_name,1)[0][4]))
        elif app_source == "Hippo":
            pprint(web_hippo_info(app_name))

    def info(self,app_name):
        print("QQ")
        try:
            qq_id = web_qq_search(app_name,1)[0][4]
        except:
            print("None")
        else:
            print(web_qq_info(qq_id))
        print("360")
        try:
            baoku_id = web_360_search("360",app_name,1)[0][4]
        except:
            print("None")
        else:
            print(web_baoku_info(baoku_id))
        print("Hippo")
        try:
            print(web_hippo_info(app_name))
        except:
            print("None")

    def install(self,app_name,app_source="all"):
        if app_source == "all":
            try:
                print("Downloading from Hippo")
                search_result = hippo_search_easy(app_name)
                download_url = search_result[0][5]
                app_name_real = search_result[0][0]
                # print(download_url)
                DownloadandInstallFile(download_url,"hippo",DAI,app_name_real)
            except:
                print("Hippo failed")
                print("Downloading from QQ")
                search_result =web_qq_search(app_name,1)
                download_url = search_result[0][5]
                app_name_real = search_result[0][0]
                DownloadandInstallFile(download_url,"qq",DAI,app_name_real)
        elif app_source == "360" or app_source == "360" or app_source == "b":
            print("Downloading from 360")
            search_result = web_360_search(app_name,1)
            download_url = search_result[0][5]
            app_name_real = search_result[0][0]
            DownloadandInstallFile(download_url,"360",DAI,app_name_real)
        elif app_source == "qq" or app_source == "qq" or app_source == "q":
            print("Downloading from QQ")
            search_result = web_qq_search(app_name,1)
            download_url = search_result[0][5]
            app_name_real = search_result[0][0]
            DownloadandInstallFile(download_url,"qq",DAI,app_name_real)
        elif app_source == "hippo" or app_source == "hippo" or app_source == "h":
            print("Downloading from Hippo")
            search_result = hippo_search_easy(app_name)
            download_url = search_result[0][5]
            app_name_real = search_result[0][0]
            # print(download_url)
            DownloadandInstallFile(download_url,"hippo",DAI,app_name_real)
    def download(self,app_name,app_source="all"):
        if app_source == "all":
            print("Downloading from QQ")
            download_url = web_qq_search(app_name,1)[0][5]
            DownloadFile(download_url,"qq")
        elif app_source == "360" or app_source == "360" or app_source == "b":
            print("Downloading from 360")
            download_url = web_360_search(app_name,1)[0][5]
            DownloadFile(download_url,"360")
        elif app_source == "qq" or app_source == "qq" or app_source == "q":
            print("Downloading from QQ")
            download_url = web_qq_search(app_name,1)[0][5]
            DownloadFile(download_url,"qq")
        elif app_source == "hippo" or app_source == "hippo" or app_source == "h":
            print("Downloading from Hippo")
            download_url = hippo_search_easy(app_name)[0][5]
            # print(download_url)
            DownloadFile(download_url,"hippo")


    def search(self,app_name,app_source="all",limmit_num = 0):
        app_source = str(app_source)
        limmit_num = int(limmit_num)
        if app_source == "all" and limmit_num == 0:
            if app_name == "Lensi":
                print("? You have installed it ,haven't you ?")
                return 
            if app_name == "Lensit":
                print("QEIE1284213AAUEUUQQ")
                print("I don't know what it means.")
            thread_360 = myThread("360", app_name,baoku_num)
            thread_qq = myThread("qq", app_name,qq_num)
            thread_H = myThread("Hippo", app_name,1)
            #多线程
            search_result = []
            # 开启新线程
            thread_360.start()
            thread_qq.start()
            thread_H.start()
            #等待进程
            thread_360.join()
            thread_qq.join()
            thread_H.join()
            # print ("退出主线程")
            #判断结果是否为空
            if thread_360.get_result() != None :
                search_result.extend(thread_360.get_result())
            if thread_qq.get_result() != None :
                search_result.extend(thread_qq.get_result())  
            if thread_H.get_result() != None :  
                search_result.extend(thread_H.get_result())  
            # pprint(search_result)
            search_result.sort(key=app_name_cmp,reverse=True)
            pprint(search_result)
        elif app_source == "360" or app_source == "360" or app_source == "b":
            if limmit_num == 0:
                pprint(web_360_search(app_name,baoku_num))
            else:
                pprint(web_360_search(app_name,limmit_num))
        elif app_source == "qq" or app_source == "qq" or app_source == "q":
            if limmit_num == 0:
                pprint(web_qq_search(app_name,qq_num))
            else:
                pprint(web_qq_search(app_name,limmit_num))
        elif app_source == "hippo" or app_source == "hippo" or app_source == "h":
            pprint(hippo_search_easy(app_name))
        else:
            print("Lensi doesn't support this source now. /(ㄒoㄒ)/~~")
    
    def yiju(self):
        headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
        url = 'https://yijuzhan.com/api/word.php'
        req = request.Request(url=url,headers=headers)
        html = urlopen(req)
        html_text = bytes.decode(html.read())
        print(html_text)
        print("(古诗API来自一句)")

    def clean(self):
        shutil.rmtree("D:\Lensi\Download")
        os.mkdir("D:\Lensi\Download")
        print("Has cleaned D:\Lensi\Download")
    
    def set(self,options,le_set=0):
        le_set =str(le_set)
        if options == "init":
            try:
                os.mkdir("D:\Lensi")
            except:
                pass
            try:
                os.mkdir("D:\Lensi\Download")
            except:
                    pass
            try:
                os.mkdir("D:\Lensi\APP_Installed")
            except:
                    pass
            try:
                os.mkdir("D:\Lensi\APP_Portable")
            except:
                    pass
            try:
                os.mkdir(winshell.startup().replace("Startup","Lensi Apps"))
            except:
                    pass
            os.chdir("D:\Lensi")
            f = open("config.ini","w",encoding="utf-8")
            init_text = "[Lensi]\nqq_num = 1\n360_num = 1\nDAI(DeletedAfterInstalled) = True\n"
            f.write(init_text)
            f.close
        else:
            Lensi_config = configparser.ConfigParser()
            os.chdir("D:\Lensi")
            Lensi_config.read("config.ini", encoding="utf-8")
            if options == "qq_num":
                Lensi_config.set("Lensi","qq_num",le_set)
            elif options == "baoku_num":
                Lensi_config.set("Lensi","360_num",le_set)
            elif options == "DAI(DeletedAfterInstalled)":
                Lensi_config.set("Lensi", "DAI(DeletedAfterInstalled)",le_set)
            else:
                print("Sorry, Lensi didn't have this setting.")
            Lensi_config.write(open("config.ini", "w"))

def main():
    fire.Fire(Lensi)