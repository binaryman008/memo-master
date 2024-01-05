from django.urls import include, path
from users.api_views import RegisterApi, LoginView

urlpatterns = [
    path('signup', RegisterApi.as_view(), name="signup"),
    path('login', LoginView.as_view(), name="login"),
]