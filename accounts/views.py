from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm, ContactForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
from .models import Stats, PostNews, Page, Program, Buku, Testimoni
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

def index(request):
    stats = Stats.objects.first()
    news_list = PostNews.objects.all()
    testimoni_list = Testimoni.objects.all()
    

     # Tampilkan 3 posting per halaman
    paginator = Paginator(news_list, 3)
    page = request.GET.get('page')

    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        # Jika 'page' bukan integer, kembalikan halaman pertama
        news_list = paginator.page(1)
    except EmptyPage:
        # Jika 'page' melebihi jumlah halaman yang ada, kembalikan halaman terakhir
        news_list = paginator.page(paginator.num_pages)


    context = {
        'stats': stats,
        'news_list' : news_list,
        'testimoni_list' : testimoni_list
    }
    
    return render(request, 'home/index.html', context)

def daftar_buku(request):
    buku_list = Buku.objects.all()
    return render(request, 'home/penerbit.html', {'buku': buku_list})

def news_detail(request, slug):
    news = get_object_or_404(PostNews, slug=slug)
    context = {
        'news': news
    }
    return render(request, 'home/news_detail.html', context)

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    news = PostNews.objects.filter()

    return render(request, 'home/page_detail.html', {'page': page, 'news': news})


def program_detail(request, slug):
    program = get_object_or_404(Program, slug=slug)
    news = PostNews.objects.filter()
    program_list = Program.objects.exclude(slug=slug) 

    return render(request, 'home/program_detail.html', {'program': program, 'news': news, 'program_list': program_list})


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('dashboard')
            elif user is not None and user.is_staff:
                login(request, user)
                return redirect('staff')
            elif user is not None and user.is_siswa:
                login(request, user)
                return redirect('siswa')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'register/login.html', {'form': form, 'msg': msg})


def logout_view(request):
    logout(request)
    return redirect('login_view')

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pesan anda berhasil dikirim')
            return redirect('contact_form')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})