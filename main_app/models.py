from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Clothes(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
      return self.name
    
    def get_absolute_url(self):
      return reverse('clothes_detail', kwargs={'pk': self.id})

class Penguin(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  clothes = models.ManyToManyField(Clothes)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'penguin_id': self.id})

  def swam_today(self):
    return self.swimming_set.filter(date=date.today()).count() >= len(TIMES)

  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Swimming(models.Model):
  date = models.DateField('swimming date')
  time = models.CharField(
      max_length=1,
      choices=TIMES,
      default=TIMES[0][0]
  )

  penguin = models.ForeignKey(Penguin, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_time_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  penguin = models.ForeignKey(Penguin, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for penguin_id: {self.penguin_id} @{self.url}"