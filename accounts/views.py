from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from accounts.forms import SignupForm
from accounts.models  import CustomUser, Roles
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import login, authenticate
from django.template.loader import render_to_string, get_template
from django.template import Context
from django.core.mail import send_mail
from .tokens import account_activation_token
from django.conf import settings
from accounts.decorators import student_required, teacher_required
# Create your views here.
def index(request):
	return render(request, 'index.html')

def login_view(request):
	if request.user.is_authenticated:
	    user = request.user
	    return redirect(reverse(f'accounts:{user.role}-home'))
	if request.method == "POST":
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(username=username, password=password)
	    if user is not None:
	        login(request, user)
	        return redirect(f'accounts:{user.role}-home')
	    else:
	        messages.success(request, 'Please activate your account.')
	        return redirect('accounts:login')
	return render(request, 'registration/login.html')

def register(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			role = form.cleaned_data['role']
			user = form.save(commit=False)
			user.save()
			Roles.objects.get_or_create(role=role, user=user)
			current_site = get_current_site(request)
			subject = 'Activate Your Book-app Account'
			message = render_to_string('email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
			})
			user.email_user(subject, message)
			messages.success(request, 'Please confirm your email to complete registration')
			return redirect("accounts:login")
	form = SignupForm()
	return render(request, "registration/register.html", {"form": form})

def activate_account_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save() 
        login(request, user)
        return redirect(f'accounts:{user.role}-home')
    else:
        return HttpResponse('Activation link is invalid')

# def dashboard(request):
#     return render(request, "accounts/dashboard.html")

@student_required
def student_home(request):
    return render(request, "accounts/student/dashboard.html")

def student_profile(request):
	return render(request, "accounts/teacher/teacher-profile.html")

@teacher_required
def teacher_home(request):
    return render(request, "accounts/teacher/dashboard.html")

def teacher_profile(request):
	return render(request, "accounts/teacher/teacher-profile.html")