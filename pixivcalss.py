import requests
import imformation
import re

class pixiv:
    def __init__(self):
        self.session    = requests.session()
        self.info       = imformation.pixivinfo()
        self.session.headers = self.info.headers
        self.session.timeout = 10
        self.result     = self.session.get(self.info.login_site)
        post_key = ''
        post_key = re.findall(r"<input.+?name=\"post_key\".+?>",self.result.text)[0].split(" ")[3].split("\"")[1]
        post_data=\
        {
            "pixiv_id":"",
            "password":"",
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

