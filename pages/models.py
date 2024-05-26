
from django.db import models
import datetime
from django.contrib.auth.models import User

def current_datetime():
    return datetime.datetime.now()


class ContactRequest(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  message = models.TextField()
  done_at = models.DateTimeField(default=current_datetime)

  def __str__(self):
    # return self.name
    return f"{self.name} - {self.done_at}"
  
  



