from django.db import models

class Base(models.Model): 
  created = models.DateTimeField (auto_now_add= True) 
  updated = models.DateTimeField(auto_now= True)
  deleted = models.DateTimeField(null=True, blank=True)

  class Meta:
    abstract = True

class User(Base):
    cpf = models.CharField(max_length=13)
    name = models.CharField(max_length=100, blank = True)
    age = models.CharField(max_length=3, null=True)
    phone = models.CharField(max_length=25, null=True)
    email = models.CharField(max_length=100, null=True)