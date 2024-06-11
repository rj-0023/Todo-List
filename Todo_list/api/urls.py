# from django.urls import path

# from . import views

# urlpatterns = [
#     path('data/', views.dataview, name="Data"),
# ]


from django.urls import path
from . import views

urlpatterns = [
    # path('tasks/', views.TaskListCreateAPIView.as_view(), name='task-list'),
    # path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
    path('data', views.dataview),
    path('register', views.RegisterAPI.as_view()),
    path('login', views.LoginAPI.as_view()),
    # path('tasks', views.TaskAPIView.as_view(), name='task-api'),
]
