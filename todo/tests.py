from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from .models import TodoList, TodoItem


class AnonymousTodoItemTests(APITestCase):
	url = '/api/v1/todo'

	@classmethod
	def setUpTestData(cls):
		item = TodoItem(title='Test Item', description='Test', status='1')
		item.save()

	def test_anonymous_list_items(self):
		"""
		Try to get a list of todo items as the anonymous user.
		"""
		response = self.client.get(self.url, None, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_anonymous_create_item(self):
		data = {
			'title': 'Some title',
			'description': 'Some description',
			'status': 1,
		}

		response = self.client.post(self.url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_anonymous_get_item(self):
		item = TodoItem.objects.first()
		response = self.client.get("%s/%s" % (self.url, item.pk), None, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_anonymous_delete_item(self):
		item = TodoItem.objects.first()
		response = self.client.delete("%s/%s" % (self.url, item.pk), None, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_anonymous_update_item(self):
		item = TodoItem.objects.first()
		data = {
			'title': 'new title',
		}
		response = self.client.put("%s/%s" % (self.url, item.pk), data, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# class UserTodoItemTests(APITestCase):
# 	url = '/api/v1/todo'
#
# 	@classmethod
# 	def setUpTestData(cls):
# 		User = get_user_model()
# 		user_one = User(username='user1', password='test')
# 		user_one.save()
# 		user_two = User(username='user2', password='test')
# 		user_two.save()
#
#
#
# 		# create three lists, two for one user, one for the other
# 		list_one = TodoList(title='List One', description='test', owner=user_one)
# 		list_one.save()
# 		list_two = TodoList(title='List Two', description='test', owner=user_one)
# 		list_two.save()
#
# 		list_three = TodoList(title='List Three', description='test', owner=user_two)
# 		list_three.save()
#
# 		# create three items, one for each list
# 		item = TodoItem(title='Test Item', description='Test', status=1, list=list_one)
# 		item.save()
# 		item2 = TodoItem.objects.create(title='Test Item 2', description='test', status=2, list=list_two)
# 		item2 = TodoItem.objects.create(title='Test Item 2', description='test', status=2, list=list_three)
#
# 	def setUp(self):
# 		self.user_one = get_user_model().objects.get(pk=1)
# 		self.user_two = get_user_model().objects.get(pk=2)
# 		self.client.authenticate('asdf')
#
# 	def test_user_list_items(self):
# 		"""
# 		Try to get a list of todo items as the anonymous user.
# 		"""
# 		self.client.login('user1', 'test')
# 		response = self.client.get(self.url, None, format='json')
# 		self.assertEqual(response.status_code, status.HTTP_200_OK)
