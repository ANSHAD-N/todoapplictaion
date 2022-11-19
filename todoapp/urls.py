from django.urls import path, include

from . import views
app_name = 'todoapp'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('details/', views.details, name='details'),
    # path('delete/<int:id>', views.delete, name='delete'),
    # path('update/<int:id>', views.update, name='update'),

    path('', views.TaskListView.as_view(), name='cbvindex'),
    path('details/<int:pk>/', views.TaskDetailView.as_view(), name='details'),
    path('cbvdelete/<int:pk>', views.TaskDeleteView.as_view(), name='delete'),
    path('cbvupdate/<int:pk>', views.TaskUpdateView.as_view(), name='update'),
 ]
