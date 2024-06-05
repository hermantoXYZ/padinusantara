from django.urls import path
from . import views, viewsAdmin, viewsStaff, viewsSiswa


urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('halaman/<slug:slug>/', views.page_detail, name='page_detail'),
    path('contact/', views.contact_form, name='contact_form'),
    path('program/<slug:slug>/', views.program_detail, name='program_detail'),
    path('penerbit/', views.daftar_buku, name='penerbit'),




    path('dashboard/', viewsAdmin.admin, name='dashboard'),
    #adminpage
    path('staff/', viewsStaff.staff, name='staff'),
    path('staff/stats/', viewsStaff.stats, name='staff_stats'),
    path('staff/post/', viewsStaff.post_list, name='post_list'),
    path('staff/post/new/', viewsStaff.post_create, name='post_create'),
    path('staff/post/<int:pk>/edit/', viewsStaff.post_update, name='post_update'),
    path('staff/post/<int:pk>/delete/', viewsStaff.post_delete, name='post_delete'),
    path('media/', viewsStaff.media_list, name='media_list'),
    path('staff/media/', viewsStaff.media_list_staff, name='media_list_staff'),
    path('staff/media/new/', viewsStaff.media_create, name='media_create'),
    path('staff/media/<int:pk>/edit/', viewsStaff.media_update, name='media_update'),
    path('staff/media/<int:pk>/delete/', viewsStaff.media_delete, name='media_delete'),

    path('staff/contact/', viewsStaff.contact_list, name='contact_list'),
    path('staff/contact/<int:pk>/delete/', viewsStaff.contact_delete, name='contact_delete'),
    path('contact/<int:pk>/', viewsStaff.contact_open, name='contact_open'),

    path('staff/halaman/', viewsStaff.page_list_staff, name='page_list_staff'),
    path('staff/halaman/<int:pk>/edit/', viewsStaff.page_update, name='page_update'),


    #customer
    path('siswa/', viewsSiswa.siswa, name='siswa'),
    #employee
    
]