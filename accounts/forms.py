from django import forms
from accounts.models import CustomUser, StudentProfile, TeacherProfile
from .tasks import send_confirmation_mail_task

class SignupForm(forms.ModelForm):
	username = forms.CharField(
	    label="", widget=forms.TextInput(attrs={"placeholder": "Username", 'class': 'form-control form-control-user'})
	)
	password1 = forms.CharField(
	    label="", widget=forms.PasswordInput(attrs={"placeholder": "Enter Password", 'class': 'form-control form-control-user'})
	)
	password2 = forms.CharField(
	    label="", widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password", 'class': 'form-control form-control-user'})
	)
	email = forms.EmailField(
	    widget=forms.TextInput(
	        attrs={"class": "form-control form-control-user", "placeholder": "Enter your email"}
	    )
	)

	class Meta:
		model = CustomUser
		fields = ['username', 'email', 'role']

	def save(self, commit=False):
	    user = super().save(commit=commit)
	    user.is_active = False
	    user.set_password(self.cleaned_data['password1'])        
	    user.save()
	    return user

	def send_email(self):
	    send_confirmation_mail_task.delay(
	        self.cleaned_data['username'], self.cleaned_data['email']
	    )

class StudentProfileForm(forms.ModelForm):
	class Meta:
		model = StudentProfile
		exclude = ['user']

class TeacherProfileForm(forms.ModelForm):
	class Meta:
		model = TeacherProfile
		exclude = ['user']