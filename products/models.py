from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    image = models.URLField(max_length=500)
    
    # RELATIONSHIP 1: Many products can belong to one Category
    # Protect models by setting them to SET_NULL if a category is deleted
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    
    # RELATIONSHIP 2: Many-to-Many relation with Tags
    tags = models.ManyToManyField(Tag, blank=True, related_name='products')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    # RELATIONSHIP 3: Many reviews belong to one Product
    # related_name='reviews' allows reversed lookup: product.reviews.all()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user_name} on {self.product.name}"