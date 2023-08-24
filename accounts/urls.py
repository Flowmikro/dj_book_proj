from django.urls import path

from .views import SingUpPageView

urlpatterns = [
    path('signup/', SingUpPageView.as_view(), name='signup'),
]