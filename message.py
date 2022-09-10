"""
本层是写bingyue dic的消息封装
主要写了%的变量
"""

from nonebot import get_driver

class message(object):

    @staticmethod
    async def 群号(self):
        """
        获取群号
        self : 消息内容
        return 返回str的群号
        """
        return str(self.group_id)

    @staticmethod
    async def QQ(self):
        """
        获取QQ号
        self : 消息内容
        return 返回str的群号
        """
        return str(self.get_user_id())

    @staticmethod
    async def Robot(self):
        """
        获取机器人QQ号
        self : 消息内容
        return int 机器人QQ号
        """
        return str(self.self_id)
    
    @staticmethod
    async def 主人(self):
        """
        获取配置文件里的主人
        self : 消息内容
        return : str = 主人qq号
        """
        return str(get_driver().config.dict().get("owner_dic","你还没设置主人"))

    @staticmethod
    async def 管理员(self):
        """
        获取配置文件里的管理员列表
        self : 消息内容
        return : str = 管理员列表
        """
        return str(get_driver().config.dict().get("admin_dic","你还没管理员"))
