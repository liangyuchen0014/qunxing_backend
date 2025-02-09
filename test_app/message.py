# 发送邮箱验证码
import random

from django.core.mail import send_mail


def send_sms_code(to_email, sms_code):
    """
    发送邮箱验证码
    :param to_mail: 发到这个邮箱
    :return: 成功：0 失败 -1
    """
    EMAIL_FROM = "lightseeker157@163.com"  # 邮箱来自
    email_title = '群星验证码'
    email_body = "您的邮箱验证码为：{0}, 该验证码有效时间为两分钟，请及时进行验证。".format(sms_code)
    # send_status函数作用
    send_status = send_mail(email_title, email_body, EMAIL_FROM, [to_email])
    return send_status


def send_reminder_email(to_email, room, date):
    """
    发送邮箱验证码
    :param to_mail: 发到这个邮箱
    :return: 成功：0 失败 -1
    """
    EMAIL_FROM = "lightseeker157@163.com"  # 邮箱来自
    email_title = '租赁到期提醒'
    email_body = "您对房间{0}的租赁将于31天后（{1}）到期。".format(room, date)
    # send_status函数作用
    send_status = send_mail(email_title, email_body, EMAIL_FROM, [to_email])
    return send_status
