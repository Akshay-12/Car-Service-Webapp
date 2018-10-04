from django.db import models

class Company(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Cars(models.Model):
	name = models.CharField(max_length=20)
	company=models.ForeignKey(Company,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Garage(models.Model):
	name = models.CharField(max_length=20)
	address=models.CharField(max_length=50)
	phone=models.IntegerField(max_length=10)
	

	def __str__(self):
		return self.name

class Parts(models.Model):
	name = models.CharField(max_length=20)
	price=models.IntegerField(max_length=7)
	model=models.ForeignKey(Cars,on_delete=models.CASCADE)
	garage_name=models.ForeignKey(Garage,on_delete=models.CASCADE)

	def __str__(self):
		return self.name