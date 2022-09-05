import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)# equvalente a un Varchar en la BD 
    pub_date =  models.DateTimeField("date published")
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
        
    #     if self.choice_set.all().count() == 0:
    #         super().delete()
    #         raise Exception("Question must have at least one choice")
    
    def __str__(self):
        return self.question_text
    
    
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        

class Choice(models.Model): 
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # la llave foranea y on.delete es para en el momento en que se borre la preguntas se borren en casaca da todas las opciones de esa pregunta 
    choice_text =  models.CharField(max_length=200)
    votes  =  models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
