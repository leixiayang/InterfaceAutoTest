from django.conf import settings

def send_email(email, code):

    from django.core.mail import EmailMultiAlternatives

    subject = '来自YC自动化测试平台的注册确认邮件'

    text_content = '''如果无法注册或者跳转，请联系管理员！'''

    html_content = '''
                    <a href="http://{}/confirm/?code={}" target=blank>点击确认</a>
                    <p>此链接有效期为{}天！</p>
                    '''.format('127.0.0.1:8089', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()