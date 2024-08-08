from django.shortcuts import render, redirect
from landing.models import Service, Portfolio, Testimonial, BlogPost, Contact
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse



def is_admin(user):
    return user.is_authenticated and user.is_staff


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if is_admin(request.user):
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "Bu sahifaga kirish uchun admin huquqlari kerak.")
            return redirect(reverse('login'))
    return wrapper


@admin_required
def index(request):
    return render(request, 'dashboard/base.html')

@admin_required
def contact_list(request):
    contacts = Contact.objects.all().order_by('harakatlar')
    return render(request, 'dashboard/contact/list.html', {'contacts': contacts})


@admin_required
def update_status(request, id):
    contact = Contact.objects.get(id=id)
    contact.harakatlar = True
    contact.save()
    return redirect('contact_list')



# =====================================================================================

# CRUD for service models

@admin_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'dashboard/service/list.html', {'services': services})

@admin_required
def service_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        icon = request.FILES.get('icon')
        if title and description and icon:
            Service.objects.create(title=title, description=description, img=icon)
            messages.success(request, "Xizmat muvaffaqiyatli yaratildi.")
            return redirect('service_list')
        else:
            messages.error(request, "Barcha maydonlarni to'ldiring.")
    return render(request, 'dashboard/service/create.html')

@admin_required
def service_update(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        service.title = request.POST.get('title')
        service.description = request.POST.get('description')
        if 'icon' in request.FILES:
            service.img = request.FILES['icon']
        service.save()
        messages.success(request, "Xizmat muvaffaqiyatli yangilandi.")
        return redirect('service_list')
    return render(request, 'dashboard/service/update.html', {'service': service})

@admin_required
def service_delete(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'dashboard/service/delete.html', {'service': service})


# =====================================================================================

# CRUD for Porfolio models

def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'dashboard/portfolio/list.html', {'portfolios': portfolios})


@admin_required
def portfolio_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        project_date = request.POST.get('project_date')
        Portfolio.objects.create(
            title=title,
            description=description,    
            image=image,
            category=category,
            project_date=project_date
        )
        return redirect('portfolio_list')
    return render(request, 'dashboard/portfolio/create.html')


@admin_required
def portfolio_update(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    if request.method == 'POST':
        portfolio.title = request.POST.get('title')
        portfolio.description = request.POST.get('description')
        if 'image' in request.FILES:
            portfolio.image = request.FILES['image']
        portfolio.category = request.POST.get('category')
        portfolio.project_date = request.POST.get('project_date')
        portfolio.save()
        return redirect('portfolio_list')
    return render(request, 'dashboard/portfolio/update.html', {'portfolio': portfolio})


@admin_required
def portfolio_delete(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    if request.method == 'POST':
        portfolio.delete()
        return redirect('portfolio_list')
    return render(request, 'dashboard/portfolio/delete.html', {'portfolio': portfolio})

# =====================================================================================

# CRUD for Testimonial models


def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'dashboard/testimonial/list.html', {'testimonials': testimonials})


@admin_required
def testimonial_create(request):
    if request.method == 'POST':
        data = request.POST
        if not all([data.get('name'), data.get('position'), data.get('content')]):
            messages.error(request, "Barcha majburiy maydonlarni to'ldiring.")
            return render(request, 'dashboard/testimonial/create.html')
        
        try:
            Testimonial.objects.create(
                name=data.get('name'),
                position=data.get('position'),
                company=data.get('company', ''),
                content=data.get('content'),
                image=request.FILES.get('image')
            )
            messages.success(request, "Guvohnoma muvaffaqiyatli yaratildi.")
            return redirect('testimonial_list')
        except IntegrityError as e:
            messages.error(request, f"Xatolik yuz berdi: {str(e)}")
    
    return render(request, 'dashboard/testimonial/create.html')


@admin_required
def testimonial_update(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    if request.method == 'POST':
        testimonial.name = request.POST.get('name')
        testimonial.position = request.POST.get('position')
        testimonial.company = request.POST.get('company')
        testimonial.content = request.POST.get('content')
        if 'image' in request.FILES:
            testimonial.image = request.FILES['image']
        testimonial.save()
        return redirect('testimonial_list')
    return render(request, 'dashboard/testimonial/update.html', {'testimonial': testimonial})


@admin_required
def testimonial_delete(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    if request.method == 'POST':
        testimonial.delete()
        return redirect('testimonial_list')
    return render(request, 'dashboard/testimonial/delete.html', {'testimonial': testimonial})

# =====================================================================================

# CRUD for BlogPost models


def blog_post_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'dashboard/blog_post/list.html', {'blog_posts': blog_posts})


@admin_required
def blog_post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        BlogPost.objects.create(
            title=title,
            content=content,
            author=author,
            image=image,
            category=category
        )
        return redirect('blog_list')
    return render(request, 'dashboard/blog_post/create.html')


@admin_required
def blog_post_update(request, id):
    blog_post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        blog_post.title = request.POST.get('title')
        blog_post.content = request.POST.get('content')
        blog_post.author = request.POST.get('author')
        blog_post.category = request.POST.get('category')
        if 'image' in request.FILES:
            blog_post.image = request.FILES['image']
        blog_post.save()
        return redirect('blog_post_list')
    return render(request, 'dashboard/blog_post/update.html', {'blog_post': blog_post})


@admin_required
def blog_post_delete(request, id):
    blog_post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        blog_post.delete()
        return redirect('blog_list')
    return render(request, 'dashboard/blog_post/delete.html', {'blog_post': blog_post})

# =====================================================================================

# CRUD for Team models


def contact_create(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        harakatlar = request.POST.get('harakatlar') == 'on'
        Contact.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            harakatlar=harakatlar
        )
        return redirect('landing:index')
    return render(request, 'dashboard/contact/create.html')


@admin_required
def contact_update(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.full_name = request.POST.get('full_name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.harakatlar = request.POST.get('harakatlar') == 'on'
        contact.save()
        return redirect('contact_list')
    return render(request, 'dashboard/contact/update.html', {'contact': contact})


@admin_required
def contact_delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'dashboard/contact/delete.html', {'contact': contact})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard_index')
        else:
            return render(request, 'dashboard/login_user.html', {'error': 'Username yoki parol xato'})
    return render(request, 'dashboard/login_user.html')


def user_logout(request):
    logout(request)
    return redirect('landing:index')
