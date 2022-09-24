import httpx
import random
import os
from nonebot import get_bot
import configparser
"""
本层是写 bingyuedic 的$变量封装
查看帮助 还没有
这里是外部操作
"""

async def messagetype(event, message_type, int):
    """
    消息遍历器
    event: 消息
    type: 要获取的类型
    int: 第几个
    return : Any
    """
    event = event.get_message()
    a = list(event)
    global i
    i = 0
    o = {"text":"text","image":"url","face":"id"} ##支持的消息类型
    for a in a:
        if a.type == message_type and i == int:
            o = o[message_type]
            return a.data[o]

        if a.type == message_type:
            i = i + 1
    return ''

class Task:

    @staticmethod
    async def 禁(event,self: str):
        """
        禁言
        self : ["群号","QQ","秒数"]
        return 直接禁言
        """
        self = self.split(maxsplit=2)
        await get_bot().call_api("set_group_ban",**{
                "group_id": self[0],
                "user_id": self[1],
                "duration": self[2],
            })
        return ""

    @staticmethod
    async def 读(event,self: str):
        """
        读取文件
        self : ["文件路径","索引","内容"]
        return 不存在是时候直接返回内容 存在即返回现在值
        """
        try:
            lujing = self.split(" ",maxsplit=2)
            n = configparser.ConfigParser()
            n.read(lujing[0], encoding='utf-8')
            get = lujing[1]
            return str(dict(n.items("bingyue-dic-free-binhe"))[get])
        except(configparser.NoSectionError,FileNotFoundError,FileExistsError):
            return lujing[2]


    @staticmethod
    async def 随机数(event,self: str):
        """
        生成随机数
        self : ["随机数最大值","随机数最小值"]
        return int
        """
        self = self.split(maxsplit=1)
        return str(random.randint(int(self[0]), int(self[1])))

    @staticmethod
    async def 改(event,self: str):
        """
        改群昵称
        self : ["群号","QQ号","昵称"]
        return 失败会返回错误提示 成功则无操作
        """
        self = self.split(maxsplit=2)
        await get_bot().call_api("set_group_card", **{
                "group_id": self[0],
                "user_id": self[1],
                "card": self[2],
            })
        return ""

    @staticmethod
    async def 访问(url: str):
        """
        访问外部链接
        url : 网站连接
        return 访问内容
        """
        return await httpx.AsyncClient().get(url=url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" }).text

    @staticmethod
    async def 写(event,self: str):
        """
        写入配置文件
        self : [路径,索引,内容]
        return : ''
        """
        a = self.split(maxsplit=2)
        if os.path.exists(a[0]) == False:
            os.makedirs(a[0])
            os.rmdir(a[0])
        n = configparser.ConfigParser()
        n.read(a[0], encoding='utf-8')
        try:
            n.set("[bingyue-dic-free-binhe]", str(a[1]), str(a[2]))
        except(configparser.NoSectionError):
            with open(a[0], "w+", encoding="utf_8") as f:
                f.write(str("[bingyue-dic-free-binhe]"))
                f.close()

        n.read(a[0], encoding='utf-8')
        n.set("bingyue-dic-free-binhe", str(a[1]), str(a[2]))
        with open(a[0], "w+", encoding="utf_8") as f:
            n.write(f)
            f.close()
        return ''

    @staticmethod
    async def 群头衔(event,self: str):
        """
        修改群头衔
        self : [群号,QQ,群头衔内容]
        return : ''
        """
        self = self.split(maxsplit=2)
        await get_bot().call_api("set_group_special_title", **{
            "group_id": self[0],
            "user_id": self[1],
            "special_title": self[2],
        })
        return ''


    @staticmethod
    async def 获取(event,self:str):
        """
        获取消息参数
        支持 AT image file等文件读取
        self : [消息类型,第几个]
        return : any
        """
        self = self.split(maxsplit=1)
        return await messagetype(event=event,message_type=self[0],int=int(self[1]))

    @staticmethod
    async def 全体禁言(event,self:str):
        """
        全体禁言
        self : [群号,开或关]
        return : ''
        """
        self = self.split(maxsplit=1)
        o = {"开":"true","关":"false"}
        o = o[self[1]]
        await get_bot().call_api("set_group_whole_ban",**{
            "group_id": self[0],
            "enable": o
        })
        return ''
