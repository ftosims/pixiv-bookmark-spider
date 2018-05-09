import pixivcalss
import re
import requests
if __name__ == '__main__':
    a = pixivcalss.pixiv()
    pag = 1
    sometingwrong = []
    #循环获取
    while(1):
        try:
            qwq = a.session.get(a.info.book_mark + str(pag))
        except requests.exceptions.RequestException:
            qwq = a.session.get(a.info.book_mark + str(pag))
        #正则
        qaq = re.compile(r'</div><a href="(.*?)" class="work  _work .*?"')
        next_url = re.findall(qaq,qwq.text)
        
        for url in next_url:
            try:
                target = a.session.get('https://www.pixiv.net/' + url)
            except requests.exceptions.RequestException:
                target = a.session.get('https://www.pixiv.net/' + url)
            qaq = re.compile(r'<img alt="(.*?)".*?data-src="(https://i.pximg.net/img-original/img/.*?_p0.(jpg|png))')
            imgurl = re.findall(qaq, target.text)
            if len(imgurl) == 1:
                imgdata = a.session.get(imgurl[0][1])
                imgdata = imgdata.content
                savedir = a.info.save_dir + imgurl[0][0] +'.' +imgurl[0][2]
                with open(savedir.replace('/',' '),'wb') as f:
                    f.write(imgdata)
                print('ok')
            else:
                print('next')
                #多图url逻辑,待写
        print(next_url)
        if (len(next_url) < 20):
            break
        pag+=1
        