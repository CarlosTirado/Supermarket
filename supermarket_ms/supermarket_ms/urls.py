from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from supermarket_ms.views.category_view import CategoryList
from supermarket_ms.views.category_view import CategoryDetail
from supermarket_ms.views.product_view import ProductList
from supermarket_ms.views.product_view import ProductDetail
from supermarket_ms.views.color_view import ColorList
from supermarket_ms.views.color_view import ColorDetail

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>', CategoryDetail.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>', ProductDetail.as_view()),
    path('colors/', ColorList.as_view()),
    path('colors/<int:pk>', ColorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)