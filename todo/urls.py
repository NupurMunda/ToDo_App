
from django.urls import path
from .views import *

app_name= "todo"
urlpatterns = [

    path('', view_home,name='homepage'),
    path('add-task/',add_task,name='add_task'),
    path('view-task/',view_task,name='view_task'),
    path('view-completed-task/',view_completed_task,name='view_completed_task'),
    path('task-completed/<int:id>',task_completed,name='task_completed'),
    path('task-delete/<int:id>',del_task,name='del_task'),
  
]
