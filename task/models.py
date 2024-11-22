from django.db import models
from accounts.models import User

# Create your models here.
class Task(models.Model):
	title = models.CharField(max_length=50)
	status = models.BooleanField(default=False, verbose_name='completed')
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-created_at']