from django.urls import path

from . import views
app_name = 'todoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:task_id>/', views.detail, name='detail'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('update/<int:task_id>/', views.update, name='update'),
]
