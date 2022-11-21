from django.urls import path
from .import views

urlpatterns = [
    path('urubuto/', views.urubuto, name="urubuto"),
]
