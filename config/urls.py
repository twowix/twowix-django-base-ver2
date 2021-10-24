from django.urls import path, include

urlpatterns = [
    path('api/v1/user', include('api.user.urls'))
]
