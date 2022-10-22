from django.urls import path, include
from . import views

app_name = 'myshop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('read/<slug:slug>/1', views.read_book, name='read'),
    path('auth_user/', views.register),
    path('', include('django.contrib.auth.urls')),



]

