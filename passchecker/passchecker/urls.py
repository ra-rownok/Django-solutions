from django.contrib import admin
from django.urls import path
from password import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index',views.index),
    path('pwd', views.pwd, name='pwd')
]
