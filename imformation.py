class pixivinfo:
    def __init__( self, refer = 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'):
        self.referer    = refer
        self.ua         = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        self.AcceptL    = 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7'
        self.headers    = \
        {
            "user-agent"        : self.ua,
            "Accept-Language"   : self.AcceptL,
            "Referer"           : self.referer
        }
        self.login_site = "https://accounts.pixiv.net/login?lang=zh"
        self.login_post = "https://accounts.pixiv.net/api/login?lang=zh"
        self.book_mark  = "https://www.pixiv.net/bookmark.php?rest=show&p="
        self.save_dir   = "C:\\_picture\\"
        


    def refereract( self, refer = ''):
        self.headers    = \
        {
            "user-agent"        : self.ua,
            "Accept-Language"   : self.AcceptL,
            "Referer"           : self.referer
        }
        return self.headers

