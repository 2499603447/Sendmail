# -*- coding: UTF-8 -*-
import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import configparser

class Mail:
    '''
    self.port = "25" # 设置默认端口号
    self.mail_host = "smtp.163.com"  # 设置服务器
    self.mail_sender = 'xiaowang@sina.com'  # 发送者
    self.mail_user = "xiaowang"  # 用户名
    self.mail_pass = "XXXXX"  # 授权码
    '''

    def __init__(self, port=25, mail_host="smtp.163.com", mail_sender="15601599167@163.com", mail_user="15601599167@163.com", mail_pass="zdz199309092093"):

        self.port = port
        self.mail_host = mail_host
        self.mail_sender = mail_sender
        self.mail_user = mail_user
        self.mail_pass = mail_pass

    def SendHtmlMail(self, mail_tolist, mail_subject, mail_body, mail_cclist, mail_bcclist):
        '''
        发送Html邮件
        :param mail_tolist: 接收者邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']
        :param mail_subject: 邮件主题
        :param mail_body: 邮件体主题内容
        :param mail_cclist: 抄送邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']，默认不传
        :param mail_bcclist: 密送邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']，默认不传
        :return:
        '''
        message = MIMEText(mail_body, _subtype='html', _charset='gb2312')
        message['Subject'] = mail_subject
        message['From'] = self.mail_sender
        if len(mail_cclist) > 0:
            message['Cc'] = ",".join(mail_cclist)
            mail_tolist.extend(mail_cclist)
        if len(mail_bcclist) > 0:
            message['Bcc'] = ",".join(mail_bcclist)
            mail_tolist.extend(mail_bcclist)

        try:
            smtpObj = smtplib.SMTP(self.mail_host, self.port)
            # smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            # smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.mail_sender, mail_tolist, message.as_string())
            smtpObj.close()
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件")

    def SendMailAttach(self, mail_tolist, mail_subject, mail_body, fileList, mail_cclist):
        '''
        发送带附件的邮件
        :param mail_tolist: 接收者邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']
        :param mail_subject: 邮件主题
        :param mail_body: 邮件体主题内容
        :param fileList: 附件列表，就文件名列表（包含路径）
        :param mail_cclist: 抄送邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']，默认不传
        :return:
        '''
        msg = MIMEMultipart()
        message = MIMEText(mail_body, _subtype='plain', _charset='utf-8')
        msg.attach(message)

        # 构造附件
        for f in fileList:
            if os.path.isfile(f):
                att = MIMEText(open(f, 'rb').read(), 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'
                att["Content-Disposition"] = 'attachment;filename=' + os.path.basename(f)
                msg.attach(att)

        msg['Subject'] = mail_subject
        msg['From'] = self.mail_sender
        msg['To'] = ",".join(mail_tolist)
        if len(mail_cclist) > 0:
            msg['Cc'] = ",".join(mail_cclist)
            mail_tolist.extend(mail_cclist)

        result = ''
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(self.mail_sender, mail_tolist, msg.as_string())
            server.close()
            result = '邮件发送成功'

        except smtplib.SMTPException as e:
            result = 'Error: 无法发送邮件:'
        return result

    def SendMail(self, mail_subject, mail_body, mail_tolist, mail_cclist):
        '''
        发送普通邮件
        :param mail_subject: 邮件主题
        :param mail_body: 邮件体主题内容
        :param mail_tolist: 接收者邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']
        :param mail_cclist: 抄送邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']，默认不传
        :return:
        '''
        message = MIMEText(mail_body, _subtype='plain', _charset='utf-8')
        message['Subject'] = mail_subject
        message['From'] = self.mail_sender
        if mail_tolist:
            message['To'] = ",".join(mail_tolist)
        if len(mail_cclist) > 0:
            message['Cc'] = ",".join(mail_cclist)
            mail_tolist.extend(mail_cclist)

        result = ''
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(self.mail_sender, mail_tolist, message.as_string())
            server.close()
            result = '邮件发送成功'
            # print "邮件发送成功"
        except smtplib.SMTPException as e:
            result = 'Error: 无法发送邮件'
        return result
