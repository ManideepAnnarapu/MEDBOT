# chatbot_site/urls.py
from django.contrib import admin
from django.urls import path
from chatbot_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', views.chatbot_view, name='chatbot'),
]
