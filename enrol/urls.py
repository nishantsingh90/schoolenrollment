from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


app_name = 'product'


urlpatterns = [
    path('', views.index,name="index"),
    path('city/', views.CityAPIView.as_view()),
    path('grade/', views.GradeAPIView.as_view()),
    path('pin/', views.PinAPIView.as_view()),
    path('findpincode/', views.findpincode,name="findpincode"),
    path('validatemobile/', views.validatemobile,name="validatemobile"),
    path('studentform/', views.studentform,name="studentform"),
    path('studentform1/', views.studentform1,name="studentform1"),
    path('showstudent/', views.showstudent,name="showstudent"),
    path('editstudent/', views.editstudent,name="editstudent"),
    ]