"""
本层是写bingyue dic的消息封装
主要写了%的变量
"""


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