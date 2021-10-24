from django.urls import path
from api.user.views import SignAPI

urlpatterns = [
    path('sign', SignAPI.as_view())
]
