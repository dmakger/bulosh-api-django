from celery import shared_task
from django.core.mail import send_mail

from api.settings import EMAIL_HOST_USER


@shared_task
def send_registration_email(email):
    subject = 'Регистрация успешна'
    message = 'Вы успешно зарегистрированы!'
    sender = EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, sender, recipient_list)
