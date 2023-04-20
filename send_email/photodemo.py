import smtplib
# 附件
from email.mime.multipart import MIMEMultipart
# 图片
from email.mime.image import MIMEImage
# 头部
from email.header import Header
# 正文
from email.mime.text import MIMEText

con = smtplib.SMTP_SSL('smtp.qq.com', '465')
con.login('961429475@qq.com', 'gabqqcjkmmljbcch')

sender = '961429475@qq.com'
revices = '961429475@qq.com'

# 创建实例  壳壳
message = MIMEMultipart()

# 把图片拿出来  路径
image1 = open('file/img.png', 'rb').read()
# 把图片附件中
image_da = MIMEImage(image1)
# 图片设置名字
image_da['Content-Disposition'] = 'attachment;filename="qq.png"'
# 把附件放到邮件对象中去
message.attach(image_da)

content = '''
gegergr
'''
cc = MIMEText(content, 'plain', 'utf-8')
message.attach(cc)

message['Subject'] = Header('唯美的图片真好看纳')
message['From'] = Header('秋水1')
message['To'] = Header('秋水2')

# 发送邮件
con.sendmail(sender, revices, message.as_string())

# 发一次
