from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Kategoriyalar'


class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    rating = models.PositiveIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero)
    discount = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, default=None)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

