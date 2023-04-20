# 发送附件  pytest+jenkins 下载工具就行  json文件
import os
import shutil
import smtplib
import zipfile
from email.mime.base import MIMEBase
from email import encoders
# 发送附件
from email.mime.multipart import MIMEMultipart
# 发送正文
from email.mime.text import MIMEText
# 头部
from email.header import Header


def zipDir(dirpath, outFullName):
    '''
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName:  压缩文件保存路径+XXXX.zip
    :return: 无
    '''
    zip = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标和路径，只对目标文件夹下边的文件及文件夹进行压缩（包括父文件夹本身）
        this_path = os.path.abspath('.')
        fpath = path.replace(this_path, '')
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()


def server_pre(msg):
    """邮件服务器基础设置"""
    server = smtplib.SMTP_SSL('smtp.qq.com', '465')
    server.login('961429475@qq.com', 'gabqqcjkmmljbcch')
    fromAddr = '961429475@qq.com'  # 发件人
    server.send_message(msg)
    server.quit()


def send_listing():
    """发送邮件"""
    global msg_list
    msg_list = MIMEMultipart()
    msg_list['From'] = '961429475@qq.com'
    msg_list['To'] = '961429475@qq.com'
    # msg_list['To'] = '**@189.cn, **@qq.com'
    msg_list['Subject'] = '-----软件测试报告-------'
    body = '++++++++++++++++-----------------------------测试报告-------------------------------++++++++++++++++++'
    msg_list.attach(MIMEText(body))
    with open("../send_filezip/report.zip", 'rb') as f:
        # 这里附件的MIME和文件名，这里是xls类型
        mime = MIMEBase('zip', 'zip')
        # 加上必要的头信息
        mime.add_header('Content-Disposition', 'attachment', filename=('gb2312','', '测试报告.zip'))
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来
        mime.set_payload(f.read())
        # 用Base64编码
        encoders.encode_base64(mime)
        msg_list.attach(mime)
    server_pre(msg_list)
    print(">>>发送邮件成功！")

if __name__ == '__main__':
    dirpath = os.path.dirname(os.path.dirname(__file__))+'/report_allure'
    outFullName = os.path.dirname(os.path.dirname(__file__))+'/send_filezip/report.zip'
    zipDir(dirpath, outFullName)
    print('>>>压缩文件成功！')
    send_listing()
    # # os.remove(outFullName)
    # # shutil.rmtree(r'C:\Users\Administrator\Desktop\报表\周末日报')
    # # print('>>>删除文件成功！')
