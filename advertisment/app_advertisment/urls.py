from django.urls import path
from .views import index_1

urlpatterns = [
    path('', index_1)
]

