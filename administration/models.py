from django.db import models

# Create your models here.
class Subject(models.Model):
	subject = models.CharField(max_length=30)

	def __str__(self) -> str:
		return f"{self.subject}"

class StudentClass(models.Model):
	class_name = models.CharField(max_length=4)

	def __str__(self) -> str:
		return f"{self.class_name}"
