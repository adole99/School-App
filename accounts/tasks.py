from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger
from .email import send_confirmation_mail
from celery import shared_task
from time import sleep

logger = get_task_logger(__name__)

@shared_task(name="send_confirmation_mail_task")
def send_confirmation_mail_task(username, email):
	sleep(20)
	logger.info("Sent Confirmation Email")
	return send_confirmation_mail(username, email)