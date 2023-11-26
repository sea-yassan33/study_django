from django.db import models

class Customer(models.Model):
	GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
	name = models.CharField(max_length=100)
	mail = models.EmailField(max_length=100)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	sns_acount = models.CharField(max_length=50)

	# テキスト表示
	def __str__(self):
		return self.name