from django.db import models
# from django.utils import timezone

class Developer(models.Model):
  dev_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  biography = models.TextField()
  image = models.ImageField(upload_to='dev_images/', null=True, blank=True)
  email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=20, blank=True)
  website_url = models.URLField(blank=True)

  def __str__(self):
    return self.name




