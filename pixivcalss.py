import requests
import imformation
import re
import os
import io
import hashlib
import math
import operator
from functools import reduce
from PIL import Image
from PIL import ImageFile
import imagehash


class pixiv:
    #构造函数开始
    #初始化,登录,账号,密码
    def __init__(self):
        self.session    = requests.session()
        self.info       = imformation.pixivinfo()
        self.session.headers = self.info.headers
        self.session.timeout = 10
        #设置request的代理
        # self.session.proxies = {
        #     'http' : 'localhost:1080',
        #     'https': 'localhost:1080'
        # }
        self.result     = self.session.get(self.info.login_site)
        post_key = ''
        post_key = re.findall(r"<input.+?name=\"post_key\".+?>",self.result.text)[0].split(" ")[3].split("\"")[1]
        post_data=\
        {
            "pixiv_id":self.info.pixivid,
            "password":self.info.pwd,
            "captcha":"",
            "g_recaptcha_response":"",
            "post_key":post_key,
            "source":"pc",
            "ref":"wwwtop_accounts_index",
            "return_to":"https://www.pixiv.net/",
        }
        self.result = self.session.post(self.info.login_post, data = post_data)
        self.session.headers = self.info.refereract('https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index')
        self.result = self.session.get("https://www.pixiv.net")
        if self.result.status_code == 200:
            print('ok')
    #构造函数结束

    #封装self.session.get,进行了异常处理
    def get(self, url, **kwargs):
        try:
            return self.session.get(url,**kwargs)
        except requests.exceptions.RequestException:
            return self.session.get(url,**kwargs)
    
    #re
    def findnext(self, regexp, text):
        regexp = re.compile(regexp)
        return re.findall(regexp, text)
    
    #进行图片的url获取,以及调用saveimg函数保存图片
    def getpic(self, url, num=0,authname=[]):
        target = self.get(url)
        if target.status_code == 404:
            return 0
         
        if num:
            authername = authname
        else:
            authername = self.findnext(self.info.getnameRe, target.text)
        savedir = authername[0][0] + '-' + authername[0][1]
        
        ismanga = self.get(url.replace("mode=medium", "mode=manga"))
        
        if ismanga.status_code == 400:
            imgurl = self.findnext(self.info.getpicRe, target.text)
        elif num:
            imgurl = self.findnext(self.info.getpicRe1, target.text)
        else:
            imgurl = self.findnext(self.info.getmangaRe, ismanga.text)
            ####not complete
        page = 0
        for turl in imgurl:
            if num or ismanga.status_code == 400:
                trueturl = turl[0].replace("\/","/")
                imgtype = turl[1]
            else:
                manga_bigurl = url.replace("mode=medium","mode=manga_big") +"&page=" + str(page)
                self.getpic( manga_bigurl, 1, authername)
                page = page + 1
                continue
            imgdata = self.get(trueturl)
            imgdata = imgdata.content
            self.saveimg(savedir, imgtype, imgdata)

    #保存图片,并且进行是否重复的判断.
    def saveimg( self, savedirn, imgtype, imgdata):
        savedir = self.info.save_dir + savedirn
        num = ""
        n = 1
        hashimg1 = hashlib.md5(imgdata)

        try:
            while os.path.exists((savedir+num+'.'+imgtype).replace('/',' ')):
                with open((savedir+num+'.'+imgtype).replace('/',' '),'rb') as f:
                    binary = f.read()
                    #hashimg2 = hashlib.md5(binary)
                if self.compare(imgdata, (savedir+num+'.'+imgtype).replace('/',' ')):
                    print("already download")
                    return 0
                num = '(' + str(n) + ')'
                n = n+1

            with open((savedir+num+'.'+imgtype).replace('/',' '),'wb') as f:
                f.write(imgdata)
                print(savedirn + ' ' + 'save success')
            return 1
        except OSError:
            print('something wrong')
            return 0

    def compare(self, imgfile ,target_fd, max_dif=0):
        try:
            ImageFile.LOAD_TRUNCATED_IMAGES = True
            hash_1 = None
            hash_2 = None
            origin = Image.open(target_fd)
            print(type(imgfile))
            print(origin.size)
            #other  = Image.frombytes(origin.mode,origin.size,imgfile)
            hash_1 = imagehash.average_hash(origin)
            hash_2 = imagehash.average_hash(Image.open(io.BytesIO(imgfile)))
            dif = hash_1 - hash_2
            if dif < 0:
                dif = -dif
            if dif <= max_dif:
                return True
            else:
                return False
        except ValueError:
            return False

