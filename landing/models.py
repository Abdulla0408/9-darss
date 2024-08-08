from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to="service/")

    def __str__(self):
        return self.title   


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    category = models.CharField(max_length=50)
    project_date = models.DateField()
    client = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return f"{self.name} - {self.company}"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/')
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    harakatlar = models.BooleanField()

    def __str__(self):
        return self.full_name