from django.db import models

# Create your models here.

class jobPosting(models.Model):
    # this section contains the feild on the table
    tittle = models.CharField(max_length=100)
    # textFeild are used for longer strings
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    # To check if there's no posting 
    is_active = models.BooleanField(default=False)

# note
    def __str__(self) -> str:
        return f"{self.tittle} | {self.company}| Active: {self.is_active}"
