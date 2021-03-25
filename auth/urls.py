from django.urls import path
from auth.views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('login/', obtain_auth_token, name='token_obtain'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    
]


