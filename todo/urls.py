from django.urls import path
from . import views

urlpatterns = [
    path('add-task/', views.add_task, name='addTask'),
    path('mark-as-done/<int:pk>/', views.mark_as_done, name='markAsDone'),
]
