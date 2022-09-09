import httpx , os , random
from nonebot import get_bot
from nonebot.adapters.onebot.exception import ActionFailed
from nonebot.log import logger
"""
本层是写 bingyuedic 的$变量封装
查看帮助 还没有
这里是外部操作
"""

class Task:

    @staticmethod
    async def 禁(self:str):
        """
        禁言
        self : ["群号","QQ","秒数"]
        return 直接禁言
        """
        self = self.split(maxsplit=2)
        try:
            await get_bot().call_api("set_group_ban",**{
                "group_id":self[0],
                "user_id":self[1],
                "duration":self[2],
            })
        except(ActionFailed):
            logger.error("禁言错误 这有可能是机器人权限不足引起的")
            return ""
        else:
            return ""


    @staticmethod
    async def 读(self:str):
        """
        读取文件
        self : ["文件路径","索引","内容"]
        return 不存在是时候直接返回内容 存在即返回现在值
        """
        lujing = self.split(maxsplit=2)
        try:
            with open(lujing[0], "a+", encoding="utf_8") as e:
                if (e.read()) == "":
                    return lujing[2]
                else:
                    return e.read()
        except(FileExistsError,NotADirectoryError):
            return lujing[2]

    @staticmethod
    async def 随机数(self:str):
        """
        生成随机数
        self : ["随机数最大值","随机数最小值"]
        return int
        """
        self = self.split(maxsplit=1)
        return str(random.randint(int(self[0]),int(self[1])))

    @staticmethod
    async def 改(self:str):
        """
        读取文件
        self : ["群号","QQ号","昵称"]
        return 失败会返回错误提示 成功则无操作
        """
        self = self.split(maxsplit=2)
        try:
            await get_bot().call_api("set_group_card", **{
                "group_id": self[0],
                "user_id": self[1],
                "card": self[2],
            })
        except(ActionFailed):
            logger.error("改名错误 这有可能是机器人权限不足引起的")
            return ""
        else:
            return ""


    @staticmethod
    async def 访问(url:str):
        """
        访问外部链接
        url : 网站连接
        return 访问内容
        """
        return await httpx.AsyncClient().get(url=url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}).text