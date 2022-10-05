<div align="center">

# Bingyue Dictionary
_✨ 一个可以支持变量的词库系统 基于nonebot✨_
    <br></br>
</div>

# 新人必看
如果你不懂python或者如何使用cq<br>
可以前往我博客观看教程<br>
[点击进入](http://blog.bingyue.xyz)<br>

<br></br>

# 一键部署
1.确保你电脑已经拥有``python3.7``或``更高版本``<br>
2.[点击下载部署包](https://github.com/bingqiu456/bingyue-dic/releases/download/0.9.2/bingyue-dic.zip)<br>
3.解压<br>
4.运行``安装依赖库.bat``<br>
5.运行``点我更新.bat``<br>
6.运行``点我启动.bat``<br>
7.在``cq配置文件里`` <br>

找到<br>
```bash
universal: ws://your_websocket_universal.server
```
改成
```bash
universal: ws://127.0.0.1:20000/onebot/v11/ws/
```

<br></br>

# 配置说明
1.打开你的``.env.dev``<br>
2.输入如下``(已有的无需重复操作)``<br>
```bash
owner_dic=0 ##词库主人
admin_dic=["0"] ##词库管理员列表
```
3.保存

<br></br>

# 目前已适配的语法(注:本页变量大全不再更新 请转移我的[博客](http://blog.bingyue.xyz))
- [x] ``如果``
- [x] ``如果尾``
- [x] ``返回``
- [x] ``取变量``   
- [x] ``正则匹配``

<br></br>

# 目前适配的变量(注:本页变量大全不再更新 请转移我的[博客](http://blog.bingyue.xyz))
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
- [x] ``$管理员 %QQ%$`` 判断该qq号在不在词库管理员列表 true则返回qq号 false返回0
- [x] ``%Type%`` 获取消息类型

<br></br>

# 关于最后

- 作者 : Bingyue
- QQ : 35***19417
- github : bingqiu456
- 编写时间 2022-10-02 13:33:02

最后本项目<br>
仅供`研究学习` 请不要`内战`<br>
但我劝你最好去学`python` 编写属于自己的插件<br>
`伪代码`没啥前途 说真的<br>
更新随缘<br>
同时也不要拿去跟某些框架比<br>

