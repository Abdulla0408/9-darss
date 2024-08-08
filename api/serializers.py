from rest_framework.serializers import ModelSerializer
from landing.models import Service, Portfolio, Testimonial, BlogPost, Contact


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class TestimonialSerializer(ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


