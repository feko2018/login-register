import os
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

def send_txt_mail():
    send_mail(
        '来自txt邮件', #第一个参数是邮件主题subject
        '欢迎访问',    #第二个参数是邮件具体内容
        'ttestt007@163.com',  #第三个参数是邮件发送方，需要和你settings中的一致
        ['1282806692@qq.com'], #第四个参数是接受方的邮件地址列表
    )
def send_html_mail():
    subject = '来自html邮件2'
    from_email =  'ttestt007@163.com'
    to =  ['1282806692@qq.com']
    text_content = '欢迎访问http://www.baidu.com'
    html_content = '<p>欢迎访问<a href="http://www.baidu.com" target=blank>http://www.baidu.com</a></p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, to) #text_content是用于当HTML内容无效时的替代txt文本
    msg.attach_alternative(html_content, "text/html")
    try:
        msg.send()
        print('邮件发送成功')
    except:
        print('邮件发送失败')
if __name__ == '__main__':
    send_html_mail()
