from django.utils.translation import ugettext as _

from rest_framework import serializers

from .models import TodoList, TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = TodoItem

	def validate_list(self, value):
		if self.context['request'].user != value.owner:
			raise serializers.ValidationError(_('You can only add items to a list that you own.'))
		else:
			return value


class TodoListSerializer(serializers.ModelSerializer):
	class Meta:
		model = TodoList