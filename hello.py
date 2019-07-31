# -*- encoding: utf-8 -*-
# 1、导包
from flask import Flask
from day01.config import *


# 2、实例化app
app = Flask(__name__)
# app.config['DEBUG'] = True

# 1、通过对象加载配置.类可以继承，代码重用性高
app.config.from_object(ProConfig)

# 2、通过文件来加载配置
# app.config.from_pyfile('c.txt')

# 3、通过环境变量来加载 key=config
# app.config.from_envvar('config')


# 3、配置路由，网址、URL
# 视图函数
@app.route("/")
def index():
    return '<h1>Hello World!AAAAAAA</h1>'


# 4、程序入口项目启动
if __name__ == '__main__':
    # debug=True 开启调试模式
    # prot 修改端口号
    # host
    app.run()
