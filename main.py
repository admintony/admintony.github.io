# coding = utf-8
"""
  用户输入数据：/2018/03/05/腾讯云COS图床智能上传工具编写/
  然后在当前目录下创建：依次创建这2018、03、05、腾讯云COS图床智能上传工具编写 这几个目录，并且在目录下创建一个index.html
  其内容如下，其中{} 表示根据用户输入来更变的
    <html>
    
    <head>
    <META HTTP-EQUIV=REFRESH CONTENT="5;URL=http://www.admintony.com/{}.html">
    </head>
    <body>
    很抱歉给您带来不便，由于站点URL规则更变，您可访问<a href="http://www.admintony.com/{}.html">{}</a>来进行文章阅读，也可以等待5秒后自动跳转到该页面。   
    <br>
    <span>感谢您对AdminTony的关注与支持</span>
    </body>
    </html>
"""

import os,re,sys

def makeDir(str):
    re_ = re.compile(r'/(\d+)/(\d+)/(\d+)/(.+)/')
    list = re_.findall(str)
    year = list[0][0]
    mouth = list[0][1]
    day = list[0][2]
    title = list[0][3]

    # 创建年份目录
    if not os.path.exists(year):
        os.mkdir(year)

    # 创建月份目录
    if not os.path.exists(year+"/"+mouth):
        os.mkdir(year+"/"+mouth)

    # 创建日期目录
    if not os.path.exists(year+"/"+mouth+"/"+day):
        os.mkdir(year+"/"+mouth+"/"+day)

    # 创建名称目录
    if not os.path.exists(year+"/"+mouth+"/"+day+"/"+title):
        os.mkdir(year+"/"+mouth+"/"+day+"/"+title)

    # 在日期目录下创建index.html
    with open(year+"/"+mouth+"/"+day+"/"+title+"/"+"index.html","wb+") as file:
        content = """<html>

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<META HTTP-EQUIV=REFRESH CONTENT="5;URL=http://admintony.com/{}.html">
</head>
<body>
很抱歉给您带来不便，由于站点URL规则更变，您可访问<a href="http://www.admintony.com/{}.html">{}</a>来进行文章阅读，也可以等待5秒后自动跳转到该页面。

<br>

<span>感谢您对AdminTony的关注与支持</span>
<br>
<br>
<span align="right">AdminTony 致上</span>
</body>
</html>
        """.format(title,title,title)
        #print(content)
        file.write(content.encode("utf-8"))
        print("[+] 已创建完成")
    #print(list[0][1])

def main():
    if len(sys.argv)==1:
        while True:
            path = input("[+] Please Enter URL:")
            if "exit" in path:
                print("[+] Bye ~ ")
                break
            makeDir(path)
    elif len(sys.argv)==2:
        with open(sys.argv[1],"r+",encoding='UTF-8') as f:
            line = f.readlines()
            i = 0
            for l in line:
                i = i+1
                makeDir(l)
            print("[+] 共创建记录{}条".format(i))

if __name__ == '__main__':
    main()