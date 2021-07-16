from django.urls import path
from django.views.generic.base import TemplateView
from useradm.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings


urlpatterns = [

    path('test_index/', TemplateView.as_view(template_name='index.html'), name='test_index'),

    # path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),

    path('logout/', LogoutView.as_view(next_page=settings.LOGIN_REDIRECT_URL), name='logout'),

    path('register/', register, name='register'),

]
