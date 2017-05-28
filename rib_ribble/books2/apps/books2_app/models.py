from __future__ import unicode_literals

from django.db import models
from datetime import datetime 

class Book(models. Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	published_date = models.DateField(auto_now_add=True)
	category = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	in_print = models.BooleanField()

	book4 = Book.objects.create(title="A Phantom Menace", author="George Lucas", published_date="1980",category="Sci Fi")
	
