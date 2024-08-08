from django.urls import path
from .views import (service_list, service_detail, portfolio_list, portfolio_detail, testimonial_list, testimonial_detail,
                    blog_post_list, blog_post_detail, contact_list, contact_detail)

app_name = 'api'
urlpatterns = [
    path('service_list/', service_list),
    path('service_detail/<int:id>/', service_detail),

    path('portfolio_list/', portfolio_list),
    path('portfolio_detail/<int:id>/', portfolio_detail),

    path('testimonial_list/', testimonial_list),
    path('testimonial_detail/<int:id>/', testimonial_detail),

    path('blog_post_list/', blog_post_list),
    path('blog_post_detail/<int:id>/', blog_post_detail),

    path('contact_list/', contact_list),
    path('contact_detail/<int:id>/', contact_detail),

]