from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField("Date Published")

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    #question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

"""
Finally, note a relationship is defined, using ForeignKey. That tells Django each Choice is related to a 
single Question. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.

A python database schema is created to access above classes

#Related name works to access in reverse way possible
"""