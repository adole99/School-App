from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.core import exceptions
from libs.utils.constants import UserType


class CustomUser(AbstractUser):
	USER_ROLES = (
        (UserType.student, "student"),
        (UserType.teacher, "teacher"),
    )
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	email = models.EmailField(unique=True)
	role = models.CharField(choices=USER_ROLES, max_length=12, null=True)
	profile_created = models.BooleanField(default=False)

	
	def __str__(self) -> str:
	    return f"{self.username}"

	@property
	def get_full_name(self):
	    if self.first_name and self.last_name:
	        return f'{self.first_name} {self.last_name}'
	    else:
	        return self.username

class Roles(models.Model):
	USER_ROLES = (
	    (UserType.student, "student"),
	    (UserType.teacher, "teacher"),
	)
	role = models.CharField(choices=USER_ROLES, max_length=12)
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_roles")
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
	    verbose_name = "User Role"
	    verbose_name_plural = "User Roles"

	def __str__(self) -> str:
	    return f"User: {self.user} -> Role: {self.role}"

	def save(self, *args, **kwargs):
	    role = Roles.objects.filter(user=self.user, role=self.role)
	    if role.exists():
	        raise exceptions.ValidationError(f"User already assigned {self.role}")
	    return super().save(*args, **kwargs)

class StudentProfile(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
	first_name = models.CharField(max_length=25, null=True)
	last_name = models.CharField(max_length=25, null=True)
	# student_class = models.ForeignKey(StudentClass, on_delete=models.DO_NOTHING, related_name="student_class", null=True)
	home_address = models.CharField(max_length=100, null=False)
	# hobbies = models.CharField(max_length=50)
	# guardian_name = models.CharField(max_length=50)
	# guardian_phone_number = models.IntegerField()
	profile_image = models.ImageField(verbose_name="User Profile Image", upload_to="student_profile_image", blank=True, null=True)

	def __str__(self) -> str:
		return f"{self.user.get_full_name} Student Profile"


class TeacherProfile(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
	first_name = models.CharField(max_length=25, null=True)
	last_name = models.CharField(max_length=25, null=True)
	home_address = models.CharField(max_length=100, null=True)
	profile_image = models.ImageField(verbose_name="User Profile Image", upload_to="teacher_profile_image", blank=True, null=True)

	

	def __str__(self) -> str:
	    return f"{self.user.get_full_name} Teacher Profile"



		