from django.urls import path

from blog.views import index, about, client, contact, products, detail

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('client/', client, name='client'),
    path('contact/', contact, name='contact'),
    path('products/', products, name='products'),
    path('detail/<int:pk>/', detail, name='detail')

]