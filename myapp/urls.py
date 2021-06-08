from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='myapp'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('get_quote',views.get_quote, name='get_quote'),
    path('feedback',views.feedback, name='feedback'),
    
]