from django.urls import path, include
from .views import IndexView, ProductDetailView, ProfileDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('profiledetail/<pk>/', ProfileDetailView.as_view(), name='profile_detail'),
]
