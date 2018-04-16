from .views import UserListAPIView
from django.conf.urls import url

urlpatterns =[
    url(r'^$', UserListAPIView.as_view(), name='lista'),
]