from django.db import models
from django.urls import reverse
# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=100)
    rating=models.FloatField()
    user_rated=models.CharField(max_length=70)
    price=models.CharField(max_length=70)
    image=models.CharField(max_length=70)


    def __str__(self) :
        return self.name

    # def get_absolute_url(self):
    #     return reverse('top_product:detail_item',args=[self.id,])