from django.db import models
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from manager.models import User


class MainCategory(models.Model):
    CHOICES = [
        ('M', 'for man'),
        ('F', 'feminine'),
        ('C', 'childish'),
    ]
    main_category = models.CharField(max_length=1, choices=CHOICES)
    
    def __str__(self):
        return self.main_category


class SubCategory(models.Model):
    main = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.sub_category


class Brand(models.Model):
    brand = models.CharField(max_length=50)
    
    def __str__(self):
        return self.brand


class Shoes(models.Model):
    name = models.CharField(max_length=225)
    price = models.CharField(max_length=9)
    obj_id = models.PositiveIntegerField()
    adder = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    m_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    s_category = models.ManyToManyField(SubCategory)
    attribute = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    from_word = GenericForeignKey('attribute', 'obj_id')
    
    def __str__(self):
        return self.name


class Attributes(models.Model):
    title = models.CharField(max_length=20)
    value = models.CharField(max_length=20)
    shoes = GenericRelation(Shoes, related_query_name='shoes')
    
    def __str__(self):
        return f'{self.titel} : {self.value}'

    
    def save(self, *args, **kwargs):
        if not self.obj_id:
            self.obj_id = slugify(self.id)
        return super(Blog, self).save(*args, **kwargs)


class Size(models.Model):
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    size = models.CharField(max_length=2)
    
    def __str__(self):
        return f'{self.shoes} has size {self.size}'


class Color(models.Model):
    color = models.CharField(max_length=10)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    number = models.CharField(max_length=5)
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)


class Gallery(models.Model):
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    photo = models.ImageField()
    
    def __str__(self):
        return f'{self.shoes.name}'


