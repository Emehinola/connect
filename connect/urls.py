"""connect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from index import views
from courses import views as courses_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aggregate/', views.aggregate, name="aggregate-template"),
    path('course-selector/', courses_views.course_selector, name='course-selector'),
    path('course-selector/get-course/',
         courses_views.get_course, name='get-course'),
    path('', include('index.urls'), name='home'),
]

admin.site.site_header = "247Connect"
admin.site.site_title = "247Connect"
admin.site.index_title = "247Connect"
