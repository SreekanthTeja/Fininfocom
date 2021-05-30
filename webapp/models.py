from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
GENDER = (('M','MALE'),('F','FEMALE'))
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete =models.CASCADE)
    phone = models.IntegerField(verbose_name = 'Phone')
    age = models.IntegerField(verbose_name='Age')
    gender = models.CharField(verbose_name='Gender',choices=GENDER, max_length=10)
    address = models.TextField(verbose_name='Adress')
    avatar = models.FileField(verbose_name='Avater',blank=True,null=True)
    def __str__(self):
        return self.user.first_name
class Education(models.Model):
    user = models.ForeignKey(to=User, on_delete =models.CASCADE, null=True)
    course = models.CharField(verbose_name = 'Course', max_length=250)
    college = models.CharField(verbose_name='School/College',max_length=250)
    year = models.IntegerField(verbose_name='Year')
    percentage = models.FloatField(verbose_name='Percentage')
    def __str__(self):
        return self.college
     

