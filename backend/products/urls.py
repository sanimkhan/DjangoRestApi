from django.urls import path

from products.migrations.views.generic_views import BookDetailView, BookListView
from products.migrations.views.views import product_detail

urlpatterns = [
    path('<int:pk>', product_detail),
    path('generics/<int:pk>/', BookDetailView.as_view()),
    path('generics/', BookListView.as_view()),
]
