import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)# equvalente a un Varchar en la BD 
    pub_date =  models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now - datetime.timedelta(days=5)
        
    
class Choice(models.Model): 
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # la llave foranea y on.delete es para en el momento en que se borre la preguntas se borren en casaca da todas las opciones de esa pregunta 
    choice_text =  models.CharField(max_length=200)
    votes  =  models.IntegerField(default=0)# capo de numero entereros
    
    def __str__(self):
        return self.choice_text
