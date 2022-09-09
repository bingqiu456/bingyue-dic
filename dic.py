"""
本层是bingyue dic的核心处理
主要描写处理变量的
"""
import json ,re ,os , httpx
from nonebot.adapters.onebot.v11 import Event , GroupMessageEvent , Message
from nonebot import  on_message , get_driver
from nonebot.log import logger
from nonebot.params import EventPlainText
from . import variable2,message


global admin_dic
global onwer_dic
admin_dic = str(get_driver().config.dict().get("admin_dic",[]))
onwer_dic = str(get_driver().config.dict().get("owner_dic",0))

def opendictxt(): ##打开词库
    try:
        with open("./dic/dic.txt","r",encoding="utf_8") as f:
            ## 打开词库 作为全局缓存
            global qrdic_json
            qrdic_json = f.readlines()
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
    logger.success("加载词库成功")
    global p
    p = False
    for i in range(c):
        """
        匹配第一行的指令
        保存索引 方便下次检索
        """
        if i == 0 and a[i] != "\n":
            v = str(str(a[i]).replace(str(a[i])[-1],""))
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
    global str_1
    o = await duquming()
    qr = json.loads(str(o["qrmingn"]).replace("'",'"'))
    if str(msg)  not in qr:
        return False
    else:
        k = []
        dic = json.loads(str(o["key"]).replace("'",'"'))
        dic1 = qrdic_json
        i = (int(dic[msg])+1)
        while i < len(dic1)-1:
            if dic1[i] == "\n":
                logger.success("消息打印成功")
                return k
            else:
                str_1 = str(dic1[i]).replace(str(dic1[i][-1]), "").replace("\\n","\n").replace("\\r","\r")
                Rstr = re.findall(r"[%](.*?)[%]", str_1)
                try:
                    for u in Rstr:
                        logger.success(f"词库变量{u}加载成功")
                        str_1 = str_1.replace("%"+u+"%", await message.message.__dict__.get(u).__func__(event))
                    ORstr = re.findall(r"[$](.*?)[$]", str_1)

                    for v in ORstr:
                        logger.success(f"词库变量{v}加载成功")
                        o = v.split(' ',1)
                        str_1 =  str_1.replace("$"+v+"$",await variable2.Task.__dict__.get(o[0]).__func__(o[1]))
                except(AttributeError):
                    pass
                k.append(str_1)
            i = i+1

test = on_message(priority=1)
@test.handle()
async def _(event: Event,group:GroupMessageEvent,A:Message=EventPlainText()):
    message = event.get_message()
    ##获取消息的参数
    b = await chuliciku(msg=A,event=group)
    ##给词库匹配
    if b == False :
        logger.success(f"未触发词库指令")
        await test.finish()
    else:
        if str(b)=="['']":
            logger.success("触发成功 但返回了空消息")
            await test.finish()
        logger.success(f'词库指令{str(message)}已触发')
        await test.finish(b)
