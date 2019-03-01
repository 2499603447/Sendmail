# -*- coding: UTF-8 -*-
import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import mail_setting

class Mail:
    '''
    self.mail_host = "smtp.sina.com"  # 设置服务器
    self.mail_user = "xiaowang"  # 用户名
    self.mail_pass = "XXXXX"  # 口令
    self.mail_sender = 'xiaowang@sina.com'  # 发送者
    '''

    def __init__(self, mail_host="210.77.136.200", mail_user="user", mail_pass="pass",
                 mail_sender="da山<das@ctrchina.cn>", port=465):
        # 第三方 SMTP 服务
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.mail_sender = mail_sender
        self.port = port


    def SendHtmlMail(self, mail_tolist, mail_subject, mail_body, fileList, mail_cclist, mail_bcclist):
        '''
        发送Html邮件
        :param mail_tolist: 接收者邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']
        :param mail_subject: 邮件主题
        :param mail_body: 邮件体主题内容
        :param fileList: 附件列表，就文件名列表（包含路径）
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
        :param mail_bcclist: 密送邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']，默认不传
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
        # if len(mail_bcclist) > 0:
        #     msg['Bcc'] = ",".join(mail_bcclist)
        #     mail_tolist.extend(mail_bcclist)

        message = ''
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(self.mail_sender, mail_tolist, msg.as_string())
            server.close()
            result = '邮件发送成功'

        except smtplib.SMTPException as e:
            # print "Error: 无法发送邮件", e
            message = 'Error: 无法发送邮件:'
        return message

    def SendMail(self, mail_subject, mail_body, mail_tolist,mail_cclist):
        '''
        发送普通邮件
        :param mail_tolist: 接收者邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']
        :param mail_subject: 邮件主题
        :param mail_body: 邮件体主题内容
        :param fileList: 附件列表，就文件名列表（包含路径）
        :param mail_cclist: 抄送邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']，默认不传
        :param mail_bcclist: 密送邮件列表，如:['xiaoli@sina.com','xiaoMa@qq.com']，默认不传
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
            server.login(self.mail_user,self.mail_pass)
            server.sendmail(self.mail_sender, mail_tolist, message.as_string())
            server.close()
            result = '邮件发送成功'
            # print "邮件发送成功"
        except smtplib.SMTPException as e:
            result = 'Error: 无法发送邮件'
        return result

    def test(self,mail_body,mail_subject,mail_sendto_user,fileName):

        fileList = []
        fileList.append(fileName)

        mail_tolist = []
        mail_tolist.append(mail_sendto_user)

        # 多个人，中间用逗号分隔
        # cc_tolist = ['xx<aa@CTRCHINA.CN>','dd<dd@CTRCHINA.CN>']
        cc_tolist =[]
        mail_bcclist = []
        print("Subject:%s\n" % mail_subject)
        print("Body:%s\n" % mail_body)
        print("To:%s\n" % mail_tolist)
        print("Cc:%s\n" % cc_tolist)
        #result = self.SendMail( mail_subject, mail_body, mail_tolist,cc_tolist)
        result = self.SendMailAttach(mail_tolist,mail_subject, mail_body,fileList, cc_tolist)
        return result


setobj = mail_setting.mail_setting()
m = Mail(setobj.mail_host,setobj.mail_user,setobj.mail_pass,setobj.mail_send_user,setobj.port)
#result = m.test('信息1',u'小测试测试',setobj.mail_receive_user)
fileName="/home/dezhou/workspace/email/20190221/mail.txt"
result = m.test('信息1',u'小测试测试',setobj.mail_receive_user,fileName)
print (result)
