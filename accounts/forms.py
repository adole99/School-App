from django import forms
from accounts.models import CustomUser

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
