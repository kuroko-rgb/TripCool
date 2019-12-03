from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUs"),
    path('products/', views.products, name="Products"),
    path('contact/', views.contact, name="ContactUs"),
    path('products/<int:myid>', views.productView, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
    path('signup', views.signup, name ='signup'),
    path('accounts/',include('django.contrib.auth.urls'),)
]
