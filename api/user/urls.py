from django.urls import path
from api.user.sign.view import SignAPI

urlpatterns = [
    path('sign', SignAPI.as_view())
]
