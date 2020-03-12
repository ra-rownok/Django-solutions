
from django.contrib import admin
from django.urls import path
from route import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum/<int:num1>/<int:num2>/', views.sum),
    path('sub/<int:num1>/<int:num2>/', views.sub)
]
