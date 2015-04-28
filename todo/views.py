from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import TodoItem, TodoList
from .serializers import TodoItemSerializer, TodoListSerializer

from rest_framework import permissions


class TodoItemViewSet(ModelViewSet):
	serializer_class = TodoItemSerializer
	paginate_by = 25
	paginate_by_param = 'page'
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		"""
		DRF authorization doesn't apply to listing methods, make sure that only
		items the user has access to are included in the queryset.
		:return:A queryset of list items that belong to this user.
		"""
		if self.request.user.is_anonymous():
			return TodoItem.objects.none()
		return TodoItem.objects.filter(list__owner=self.request.user)


class TodoListViewSet(ModelViewSet):
	serializer_class = TodoListSerializer
	paginate_by = 25
	paginate_by_param = 'page'

	def get_queryset(self):
		return None