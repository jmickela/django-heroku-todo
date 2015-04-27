from rest_framework.routers import DefaultRouter

from todo.views import TodoItemViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'todo', TodoItemViewSet, base_name='todo-item')