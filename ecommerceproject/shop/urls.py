from django.urls import path

from . import views
from .views import allProdCat

app_name = 'shop'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),

]
