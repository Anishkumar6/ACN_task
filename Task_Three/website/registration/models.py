from django.db import models


# # Create your models here.
#
class Registration(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    m_no = models.IntegerField(max_length=10)
