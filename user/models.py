from django.db import models

# Create your models here.

# __str__ function identation problem

class user(models.Model):
	user_name = models.CharField(max_length = 3000)
	user_taskList = models.CharField(max_length = 3000)
	user_adviceList = models.CharField(max_length = 3000)
	task_achieved= models.ForeignKey('Task',on_delete=models.CASCADE)
	def __str__(self):
    	 return self.user_name    
    

class Task(models.Model):
	task_category = models.CharField(max_length = 1000)
	task_text = models.TextField(default=" task ")
	ACHIEVED = 'AC'
	NOT_ACHIEVED = "NC"
	TASK_ACHIEVED = [
		(ACHIEVED,'Task Achieved'),
		(NOT_ACHIEVED,'Task Not Achieved')
	]
	task_achieved = models.CharField(max_length = 2,
	 choices = TASK_ACHIEVED,default = NOT_ACHIEVED)
	task_count = models.IntegerField(default=0)
	def __str__(self):
    	 return self.task_text

class Advices(models.Model):
	class AdviceCategory(models.TextChoices):
		HEALTH ='H', ('Health')
		FINANCE ='F', ('Finance')
		HOUSEHOLD = 'C', ('Household')
	advice_category = models.CharField(max_length = 2 ,choices = AdviceCategory.choices)
	advice_text = models.TextField()
	def __str__(self):
    	 return self.advice_text
