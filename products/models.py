from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):

	app_title = models.CharField(default='抖音：记录美好生活', max_length=50)
	app_intro = models.TextField(default='这是APP介绍')
	app_url = models.CharField(default='Http://', max_length=100)
	app_icon = models.ImageField(default='default_icon.png', upload_to='images/')
	app_image = models.ImageField(default='defult_image.png', upload_to='images/')

	votes = models.IntegerField(default=1)
	pub_date = models.DateField()
	# 添加外键  CASCADE串联
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.app_title
    