from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ServiceSerializer, PortfolioSerializer, TestimonialSerializer, BlogPostSerializer,ContactSerializer
from landing.models import Service, Portfolio, Testimonial, BlogPost, Contact


# Write API for service_list and service_detail functions
@api_view(['GET'])
def service_list(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def service_detail(request, id):
    try:
        service = Service.objects.get(id=id)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)
    except Service.DoesNotExist:
        return Response({"error": "Service not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


# Write API for portfolio_list and portfolio_detail functions
@api_view(['GET'])
def portfolio_list(request):
    portfolio = Portfolio.objects.all()
    serializer_data = PortfolioSerializer(portfolio, many=True)
    return Response(serializer_data.data)


@api_view(['GET'])
def portfolio_detail(request, id):
    portfolio = Portfolio.objects.get(id=id)
    serializer_data = PortfolioSerializer(portfolio).data
    return Response(serializer_data)


# Write API for testimonial_list and testimonial_detail functions
@api_view(['GET'])
def testimonial_list(request):
    testimonial = Testimonial.objects.all()
    serializer_data = TestimonialSerializer(testimonial, many=True)
    return Response(serializer_data.data)


@api_view(['GET'])
def testimonial_detail(request, id):
    testimonial = Testimonial.objects.get(id=id)
    serializer_data = TestimonialSerializer(testimonial).data
    return Response(serializer_data)


# Write API for blog_post_list and blog_post_detail functions
@api_view(['GET'])
def blog_post_list(request):
    blog_post = BlogPost.objects.all()
    serializer_data = BlogPostSerializer(blog_post, many=True)
    return Response(serializer_data.data)


@api_view(['GET'])
def blog_post_detail(request, id):
    blog_post = BlogPost.objects.get(id=id)
    serializer_data = BlogPostSerializer(blog_post).data
    return Response(serializer_data)


@api_view(['GET'])
# Write API for contact_list and contact_detail functions
def contact_list(request):
    contact = Contact.objects.all()
    serializer_data = ContactSerializer(contact, many=True)
    return Response(serializer_data.data)


@api_view(['GET'])
def contact_detail(request, id):
    contact = Contact.objects.all(id=id)
    serializer_data = ContactSerializer(contact).data
    return Response(serializer_data)
