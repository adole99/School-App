from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
	path('', views.index, name="index"),
	path('login/', views.login_view, name="login"),
	path('register/', views.register, name="register"),
	path('activate/<uidb64>/<token>/', views.activate_account_view, name='activate'),
	# path('dashboard/', views.dashboard, name="dashboard"),
#student URLs
	path('student/', views.student_home, name="student-home"),
	path('student-profile/', views.student_profile, name="student-profile"),

#teacher URLs
	path('teacher/', views.teacher_home, name="teacher-home"),
	path('teacher-profile/', views.teacher_profile, name="teacher-profile"),
]