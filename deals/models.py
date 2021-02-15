from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='media', blank=False, null=False)


class Deals(models.Model):
    customer = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer} - {self.item}'

