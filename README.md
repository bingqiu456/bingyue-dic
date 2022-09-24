<div align="center">

# Bingyue Dictionary
_✨ 一个可以支持变量的词库系统 ✨_
    <br></br>
</div>



# 如何安装?如何使用?
1.首先确保电脑上有``python3.7或者更高版本``

2.打开你的``cmd``

3.先把镜像站切换到清华源
```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

4.然后安装我的库
```bash
pip install bingyue-dic
```

5.如果出现``Requirement already``或者``Successfully``就说明已经安装成功

6.加载到nonebot上

打开你的`bot.py` 加上这条语句
```bash
nonebot.load_plugin("bingyue_dic")
```

同时在你的`.env.dev（nonebot配置文件）`加上
```bash
owner_dic=1212212
admin_dic=["1001","10212"]
```

7.在你的nonebot机器人目录下 新建一个叫``dic``的文件夹

再新建一个`dic.txt`

就能开始编写词库了

<br></br>

# 目前适配的变量
- [x] ``%QQ%``：发言人QQ
- [x] ``%Robot%`` 机器人QQ
- [x] ``%群号%`` 获取qq群号
- [x] ``$禁 群号 QQ 秒数$`` 群里禁言
- [x] ``$读 路径/路径 a 0$`` 读取文件
- [x] ``$随机数 0 1$`` 随机数
- [x] ``$改 群号 QQ 名字$`` 改群里名字
- [x] ``$访问 网址$`` 访问链接
- [x] ``%管理员%`` 获取管理员列表 以json形式返回
- [x] ``%主人%`` 获取主人qq号
- [x] ``$写 路径/路径 a 0$`` 写文件
- [x] ``$群头衔 群号 QQ 内容$`` 给头衔的
- [x] ``$全体禁言 群号 开$`` 全体禁言
- [x] ``$获取 消息类型 第几个$`` 获取消息参数

<br></br>

# 未来打算适配的
``待补充``


<br></br>

# 关于最后

- 作者 : Bingyue
- QQ : 35***19417
- github : bingqiu456
- 编写时间 2022-09-09 22:01:10

最后本项目<br>
仅供`研究学习` 请不要`内战`<br>
但我劝你最好去学`python` 编写属于自己的插件<br>
`伪代码`没啥前途 说真的<br>
更新随缘<br>
同时也不要拿去跟某些框架比<br>
