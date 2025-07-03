from django.urls import path
from .views import Signupview, custom_login

urlpatterns=[
    path('custom-login/', custom_login, name='custom_login'),
    path('signup/', Signupview.as_view(),name='signup'),
]