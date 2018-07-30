import pixivcalss
import re
import requests
import time
import os

##
# 虽然增加了图像是否相同的判断，但是并没有写重复了多少次之后停止运行
# 所以需要手动C-c

if __name__ == '__main__':
    a = pixivcalss.pixiv()
    pag = 1
    num = 0
    #循环获取
    
    while(1):
        # 获取bookmark页面，并且获得其中的图像页面链接
        markpage = a.get(a.info.book_mark+ str(pag))
        
        #正则
        next_url = a.findnext(a.info.firstRe, markpage.text)
        num = 0
        for url in next_url:
            a.getpic('https://www.pixiv.net/' + url)
            
        # 如果一个页面里的连接小于20，那么在执行完该页面之后将停止循环
        if (len(next_url) < 20):
            break
        pag+=1
        
