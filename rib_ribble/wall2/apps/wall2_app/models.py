from __future__ import unicode_literals

from django.db import models

class User( models.Model):
	first_name = models.CharField(max_length=255)
	last_name =models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_=True)

class Post( models.Model):
	message = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_=True)
	user_id = models.ForeignKey('User')


class Comment( models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_=True)
	user_id = models.ForeignKey('User')
	post_id = models.ForeignKey('Post')
	"""docstring for comment"models.Modelf __init__(self, arg):
		super(comment,models.Model.__init__()
		self.arg = arg
		
