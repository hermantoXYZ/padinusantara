
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_siswa(user):
    return user.is_authenticated and user.is_siswa

@user_passes_test(is_siswa)
def siswa(request):
    return render(request,'dashboard/siswa.html')