from django.db import models
# from django.utils import timezone

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price= models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    # pub_date = models.DateField(default=timezone.now().date)
    image = models.ImageField(upload_to='shop/images', default=None, blank=True, null=True)
    
    def __str__(self):
       return "{}:${}".format(self.product_name, self.price)