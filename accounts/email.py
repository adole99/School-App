from django.template import Context
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.conf import settings
from .models import CustomUser
from django.contrib.sites.models import Site

def send_confirmation_mail(username, email):
    user = CustomUser.objects.get(username=username)
    current_site = Site.objects.get_current().domain
    message={
        'username': username,
        'email': email,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    }
    email_subject = 'Activate your School-App'
    email_body = render_to_string('email.html', message)

    email = EmailMessage(
        email_subject, email_body, 
        settings.DEFAULT_FROM_EMAIL, [email],
    )
    return email.send(fail_silently=False)