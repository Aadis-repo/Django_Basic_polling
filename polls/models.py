
import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Question(models.Model):
    question_txt = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date_Published')

    def __str__(self):
        return self.question_txt
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_txt = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)    

    def __str__(self):
        return self.choice_txt
