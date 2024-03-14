from django.db import models
from django.conf import settings

# User Profile for additional user information
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)



# Store model
class Store(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stores')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # Other fields as necessary

# Category model for product categorization
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

# Product model
class Product(models.Model):
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Other fields as necessary

# Order and OrderItem models for handling purchases
class Order(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    # Other fields as necessary

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

# Chat model for communication
class ChatSession(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chatsessions')

class Message(models.Model):
    chat_session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Subscription model for premium features
class Subscription(models.Model):
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subscriptions', on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)

# Review and Rating models for feedback
class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    rater = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ratings', on_delete=models.CASCADE)
    score = models.IntegerField()
