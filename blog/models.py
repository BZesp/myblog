from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=200, unique=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	content = models.TextField()

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
	name = models.CharField(max_length=120)
	email = models.EmailField()
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
 		return 'Comment {} by {}'.format(self.body, self.name)