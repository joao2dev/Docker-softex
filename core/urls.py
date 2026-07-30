from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Servidor Django rodando com Docker!</h1><p>Status: OK</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]
