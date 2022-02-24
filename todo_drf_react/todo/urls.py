from django.urls import path 
from rest_framework import routers 

from todo.views import ToDoViewSet 

router = routers.DefaultRouter()
router.register('todo', ToDoViewSet)
