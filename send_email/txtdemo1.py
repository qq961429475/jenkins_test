# 邮件
# 1.用python代码发送邮件 文本邮件
# 2.发送html邮件
# 3.发送附件和图片

# smtplib  smtp进行封装
import smtplib
# 发送邮件正文
from email.mime.text import MIMEText
# 发送头部
from email.header import Header

# 创建邮箱服务器  邮局  SMTP_SSL(邮箱链接地址，端口号)
# 邮箱链接地址：smtp.xx.com  端口号:自己去查
# 163邮箱  网易邮箱  qq邮箱
con = smtplib.SMTP_SSL('smtp.qq.com', '465')
# 登录邮箱 用户名和密码
# 163邮箱  qq邮箱 设置一下 用户名是邮箱名  密码：授权密码  qq邮箱--设置--账号--POP3/SMTP服务开启
con.login('961429475@qq.com', 'gabqqcjkmmljbcch')
# print(con)

# 发送者账号
sender = '961429475@qq.com'
# 接受者账号
recevier = ['961429475@qq.com']

# 邮件的内容  _text文本内容 正文  _subtype 文件类型 plain 文本 txt html base64
message = MIMEText(_text='最后一节课你开不开心，反正我不开心', _subtype='plain', _charset='utf-8')

# 设置头部 设置标题
message['Subject'] = Header('我还是很忧伤，高兴不起来了')
# 发件人
message['From'] = Header('秋水1<2804555260@qq.com>')
# 接受人 的信息
message['To'] = Header('秋水2')

try:
    # 发送邮件  由谁发送  邮局发送 con  发送邮件失败
    con.sendmail(sender, recevier, message.as_string())
    print('发送邮件成功')
except Exception:
    print('无法发送邮件')

# 文本邮件  封装邮件  服务器链接 init方法
# 发送html文件
