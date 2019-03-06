from Mail import *
import configparser
import sys
import os

cf = configparser.ConfigParser()
cf.read("mail.conf")
mail_sender = cf.items("Email")

m = Mail(mail_sender[0][1], mail_sender[1][1], mail_sender[2][1], mail_sender[3][1], mail_sender[4][1])

#邮件发送信息设置
to = input("To:")
mail_tolist = []
mail_tolist.append(to)
cc = input("Cc:")
cc_tolist =[]
subject = input("Subject:")

#邮件主体部分设置
body = ""
print("Body:")
while True:
    temp = input()
    if temp == "":
        break
    body += temp.replace("\t", "    ") + "\n"

if len(sys.argv) <= 1:
    # 默认不带参数，发送不带附件的邮件
    result = m.SendMail(subject, body, mail_tolist, cc_tolist)

elif sys.argv[1] == 'attach':
    # 发送带附件的邮件
    # os.system("dialog --title \"Pick Files\" --fselect /root/ 7 40 >> /tmp/sendmail.files")
    annex = input("Annex(Absolute path):")
    fileList = []
    fileList.append(annex)
    # 检查文件是否存在
    for f in fileList:
        if not os.path.isfile(f):
            # 文件不存在的处理方法
            print("%s FILE NOT FOUND! PLEASE CHECK IT PATH" % f)
    result = m.SendMailAttach(mail_tolist, subject, body, fileList, cc_tolist)
elif sys.argv[1] == 'html':
    # 发送html邮件
    print("html")

print(result)


# to = "2499603447@qq.com"
# cc = ""
# subject = "hello"
#
# #邮件主体部分设置
# body = ""
# print("Body:")
# #body_head = "\t" + input() + "\n"
# while True:
#     temp = input()
#     if temp == "":
#         break
#     body += temp.replace("\t", "    ") + "\n"
#
# fileName = "/home/dezhou/workspace/email/20190221/mail.txt"
# result = m.test(body, subject, to, fileName)
# print(result)
