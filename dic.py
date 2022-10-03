"""
本层是bingyue dic的核心处理
主要描写处理变量的
"""
import json
import re
import os
import httpx
from nonebot.adapters.onebot.v11 import Event
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11 import Message
from nonebot import  on_message
from nonebot.log import logger
from nonebot.params import EventPlainText
from nonebot.matcher import Matcher
from . import variable2
from . import message



def opendictxt(): ##打开词库
    try:
        with open("./dic/dic.txt","r",encoding="utf_8") as f:
            ## 打开词库 作为全局缓存
            global qrdic_json
            f = f.readlines()
            if f[len(f)-1].find("\n")==-1:
                f.append("\n")
                f[len(f)-2] = f[len(f)-2]+"\n"
            f.append("\n")
            qrdic_json = f
            return qrdic_json
    except(FileNotFoundError):
        qrdic_json=False
        return False

opendictxt()

async def duquming(): ##读取命令
    h = qrdic_json
    if h == False:
        return logger.error("读取文件失败")

    a = h
    b = [] ##词库命令
    t = {} ##索引key
    c = len(a)-1
    logger.debug("加载词库成功")
    global p
    p = False
    for i in range(c):
        """
        匹配第一行的指令
        保存索引 方便下次检索
        """
        if i == 0 and a[i] != "\n":
            v = str(str(a[i]).replace(str(a[i])[-1],"").replace("\ufeff",""))
            b.append(v)
            t[v] = str(i)

        if a[i] == str('\n'):
            p = True

        i = i+1
        if p == True and a[i] !="\n":
            v = str(str(a[i]).replace(str(a[i])[-1], ""))
            b.append(v)
            t[v] = str(i)

        p = False
    return {"qrmingn":str(b),"key":str(t)}

async def chuliciku(msg,event): ##读取词库
    """
    匹配词库
    msg : 消息内容纯文本
    event : 消息的附带参数
    return 返回json数组 是处理好后的词条
    """
    global judge_code
    global str_1
    vv = {}
    o = await duquming()
    judge_code = False
    qr = json.loads(str(o["qrmingn"]).replace("'",'"'))
    if await regex_zhiling(a=qr,b=str(msg))==False:
        await Matcher.finish()

    vv.update(await regex_zhiling(a=qr,b=str(msg)))
    k = []
    dic = json.loads(str(o["key"]).replace("'",'"'))
    dic1 = qrdic_json
    i = (int(dic[vv["zhiling"]])+1)
    while i < len(dic1):
        if dic1[i]=="\n" :
            vv = {}
            logger.success("消息打印成功")
            return k
        else:
            str_1 = str(dic1[i]).replace(str(dic1[i][-1]), "").replace("\\n","\n").replace("\\r","\r")
            Rstr = re.findall(r"[%](.*?)[%]", str_1)
            if str_1 == "如果尾" and judge_code == True:
                judge_code = False
                str_1 = ''

            if judge_code == True:
                str_1 = ''

            for u in Rstr:
                logger.success(f"词库变量{u}加载成功")
                try:
                    if u in vv:
                        str_1 = str_1.replace("%" + u + "%", vv[str(u)])
                        logger.success(f"自创变量{u}加载成功")
                    str_1 = str_1.replace("%" + u + "%", await message.message.__dict__.get(u).__func__(event))
                    logger.success(f"词库变量{u}加载成功")
                except(KeyError,TypeError,AttributeError):
                    str_1 = str_1

            ORstr = re.findall(r"[$](.*?)[$]", str_1)
            for v in ORstr:
                try:
                    logger.success(f"词库变量{v}加载成功")
                    o = v.split(' ',1)
                    str_1 =  str_1.replace("$"+v+"$",await variable2.Task.__dict__.get(o[0]).__func__(event,o[1]))
                except(KeyError,AttributeError,TypeError):
                    str_1 = str_1

            l = str_1.split(":",maxsplit=1)
            if l[0]=="如果":
                logger.warning("判断成功触发 开始过滤")
                if await judge(p=l[1])==True and judge_code== False:
                    str_1 = ''
                else:
                    str_1 = ''
                    judge_code = True

            if len(l[0])==1 and len(l)==2:
                vv[str(l[0])] = str(l[1])
                str_1 = ''

            if str_1 == "返回" and judge_code == False:
                vv = {}
                logger.success("消息打印成功 [返回]")
                return k
        k.append(str_1)
        i = i+1


async def judge(p): ##判断
    p = str(p).replace("|", '" or "').replace("&", '" and "').replace("==", '"=="')  ##转义符
    return eval('"'+p+'"')

async def regex_zhiling(a,b): ##指令中的正则匹配
        vv = {}
        for a in a:
            o = re.findall(a, b)
            if o == []:
                continue
            if o[0] == a:
                vv["zhiling"]=a
                vv[str("参数-1")] = a
                return vv
            i = 0
            vv["zhiling"]=a
            for o in o:
                vv[str("参数") + str(i)] = o
                return vv

        return False


test = on_message(priority=1)
@test.handle()
async def _(event: Event,group:GroupMessageEvent,A:Message=EventPlainText()):
    message = event.get_message()
    ##获取消息的参数
    b = await chuliciku(msg=A,event=group)
    ##给词库匹配
    if str(b)=="['']":
        logger.success("触发成功 但返回了空消息")
        await test.finish()
    logger.success(f'词库指令{str(message)}已触发')
    await test.finish(b)
