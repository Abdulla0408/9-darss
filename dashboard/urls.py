from django.urls import path
from .views import (index, contact_list, update_status, service_list, service_create, service_update, service_delete,
                   portfolio_create, portfolio_update, portfolio_list, portfolio_delete,
                   blog_post_list, blog_post_create, blog_post_update, blog_post_delete,
                   testimonial_list, testimonial_create, testimonial_update, testimonial_delete,
                   contact_list, contact_create, contact_update, contact_delete, user_login, user_logout)





urlpatterns = [
    path('', index, name='dashboard_index'),
    path('contact_list/', contact_list, name="contact_list"),
    path('contact/update/<int:id>/', update_status, name="update_status"),
    path('contact/create/', contact_create, name="contact_create"),
    path('contact/update/<int:id>/', contact_update, name="contact_update"),
    path('contact/delete/<int:id>/', contact_delete, name="contact_delete"),

    # =========================================================================

    path('service_list/', service_list, name="service_list"),
    path('service/create/', service_create, name="service_create"),
    path('service/update/<int:id>/', service_update, name="service_update"),
    path('service/delete/<int:id>/', service_delete, name="service_delete"),

    # =========================================================================

    path('portfolio_list/', portfolio_list, name="portfolio_list"),
    path('portfolio/create/', portfolio_create, name="portfolio_create"),
    path('portfolio/update/<int:id>/', portfolio_update, name="portfolio_update"),
    path('portfolio/delete/<int:id>/', portfolio_delete, name="portfolio_delete"),

    # =========================================================================

    path('testimonial_list/', testimonial_list, name="testimonial_list"),
    path('testimonial/create/', testimonial_create, name="testimonial_create"),
    path('testimonial/update/<int:id>/', testimonial_update, name="testimonial_update"),
    path('testimonial/delete/<int:id>/', testimonial_delete, name="testimonial_delete"),

    # =========================================================================

    path('blog_list', blog_post_list, name="blog_list"),
    path('blog/create/', blog_post_create, name="blog_create"),
    path('blog/update/<int:id>/', blog_post_update, name="blog_update"),
    path('blog/delete/<int:id>/', blog_post_delete, name="blog_delete"),

    # =========================================================================

    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
]

