class pixivinfo:
    def __init__( self):
        self.pixivid    = "" ## 请修改此处为您的账户
        self.pwd        = "" ## 请修改此处为您的密码
        # 默认储存文件夹
        self.save_dir   = "C:\\_picture\\"
        # HTTP header
        self.referer    = 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'
        self.ua         = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        self.AcceptL    = 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7'
        # Some Link
        ## login
        self.login_site = "https://accounts.pixiv.net/login?lang=zh"
        self.login_post = "https://accounts.pixiv.net/api/login?lang=zh"
        ## bookmark
        self.book_mark  = "https://www.pixiv.net/bookmark.php?rest=show&p="
        # 正则表达式
        ## 获取每页收藏夹内的次级图片链接
        self.firstRe    = r'</div><a href="(.*?)" class="work  _work .*?"'
        ## 获取单图链接下的大图链接
        self.getpicRe   = r'(https:\\/\\/i.pximg.net\\/img-original\\/img\\/.*?_p[0-9]+.(jpg|png))'
        ## 获取多图链接的manga_big中的大图链接
        self.getpicRe1  = r'(https://i.pximg.net/img-original/img/.*?_p[0-9]+.(jpg|png))'
        ## 获取作者名和作品名
        self.getnameRe  = r'<title>「(.*?)」/「(.*?)」のイラスト \[pixiv\]</title>'
        ## 获取多图链接下的次级链接
        self.getmangaRe = r'data-src="(https://i.pximg.net/img-master/img/.*?_master1200.jpg)"'
        # 文件头
        self.headers    = \
        {
            "user-agent"        : self.ua,
            "Accept-Language"   : self.AcceptL,
            "Referer"           : self.referer
        }
        
        

    # 暂时无用
    def refereract( self, refer = ''):
        self.headers    = \
        {
            "user-agent"        : self.ua,
            "Accept-Language"   : self.AcceptL,
            "Referer"           : self.referer
        }
        return self.headers

