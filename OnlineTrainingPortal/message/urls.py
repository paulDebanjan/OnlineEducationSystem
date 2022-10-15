from django.urls import path
from message import views


urlpatterns = [
    path('<str:group_name>/',views.index)
]