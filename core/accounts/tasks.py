from celery import shared_task
from mail_templated import send_mail


@shared_task
def send_verified_email(template_name, mail_context, from_email, to_email):
    send_mail(
        template_name=template_name,
        context=mail_context,
        from_email=from_email,
        recipient_list=to_email,
    )
