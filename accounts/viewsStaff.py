from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Stats, PostNews, Media, Contact, Page
from .forms import StatsForm, PostNewsForm, MediaForm, PageForm


def media_list(request):
    media_objects = Media.objects.all()
    posts = PostNews.objects.all()
    
    return render(request, 'home/media.html',{'posts': posts, 'media_objects': media_objects})

def is_staff(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_staff)
def staff(request):
    return render(request, 'staff/staff.html')

@user_passes_test(is_staff)
def stats(request):
    stats = Stats.objects.first()  # Ambil objek Stats pertama (jika ada)

    if request.method == 'POST':
        form = StatsForm(request.POST, instance=stats)
        if form.is_valid():
            form.save()
            return redirect('staff')
    else:
        form = StatsForm(instance=stats)

    return render(request, 'staff/stats.html', {'form': form})


@user_passes_test(is_staff)
def post_list(request):
    query = request.GET.get('q')
    if query:
        posts = PostNews.objects.filter(title__icontains=query).order_by('-created_at')
    else:
        posts = PostNews.objects.order_by('-created_at')
    
    return render(request, 'staff/post_list.html', {'posts': posts})

@user_passes_test(is_staff)
def post_create(request):
    if request.method == 'POST':
        form = PostNewsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostNewsForm()
    return render(request, 'staff/post_form.html', {'form': form})

@user_passes_test(is_staff)
def post_update(request, pk):
    post = get_object_or_404(PostNews, pk=pk)
    if request.method == 'POST':
        form = PostNewsForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostNewsForm(instance=post)
    return render(request, 'staff/post_form.html', {'form': form})

@user_passes_test(is_staff)
def post_delete(request, pk):
    post = get_object_or_404(PostNews, pk=pk)
    post.delete()
    return redirect('post_list')

@user_passes_test(is_staff)
def media_create(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('media_list_staff')  # Ganti 'home' dengan nama URL yang benar
    else:
        form = MediaForm()
    return render(request, 'staff/media_form.html', {'form': form})

@user_passes_test(is_staff)
def media_update(request, pk):
    media = get_object_or_404(Media, pk=pk)
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES, instance=media)
        if form.is_valid():
            form.save()
            return redirect('media_list_staff')
    else:
        form = MediaForm(instance=media)
    return render(request, 'staff/media_form.html', {'form': form})

@user_passes_test(is_staff)
def media_list_staff(request):
    media_objects = Media.objects.all()
    return render(request, 'staff/media_list.html', {'media_objects': media_objects})

@user_passes_test(is_staff)
def media_delete(request, pk):
    media = get_object_or_404(Media, pk=pk)
    media.delete()
    return redirect('media_list_staff')

@user_passes_test(is_staff)
def contact_list(request):
    contact_objects = Contact.objects.all()
    return render(request, 'staff/contact_list.html', {'contact_objects' : contact_objects})

@user_passes_test(is_staff)
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contact_list')

@user_passes_test(is_staff)
def contact_open(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'staff/contact_open.html', {'contact': contact})

@user_passes_test(is_staff)
def page_list_staff(request):
    page_objects = Page.objects.all()
    return render(request, 'staff/page_list.html', {'page_objects' : page_objects})

@user_passes_test(is_staff)
def page_update(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect('page_list_staff')
    else:
        form = PageForm(instance=page)
    return render(request, 'staff/page_form.html', {'form': form})