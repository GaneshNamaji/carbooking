from django.db import models


CATEGORY_CHOICES=(
    ('MZ','maruti suzuki'),
    ('HY','hyunda'),
    ('AD','audi'),
    ('JR','jaguar'),
    ('JP','jeep'),
    ('BM','bmw'),
    ('MS','mercedes'),
    ('SK','skoda'),
    ('VO','volvo'),
    ('HO','honda'),
    ('LM','lamborghini'),
    ('PE','porsche'),
)
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phoneNumber=models.CharField(max_length=12)
    description=models.TextField()
    def __str__(self) :
        return f'Message from {self.name}'

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_prize=models.FloatField()
    discription=models.TextField()
    composition=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_images=models.ImageField(upload_to='product')
    def __str__(self):
        return self.title


        gnesh



    
    
