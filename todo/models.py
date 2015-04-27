from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings


class TodoList(models.Model):
	"""
	Lists hold todo items and give a bit of organization, allowing users to group their todo items.
	"""
	title = models.CharField(_('Title'), max_length=255)
	description = models.TextField(_('Description'))
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='lists')

	def __unicode__(self):
		return self.title


class TodoItem(models.Model):
	"""
	Holds the data for a todo item
	"""
	NORMAL = 0
	COMPLETED = 1
	OVERDUE = 2

	status_choices = (
		(NORMAL, _('Normal')),
		(COMPLETED, _('Completed')),
		(OVERDUE, _('Overdue'))
	)

	title = models.CharField(_('Title'), max_length=255)
	description = models.TextField(_('Description'))
	status = models.IntegerField(_('Status'), choices=status_choices)
	list = models.ForeignKey(TodoList, related_name='tasks', null=True)
	created = models.DateTimeField(_('Created Date'), auto_now_add=True, null=True)
	updated = models.DateTimeField(_('Updated Date'), auto_now=True, null=True)
	due = models.DateTimeField(_('Due Date'), blank=True, null=True, default=None)

	def __unicode__(self):
		return self.title