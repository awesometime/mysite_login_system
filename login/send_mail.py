# 本模块仅供测试 通过Django发送邮件 使用，不属于项目必须文件
import os
from django.core.mail import EmailMultiAlternatives
# from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    subject, from_email, to = '邮件subject', '2438529228@qq.com', '2438529228@qq.com'
    text_content = '欢迎访问www.baidu.com！'
    html_content = '<p>欢迎访问<a href="http://www.baidu.com" target=blank>www.baidu.com</a>,专注于技术,热爱生活！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print('success')
