from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
	path('', views.index, name="index"),
	path('login/', views.login_view, name="login"),
	path('register/', views.register, name="register"),
	path('activate/<uidb64>/<token>/', views.activate_account_view, name='activate'),
	path('dashboard/', views.dashboard, name="dashboard"),
	path('student/', views.student_home, name="student-home"),
	path('teacher/', views.teacher_home, name="teacher-home"),
]