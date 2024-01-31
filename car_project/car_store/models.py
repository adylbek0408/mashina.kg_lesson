from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.title


class Marka(models.Model):
    title = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.title


class Car(models.Model):
    name = models.CharField(max_length=16)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    marka = models.ForeignKey(to=Marka, on_delete=models.CASCADE)
    year = models.PositiveIntegerField(default=1980)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_used = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class CarPhoto(models.Model):
    cars_photo = models.ForeignKey(to=Car, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')


class Comment(models.Model):
    author = models.CharField(max_length=16)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    cars_text = models.ForeignKey(to=Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} - {self.cars_text}"
