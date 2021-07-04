from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'get-course/', views.get_course, name='get-course')
]
