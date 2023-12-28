"""Librarypro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Libraryapp.views import *
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [

    path('admin/', admin.site.urls),

    # path("front_page/",front_page,name =front_page),

    path("admin_page/",admin_page,name ="admin_page"),
    path("admin_login_page/",admin_login_page, name ="admin_login_page"),
    path("admin_signup_page/",admin_signup_page, name ="admin_signup_page"),
    path("admin_logout_page/",admin_logout_page,name= "admin_logout_page"),

    path("Student_page/",Student_page,name= "Student_page"),
    path("student_signup_page/",student_signup_page, name="student_signup_page"),
    path("student_login_page/",student_login_page,name ="student_login_page"),
    path("student_logout_page/",student_logout_page,name ="student_logout_page/"),
 
    path("add_BOOK/",add_BOOK,name ="add_BOOK"),
    path("issue_book/",issue_book,name="issue_book"),
    path("Avalable_book/",Avalable_book,name ="Avalable_book"),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

