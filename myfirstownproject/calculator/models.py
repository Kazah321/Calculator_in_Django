from django.db import models

# Create your models here.
class CalculatorModel(models.Model):
	def calc_add(self,a,b):
		 return a+b
	def calc_sub(self,a,b):
		return a-b
	def calc_sq(self,a):
		return a*a
	def calc_div(self,a,b):
		return a/b
	def calc_mul(self,a,b):
		return a*b