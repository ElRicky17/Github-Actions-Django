from django.urls import path
from .views import get_member


urlpatterns = [
    path('members/', get_member, name='get_member')
]