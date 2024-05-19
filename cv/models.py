from django.db import models # type: ignore

class CV(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    summary = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    awards = models.TextField()
    portfolio_link = models.URLField()
    cv_file = models.FileField(upload_to='cvs')  # For storing the PDF file

    def __str__(self):
        return self.name




