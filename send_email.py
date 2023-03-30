from datetime import datetime
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

import yaml


def send(title, content):
    current_time = datetime.strftime(datetime.now(), "%m-%d %H:%M")

    # 邮件内容编写
    sender_show = title  # 一级：大标题
    subject = f'{current_time}'  # 二级：时间
    message = content  # 三级：邮件正文
    to_addrs = '1203823603@qq.com, 17538056834@163.com'

    # 赋值
    msg = MIMEText(message, 'plain', _charset="utf-8")
    msg["from"] = sender_show
    msg["Subject"] = subject

    # 发件人账号
    with open("/etc/pwd.yaml", 'r') as f:
        Password = yaml.load(f, Loader=yaml.FullLoader)
    mail_server = '网易'
    user = Password[f'{mail_server}']['Account']
    password = Password[f'{mail_server}']['Password']

    # 发送
    with SMTP_SSL(host=Password[f'{mail_server}']['Host'], port=465) as smtp:
        smtp.login(user=user, password=password)
        smtp.sendmail(from_addr=user, to_addrs=to_addrs.split(','), msg=msg.as_string())
