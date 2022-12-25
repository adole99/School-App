from django.urls import reverse
from django.shortcuts import redirect,render
from django.contrib import messages

from accounts.models import CustomUser


def student_required(func):
    """
    Decorator for views that checks that the logged-in user is a contributor,
    redirects to the log-in page if necessary.
    """

    def wrap(request, *args, **kwargs):

        if request.user.is_anonymous:
            return redirect(reverse('accounts:login'))
        if request.user.role == 'student':
            pass
        else:
            return redirect(reverse('accounts:login'))
        
        return func(request, *args, **kwargs)

    return wrap

def teacher_required(func):
    """
    Decorator for views that checks that the logged-in user is a contributor,
    redirects to the log-in page if necessary.
    """

    def wrap(request, *args, **kwargs):

        if request.user.is_anonymous:
            return redirect(reverse('accounts:login'))
        if request.user.role == 'teacher':
            pass
        else:
            return redirect(reverse('accounts:login'))
        
        return func(request, *args, **kwargs)

    return wrap