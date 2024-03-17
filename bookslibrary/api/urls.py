from django.urls import path
from .views import AllBooksView

urlpatterns = [
    path('books', AllBooksView.as_view(), name='all-books'),
]