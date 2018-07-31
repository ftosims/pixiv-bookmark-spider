# python-bookmark-spider

## v0.2
What's new?<br>
1.多图链接已经可以爬取
2.多图链接的图像会用默认命名后面加上'(1)'、'(2)'这样的名字进行命名
3.为了防止每次收藏夹新增项目之后的重新爬，添加了图像是否相同的比较。
4.pixivclass中的登陆信息已经修改到imformation里面了。

修改imformation构造函数的前三条
第一条是pixivid
第二条是密码
第三条是默认保存地址。
Keep Moving~



## v0.1
第一次写python,代码写的蛮难看的……

已实现功能:
1. 爬p站收藏夹
2. 收藏夹中的多图链接还没法爬
3. 动图也没法爬=-=

python ./new.py 就可以运行
运行前记得打开全局代理
以及修改pixivclass.py中
post_data的pixiv_id和password为你的用户名和密码呢qwq
保存地址在imformation.py中,save_dir是保存地址
目前还有不少bug…就是有些时候遇到某些标题就崩了……倒是不影响其他的
