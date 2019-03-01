# -*- coding: utf-8 -*-
# 配置文件类

class mail_setting:
    def __init__(self):
       

        #由于机器端口控制，目前只能用公司邮箱
        # 邮件端口
        # self.port = 465
        self.port = 25

        # 邮件服务器地址
        self.mail_host = 'smtp.163.com'

        # 接收人邮件地址（需要修改）改成你自己的，发送人和接收人可以用一个地址
        self.mail_receive_user = '2499603447@qq.com'

        # self.mail_receive_user = 'shaodd@sina.com'

        # 发送人邮件地址（需要修改）改成你自己的，
        self.mail_send_user='15601599167@163.com'

        #邮件登录用户名 （需要修改）
        self.mail_user = '15601599167@163.com'

        # 登录用密码（需要修改）
        self.mail_pass = "zdz199309092093"
